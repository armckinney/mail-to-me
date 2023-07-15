from abc import ABC, abstractmethod
from smtplib import SMTP


class SMTPServer(SMTP, ABC):
    def __init__(self) -> None:
        super().__init__(self._get_host(), self._get_port())

    def initialize(self, user, password):
        self.ehlo()
        self.starttls()
        self.login(user, password)

    @abstractmethod
    def _get_host(self) -> str:
        # factory method for defining host
        raise NotImplementedError

    @abstractmethod
    def _get_port(self) -> int:
        # factory method for defining port
        raise NotImplementedError
