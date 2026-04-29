# README for Flickr API integration

This module provides API routes for accessing Flickr data, similar to the GitHub integration. It expects the following environment variables to be set in your .env file:

- FLICKR_USER
- FLICKR_KEY
- FLICKR_SECRET

### Route

- **GET /flickr**: Returns counts and recent records from all Flickr tables.

### Proposed Table Design

1. flickr_accounts
   - One row per Flickr account/user profile.
   - Stores account identity fields and full raw payload.
2. flickr_photos
   - One row per photo.
   - Stores photo metadata plus raw JSON payload.
3. flickr_albums
   - One row per album.
   - Stores album metadata plus raw JSON payload.
4. flickr_resources
   - Generic catch-all for any future Flickr resource type.
   - Supports additional Flickr objects through jsonb payload storage.

This structure mirrors the GitHub integration for consistency and flexibility.
