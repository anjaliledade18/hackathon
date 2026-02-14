from fastapi import FastAPI, Security, HTTPException, status
from fastapi.security.api_key import APIKeyHeader
from dotenv import load_dotenv
import os


load_dotenv()

app = FastAPI()

@app.get("/test")
def test():
    return {"status": "working"}

API_KEY = os.getenv("FASTAPI_SECRET_KEY")

# Header name client must send
API_KEY_NAME = "x-api-key"

api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)


def verify_api_key(api_key: str = Security(api_key_header)):

    if api_key == API_KEY:
        return api_key

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid API Key",
    )


@app.get("/secure-data")
def secure_endpoint(api_key: str = Security(verify_api_key)):
    return {"message": "Access granted"}
