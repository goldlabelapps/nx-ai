import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../..')))
from app.utils.db import get_db_connection_direct

if __name__ == "__main__":
    sql = """
    ALTER TABLE llm ADD COLUMN IF NOT EXISTS search_vector tsvector;
    CREATE INDEX IF NOT EXISTS idx_llm_search_vector ON llm USING GIN(search_vector);
    """
    conn = get_db_connection_direct()
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    cur.close()
    conn.close()
    print("Migration complete: search_vector column and index added to llm table.")
