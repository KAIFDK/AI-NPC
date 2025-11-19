from datetime import datetime

def ts() -> str:
    return datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
