from fastapi import status

from .mail_to_me_error import MailToMeError


class PayloadParseError(MailToMeError):
    def __init__(self) -> None:
        message = "Unable to parse given body."
        super().__init__(status.HTTP_400_BAD_REQUEST, message)
