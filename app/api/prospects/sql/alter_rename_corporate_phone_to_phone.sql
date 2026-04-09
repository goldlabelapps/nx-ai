-- Migration: Rename corporate_phone column to phone in prospects table
ALTER TABLE prospects RENAME COLUMN corporate_phone TO phone;