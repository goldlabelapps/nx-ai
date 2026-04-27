from app import __version__
from fastapi import APIRouter
import os, time
from dotenv import load_dotenv
from app import __version__

router = APIRouter()

@router.get("/")
def root() -> dict:
    """"Python°"""
    load_dotenv()
    base_url = os.getenv("BASE_URL", "http://localhost:8000")
    meta = {
        "title": "Python°",
        "version": __version__,
        "base": base_url,
    }
    
    return {"meta": meta}
