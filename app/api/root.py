from app import __version__
from fastapi import APIRouter
import os, time
from dotenv import load_dotenv
from app import __version__

router = APIRouter()

@router.get("/")
def root() -> dict:
    """NX-AI."""
    load_dotenv()
    base_url = os.getenv("BASE_URL", "http://localhost:8000")
    epoch = int(time.time() * 1000)
    meta = {
        "title": "Python",
        "severity": "success",
        "version": __version__,
        "base_url": base_url,
        "time": epoch,
    }
    endpoints = [
        {"name": "health", "url": f"{base_url}/health"},
        {
            "name": "orders", 
            "endpoints": [
                {"name": "list", "url": f"{base_url}/orders"},
            ]
        },
        {
            "name": "prospects", 
            "endpoints": [
                {"name": "list", "url": f"{base_url}/prospects"},
            ]
        },
        {
            "name": "llm", 
            "endpoints": [
                {"name": "list", "url": f"{base_url}/llm"},
            ]
        },
        {"name": "docs", "url": f"{base_url}/docs"},
    ]
    return {"meta": meta, "data": endpoints}
