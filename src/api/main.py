from typing import Optional

from fastapi import Body, FastAPI, Request, status
from fastapi.templating import Jinja2Templates

from mail_to_me.config import EnvironmentConfigurationProvider
from mail_to_me.errors import MailToMeError, RecipientNotGivenError, SenderNotGivenError
from mail_to_me.models import MailToMeResponse, MailToMeStatus
from mail_to_me.smtp.message import MTMMessage
from mail_to_me.smtp.server import GmailSMTPServer
from mail_to_me.utils import parse_body

app = FastAPI()

templates = Jinja2Templates(directory="templates")
config = EnvironmentConfigurationProvider()


@app.get("/")
def root(request: Request):
    template = "index.html"
    context = {"request": request}
    return templates.TemplateResponse(template, context)


@app.post("/submit/")
def submit(
    request: Request,
    payload: str = Body(...),
    sender: Optional[str] = None,
    recipient: Optional[str] = None,
) -> None:
    try:
        params = parse_body(payload)

        if recipient is None and "recipient" not in params.keys():
            raise RecipientNotGivenError()

        if sender is None and "sender" not in params.keys():
            raise SenderNotGivenError()

        msg = MTMMessage(sender, recipient, params)

        # sending message
        with GmailSMTPServer() as server:
            # server.initialize(config.get("smtp_username"), config.get("smtp_password"))
            # server.sendmail(sender, recipient, msg)
            pass

        # formatting response
        mtm_status = MailToMeStatus(status.HTTP_200_OK, "Request Successful")
        data = {"recipient": recipient}

        return MailToMeResponse(mtm_status, data)

    # handling all known / expected errors
    except MailToMeError as e:
        return MailToMeResponse(e.status)

    # handling all unknown exceptions
    except Exception:
        unknown_error_status = MailToMeStatus(
            status.HTTP_500_INTERNAL_SERVER_ERROR, "Unknown Server Error Occured"
        )
        return MailToMeResponse(unknown_error_status)
