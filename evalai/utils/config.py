# Store all the varibales here
import os

from os.path import expanduser


LEN_OF_TOKEN = 40

AUTH_TOKEN_FILE_NAME = "token.json"

HOST_URL_FILE_NAME = "host_url"

AUTH_TOKEN_DIR = expanduser("~/.evalai/")

AUTH_TOKEN_PATH = os.path.join(AUTH_TOKEN_DIR, AUTH_TOKEN_FILE_NAME)

API_HOST_URL = os.environ.get("EVALAI_API_URL", "https://evalapi.cloudcv.org")

EVALAI_ERROR_CODES = [400, 401, 406]

HOST_URL_FILE_PATH = os.path.join(AUTH_TOKEN_DIR, HOST_URL_FILE_NAME)

EVALAI_HOST_URLS = [
    "https://evalai.cloudcv.org",
    "https://evalai-staging.cloudcv.org",
    "http://localhost:8888",
]

EVALAI_API_URLS = [
    "https://evalapi.cloudcv.org",
    "http://localhost:8000",
]
