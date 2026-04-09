-- Migration: Remove cleaned column from prospects table
ALTER TABLE prospects DROP COLUMN IF EXISTS cleaned;