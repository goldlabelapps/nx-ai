from fastapi import APIRouter, Depends

from app.utils.api_key_auth import get_api_key
from app.utils.make_meta import make_meta

router = APIRouter()


@router.post("/prompt/linkedin")
def linkedin_prompt_success(api_key: str = Depends(get_api_key)) -> dict:
    """POST /prompt/linkedin: Success stub endpoint."""
    return {
        "meta": make_meta("success", "LinkedIn prompt endpoint working"),
        "message": "LinkedIn prompt endpoint is live.",
    }
