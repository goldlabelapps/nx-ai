-- Migration: Add search_vector tsvector column to llm table
ALTER TABLE llm ADD COLUMN IF NOT EXISTS search_vector tsvector;

-- Optional: Create a GIN index for faster search
CREATE INDEX IF NOT EXISTS idx_llm_search_vector ON llm USING GIN(search_vector);