-- Migration: Remove work_direct_phone column from prospects table
ALTER TABLE prospects DROP COLUMN IF EXISTS work_direct_phone;