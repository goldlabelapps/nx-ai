import os
from fastapi import APIRouter, HTTPException
from app.utils.make_meta import make_meta
from app.utils.db import get_db_connection_direct

router = APIRouter()

@router.post("/queue/create")
def create_queue_table() -> dict:
    """POST /queue/create: Create the queue table from SQL script."""
    try:
        sql_path = os.path.join(os.path.dirname(__file__), "../sql/create_queue_table.sql")
        with open(sql_path, "r") as f:
            sql = f.read()
        conn = get_db_connection_direct()
        cursor = conn.cursor()
        # Split SQL script into individual statements for PostgreSQL
        statements = [s.strip() for s in sql.split(';') if s.strip()]
        for statement in statements:
            cursor.execute(statement)
        conn.commit()
        conn.close()
        return {"meta": make_meta("success", "Queue table created")}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
