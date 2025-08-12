import os
from typing import Dict, Any

USE_LANGSMITH = bool(os.getenv("LANGSMITH_API_KEY"))

def log_trace(event: str, payload: Dict[str, Any]):
    # Minimal no-op logger that won't fail
    if USE_LANGSMITH:
        # TODO: integrate with LangSmith client; placeholder to avoid runtime errors
        pass
    # You can also push to your own webhook/log store here.
    return True
