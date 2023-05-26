from .smtp_server import SMTPServer


class GmailSMTPServer(SMTPServer):
    """
    Gmail implementation of abstract SMTPServer.
    """

    def _get_host(self) -> str:
        return "smtp.gmail.com"

    def _get_port(self) -> str:
        return 587
