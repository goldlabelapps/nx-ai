-- Migration: Remove email_confidence column from prospects table
ALTER TABLE prospects DROP COLUMN IF EXISTS email_confidence;