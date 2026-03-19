"""NX AI - FastAPI entry point."""

from fastapi import FastAPI

from app.api.routes import router

app = FastAPI(
    title="NX AI",
    description="Production-ready Python FastAPI app for NX",
    version="1.0.0",
)

app.include_router(router)
