-- Migration: Remove secondary_intent_score column from prospects table
ALTER TABLE prospects DROP COLUMN IF EXISTS secondary_intent_score;