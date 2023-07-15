from mail_to_me.models import MailToMeStatus


class MailToMeError(Exception):
    status: MailToMeStatus

    def __init__(self, http_code, message) -> None:
        message = f"{self.__class__.__name__}:  {message}"
        self.status = MailToMeStatus(http_code, message)
