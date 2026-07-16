from typing import Any, Dict, Optional


def success_response(message: str, data: Optional[Any] = None, status_code: int = 200) -> Dict[str, Any]:
    payload: Dict[str, Any] = {"success": True, "message": message}
    if data is not None:
        payload["data"] = data
    return payload


def error_response(message: str, status_code: int = 400) -> Dict[str, Any]:
    return {"success": False, "message": message}
