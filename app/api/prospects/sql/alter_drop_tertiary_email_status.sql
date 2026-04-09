-- Migration: Remove tertiary_email_status column from prospects table
ALTER TABLE prospects DROP COLUMN IF EXISTS tertiary_email_status;