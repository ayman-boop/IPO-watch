import os
import httpx
import json
from pathlib import Path


#Reads .env from the project root, wherever the script is run from.
#Missing file is fine; variables already set in the shell win.
ENV_PATH = Path(__file__).resolve().parent.parent / ".env"
if ENV_PATH.exists():
    for line in ENV_PATH.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            key, value = line.split("=", 1)
            os.environ.setdefault(key.strip(), value.strip().strip('"'))

def get(url):
    if "SEC_USER_AGENT" not in os.environ:
        raise RuntimeError("SEC_USER_AGENT is not set: copy .env.example to .env and fill it in")
    response=httpx.get(url,headers={"User-Agent":os.environ["SEC_USER_AGENT"]})
    response.raise_for_status()
    return response.content

def get_json(url):
    call=get(url)
    return json.loads(call)

if __name__ == "__main__":
    data = get_json("https://data.sec.gov/submissions/CIK0001946563.json")
    print("company:", data["name"])