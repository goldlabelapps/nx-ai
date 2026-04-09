-- Migration: Remove primary_intent_score column from prospects table
ALTER TABLE prospects DROP COLUMN IF EXISTS primary_intent_score;