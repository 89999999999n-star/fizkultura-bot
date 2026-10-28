from fastapi import FastAPI
from platinum.check_sub import check_subscription
from telegram import Bot
import os

app = FastAPI()

@app.get("/api/health")
async def health():
    return {"status": "ok"}

from fastapi import HTTPException
from pydantic import BaseModel

class SubscriptionRequest(BaseModel):
    init_data: str


@app.post("/api/check-subscription")
async def check_subscription_api(request: SubscriptionRequest):
    if not request.init_data:
        raise HTTPException(status_code=401, detail="Telegram authentication required")
    raise HTTPException(
        status_code=503,
        detail="Secure Telegram verification is not connected yet"
    )
