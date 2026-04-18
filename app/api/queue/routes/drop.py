import os
from fastapi import APIRouter, HTTPException
from app.utils.make_meta import make_meta
from app.utils.db import get_db_connection_direct

router = APIRouter()

@router.post("/queue/drop")
def drop_queue_table() -> dict:
    """POST /queue/drop: Drop the queue table."""
    try:
        conn = get_db_connection_direct()
        cursor = conn.cursor()
        cursor.execute("DROP TABLE IF EXISTS queue;")
        conn.commit()
        conn.close()
        return {"meta": make_meta("success", "Queue table dropped")}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
