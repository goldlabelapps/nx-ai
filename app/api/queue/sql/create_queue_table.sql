CREATE TABLE IF NOT EXISTS queue (
    id SERIAL PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    url TEXT,
    email_address TEXT,
    company TEXT,
    position TEXT,
    connected_on TEXT,
    created INTEGER,
    updated INTEGER,
    hidden BOOLEAN DEFAULT FALSE,
    collection TEXT
);