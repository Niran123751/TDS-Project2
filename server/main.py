from fastapi import FastAPI, Request, HTTPException
from dotenv import load_dotenv
import os
from server.solve_quiz import solve_quiz
from loguru import logger

load_dotenv()
SECRET = os.getenv("NIRANJAN2025TDS")

app = FastAPI()

@app.post("/solve")
async def solve(request: Request):
    try:
        payload = await request.json()
    except:
        raise HTTPException(status_code=400, detail="Invalid JSON")

    if payload.get("secret") != SECRET:
        raise HTTPException(status_code=403, detail="Invalid secret")

    logger.info(f"Solving quiz: {payload.get('url')}")
    return await solve_quiz(payload)
