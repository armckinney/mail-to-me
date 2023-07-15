from abc import ABC, abstractmethod
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import Dict


class SMTPMessage(ABC):
    """
    Abstract interface for an SMTPMessage.

    Should override __new__ for building a message,
    and can use __init__ for pass parameters for configuring subclasses.
    """

    @classmethod
    @abstractmethod
    def _build_message(cls) -> str:
        raise NotImplementedError

    def __new__(cls, sender: str, receiver: str, message_params: Dict[str, str]) -> str:
        msg = MIMEMultipart()
        msg["From"] = sender
        msg["To"] = receiver

        body = cls._build_message(sender, receiver, message_params)

        msg.attach(MIMEText(body, "plain"))
        # return msg.as_string()
        return body
