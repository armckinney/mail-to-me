from fastapi import status

from .mail_to_me_error import MailToMeError


class RecipientNotGivenError(MailToMeError):
    def __init__(self) -> None:
        message = "Parameter 'recipient' was not found. Include as query parameter or in Form / Body of request."
        super().__init__(status.HTTP_400_BAD_REQUEST, message)
