import os
import httpx

for line in open(".env"):
    line = line.strip()
    if line and not line.startswith("#"):
        key, value = line.split("=", 1)
        os.environ[key]=value.strip('"')