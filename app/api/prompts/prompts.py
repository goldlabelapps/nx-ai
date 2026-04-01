
from app import __version__

import os
from app.utils.make_meta import make_meta
from fastapi import APIRouter, Query, Path, status
from app.utils.db import get_db_connection
from app.api.prompts.schemas import PromptCreate, PromptOut
from fastapi import Body

router = APIRouter()
base_url = os.getenv("BASE_URL", "http://localhost:8000")

@router.get("/prompts")
def root() -> dict:
    """GET /prompts endpoint."""
    from fastapi import status
    meta = None
    data = []
    # Check if 'prompts' table exists
    from app.utils.db import get_db_connection_direct
    conn = get_db_connection_direct()
    try:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT EXISTS (
                    SELECT FROM information_schema.tables 
                    WHERE table_name = 'prompts'
                );
            """)
            result = cur.fetchone()
            exists = result[0] if result else False
    finally:
        conn.close()
    if not exists:
        meta = make_meta("warning", "Table 'prompts' does not exist.")
        # Do not include 'kata' key or any other keys in data
        response = {"meta": meta}
    else:
        meta = make_meta("success", "Prompts endpoint")
        # Example: include 'kata' key only if table exists (add as needed)
        data = [
            {"init": f"{base_url}/prompts", "kata": "example"},
        ]
        response = {"meta": meta, "data": data}
    # Remove 'kata' key from all items in data if table does not exist
    if not exists:
        for item in data:
            item.pop('kata', None)
    return response


# POST /prompts endpoint
@router.post("/prompts", status_code=status.HTTP_201_CREATED)
def create_prompt(prompt_in: PromptCreate = Body(...)):
    """Create a new prompt record in the prompts table."""
    from app.utils.db import get_db_connection_direct
    import psycopg2
    conn = get_db_connection_direct()
    try:
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO prompts (prompt, response, duration_ms, llm, timestamp)
                VALUES (%s, %s, %s, %s, COALESCE(%s, NOW()))
                RETURNING id, prompt, response, duration_ms, llm, timestamp
                """,
                (
                    prompt_in.prompt,
                    prompt_in.response,
                    prompt_in.duration_ms,
                    prompt_in.llm,
                    prompt_in.timestamp,
                )
            )
            row = cur.fetchone()
            conn.commit()
    except psycopg2.Error as e:
        conn.rollback()
        return {"error": str(e)}
    finally:
        conn.close()
    if row:
        keys = ["id", "prompt", "response", "duration_ms", "llm", "timestamp"]
        return dict(zip(keys, row))
    return {"error": "Failed to insert prompt."}
