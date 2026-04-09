-- Migration: Remove home_phone column from prospects table
ALTER TABLE prospects DROP COLUMN IF EXISTS home_phone;