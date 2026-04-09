-- Migration: Remove tertiary_email_verification_source column from prospects table
ALTER TABLE prospects DROP COLUMN IF EXISTS tertiary_email_verification_source;