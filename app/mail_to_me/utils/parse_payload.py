from typing import Dict
from urllib.parse import parse_qs

from mail_to_me.errors import PayloadParseError


def parse_body(payload: str) -> Dict[str, str]:
    try:
        params = {k: v[0] for k, v in parse_qs(payload).items()}
    except Exception:
        raise PayloadParseError()

    return params
