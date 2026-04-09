-- Migration: Remove primary_email_verification_source column from prospects table
ALTER TABLE prospects DROP COLUMN IF EXISTS primary_email_verification_source;