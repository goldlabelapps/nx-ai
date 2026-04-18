import os
from fastapi import APIRouter, HTTPException
from app.utils.make_meta import make_meta
from app.utils.db import get_db_connection_direct

router = APIRouter()

@router.post("/queue/empty")
def empty_queue_table() -> dict:
    """POST /queue/empty: Remove all records from the queue table."""
    try:
        conn = get_db_connection_direct()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM queue;")
        conn.commit()
        conn.close()
        return {"meta": make_meta("success", "Queue table emptied")}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
