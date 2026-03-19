"""API route definitions for NX AI."""

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class EchoRequest(BaseModel):
    """Request body for the echo endpoint."""

    message: str


class EchoResponse(BaseModel):
    """Response body for the echo endpoint."""

    echo: str



import time
import sys
from app import __version__

@router.get("/")
def root() -> dict:
    """Return a structured welcome message for the API root."""
    epoch = int(time.time() * 1000)
    meta = {
        "version": __version__,
        "time": time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()),
        "epoch": epoch,
        "severity": "success",
        "message": "NX AI says hello.",
    }
    return {"meta": meta}


@router.get("/health")
def health() -> dict[str, str]:
    """Return the health status of the application."""
    return {"status": "ok"}


@router.post("/echo", response_model=EchoResponse)
def echo(body: EchoRequest) -> EchoResponse:
    """Echo the provided message back to the caller."""
    return EchoResponse(echo=body.message)
