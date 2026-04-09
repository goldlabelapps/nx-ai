-- Migration: Remove secondary_intent_topic column from prospects table
ALTER TABLE prospects DROP COLUMN IF EXISTS secondary_intent_topic;