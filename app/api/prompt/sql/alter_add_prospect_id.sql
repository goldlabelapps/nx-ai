-- Migration: Add prospect_id column to llm table
ALTER TABLE llm ADD COLUMN IF NOT EXISTS prospect_id INTEGER REFERENCES prospects(id);