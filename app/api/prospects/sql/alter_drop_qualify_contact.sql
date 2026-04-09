-- Migration: Remove qualify_contact column from prospects table
ALTER TABLE prospects DROP COLUMN IF EXISTS qualify_contact;