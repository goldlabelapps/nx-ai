from pydantic import BaseModel
from typing import Optional

class PromptCreate(BaseModel):
    prompt: str
    response: str
    duration_ms: int
    llm: str
    timestamp: Optional[str] = None  # ISO format, optional for auto

class PromptOut(BaseModel):
    id: int
    prompt: str
    response: str
    duration_ms: int
    llm: str
    timestamp: str
