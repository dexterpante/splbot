import logging
from typing import Any, Dict

import requests

from src.api.spl import configure_http_session, API_URLS

log = logging.getLogger(__name__)

http = configure_http_session()


def _post(url: str, data: Dict[str, Any]) -> bool:
    """Helper to POST data to an endpoint and return success flag."""
    try:
        response = http.post(url, json=data, timeout=10)
        response.raise_for_status()
        payload = response.json()
        if isinstance(payload, dict) and payload.get("status") == "success":
            return True
        return False
    except requests.exceptions.RequestException as exc:
        log.error("HTTP error calling %s: %s", url, exc)
        return False


def queue_battle(payload: Dict[str, Any]) -> bool:
    """Queue a battle with the given payload."""
    url = f"{API_URLS['base']}battle/queue"
    return _post(url, payload)


def submit_team(payload: Dict[str, Any]) -> bool:
    """Submit a team for an active battle."""
    url = f"{API_URLS['base']}battle/submit_team"
    return _post(url, payload)


def claim_rewards(payload: Dict[str, Any]) -> bool:
    """Claim player rewards."""
    url = f"{API_URLS['base']}players/claim_reward"
    return _post(url, payload)
