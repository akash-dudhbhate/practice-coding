"""SOLUTION: FastAPI async endpoints (Hard)"""
import asyncio
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class NotifyRequest(BaseModel):
    users: list[str]
    message: str

async def fetch_weather(city: str):
    await asyncio.sleep(1)  # simulate API call
    return {"city": city, "temp": 25, "condition": "sunny"}

async def send_notification(user: str, message: str):
    await asyncio.sleep(0.5)  # simulate sending
    return {"user": user, "status": "sent"}

@app.get("/weather/{city}")
async def get_weather(city: str):
    weather = await fetch_weather(city)
    return weather

@app.post("/notify")
async def notify(req: NotifyRequest):
    tasks = [send_notification(u, req.message) for u in req.users]
    results = await asyncio.gather(*tasks)
    return {"notifications": results}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
