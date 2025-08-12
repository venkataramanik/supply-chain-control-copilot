import os
import random

ARCADE_API_KEY = os.getenv("ARCADE_API_KEY")

def send_email(to: str, subject: str, body: str) -> str:
    # For first demo, mock when key missing
    if not ARCADE_API_KEY:
        return f"demo-email-{random.randint(100,999)}"
    # TODO: call Arcade.dev with API key; return email/message id
    return f"sent-email-{random.randint(1000,9999)}"
