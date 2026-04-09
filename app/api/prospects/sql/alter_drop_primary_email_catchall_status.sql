-- Migration: Remove primary_email_catchall_status column from prospects table
ALTER TABLE prospects DROP COLUMN IF EXISTS primary_email_catchall_status;