from fastapi import APIRouter, Depends, HTTPException

from app.utils.api_key_auth import get_api_key
from app.utils.db import get_db_connection_direct
from app.utils.make_meta import make_meta

router = APIRouter()


@router.post("/prompt/linkedin")
def linkedin_prompt_success(payload: dict, api_key: str = Depends(get_api_key)) -> dict:
    """POST /prompt/linkedin: return cached completion for linkedinUrl when available."""
    linkedin_url = (payload.get("linkedinUrl") or "").strip()
    if not linkedin_url:
        raise HTTPException(status_code=400, detail="Missing 'linkedinUrl' in request body.")

    conn = None
    cur = None
    try:
        conn = get_db_connection_direct()
        cur = conn.cursor()
        cur.execute(
            """
            SELECT id, completion, time, model, data
            FROM prompt
            WHERE (data->>'linkedinUrl' = %s OR prompt ILIKE %s)
            ORDER BY id DESC
            LIMIT 1;
            """,
            (linkedin_url, f"%{linkedin_url}%"),
        )
        row = cur.fetchone()

        if row:
            return {
                "meta": make_meta("success", "LinkedIn URL already analysed"),
                "data": {
                    "cached": True,
                    "id": row[0],
                    "linkedinUrl": linkedin_url,
                    "completion": row[1],
                    "time": row[2].isoformat() if row[2] else None,
                    "model": row[3],
                    "record_data": row[4],
                },
            }

        return {
            "meta": make_meta("warning", "LinkedIn URL not analysed yet"),
            "data": {
                "cached": False,
                "linkedinUrl": linkedin_url,
                "completion": None,
            },
        }
    except HTTPException:
        raise
    except Exception as e:
        return {
            "meta": make_meta("error", f"DB error: {str(e)}"),
            "data": {},
        }
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()
