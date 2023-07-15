import os
from typing import Optional, Dict
from pathlib import Path
from typing import Final


from fastapi import Body, FastAPI, Request, status
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from mail_to_me.config import EnvironmentConfigurationProvider
from mail_to_me.errors import MailToMeError, RecipientNotGivenError, SenderNotGivenError
from mail_to_me.models import MailToMeResponse, MailToMeStatus
from mail_to_me.smtp.message import MTMMessage
from mail_to_me.smtp.server import GmailSMTPServer
from mail_to_me.utils import parse_body

__APP_ROOT: Final[str] = str(Path(__file__).parent)

app = FastAPI()

templates = Jinja2Templates(directory="templates")
config = EnvironmentConfigurationProvider()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods="GET",
    allow_headers=["*"],
)
app.mount(
    "/static",
    StaticFiles(directory=os.path.join(__APP_ROOT, "static")),
    name="static",
)


@app.get("/")
def root(request: Request):
    template = "index.html"
    context = {"request": request}
    return templates.TemplateResponse(template, context)


@app.get("/nopost")
def nopost(request: Request):
    template = "nopost.html"
    context = {"request": request}
    return templates.TemplateResponse(template, context)


@app.get("/post")
def post(request: Request):
    template = "post.html"
    context = {"request": request, "recipient": "<recipient>"}
    return templates.TemplateResponse(template, context)


@app.get("/demo")
def demo(request: Request):
    template = "demo.html"
    context = {"request": request}
    return templates.TemplateResponse(template, context)


def _send_message(
    params: Dict[str, str],
    sender: Optional[str] = None,
    recipient: Optional[str] = None,
) -> None:
    if recipient is None:
        recipient = params.get("recipient")
        if "recipient" not in params.keys():
            raise RecipientNotGivenError()

    if sender is None:
        sender = params.get("sender")
        if "sender" not in params.keys():
            raise SenderNotGivenError()

    msg = MTMMessage(sender, recipient, params)

    # sending message
    with GmailSMTPServer() as server:
        server.initialize(config.get("smtp_username"), config.get("smtp_password"))
        server.sendmail(sender, recipient, msg)


@app.post("/submit")
def submit(
    request: Request,
    payload: str = Body(...),
    sender: Optional[str] = None,
    recipient: Optional[str] = None,
) -> None:

    try:
        params = parse_body(payload)
        _send_message(params, sender, recipient)
        template = "post.html"

    except Exception:
        template = "nopost.html"

    context = {
        "request": request,
        "recipient": recipient if recipient is not None else params.get("recipient"),
    }
    return templates.TemplateResponse(template, context)


@app.post("/api/submit")
def api_submit(
    request: Request,
    payload: str = Body(...),
    sender: Optional[str] = None,
    recipient: Optional[str] = None,
) -> None:
    try:
        params = parse_body(payload)
        _send_message(params, sender, recipient)

        # formatting response
        mtm_status = MailToMeStatus(status.HTTP_200_OK, "Request Successful")

        return MailToMeResponse(mtm_status, params)

    # handling all known / expected errors
    except MailToMeError as e:
        return MailToMeResponse(e.status, params)

    # handling all unknown exceptions
    except Exception as e:
        unknown_error_status = MailToMeStatus(
            status.HTTP_500_INTERNAL_SERVER_ERROR, "Unknown Server Error Occured"
        )
        return MailToMeResponse(unknown_error_status, str(e))
