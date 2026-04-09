-- Migration: Remove do_not_call column from prospects table
ALTER TABLE prospects DROP COLUMN IF EXISTS do_not_call;