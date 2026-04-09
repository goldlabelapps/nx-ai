-- Migration: Remove tertiary_email column from prospects table
ALTER TABLE prospects DROP COLUMN IF EXISTS tertiary_email;