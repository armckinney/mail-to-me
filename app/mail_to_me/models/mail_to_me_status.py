from dataclasses import dataclass


@dataclass
class MailToMeStatus:
    http_code: int
    message: str
