from dataclasses import dataclass
from typing import Any, Dict, Optional

from .mail_to_me_status import MailToMeStatus


@dataclass
class MailToMeResponse:
    status: MailToMeStatus
    data: Optional[Dict[Any, Any]] = None
