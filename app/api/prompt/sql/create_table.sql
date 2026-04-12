
CREATE TABLE IF NOT EXISTS llm (
	id SERIAL PRIMARY KEY,
	vector vector(1536),
	prompt TEXT NOT NULL,
	completion TEXT NOT NULL,
	duration FLOAT,
	time TIMESTAMPTZ DEFAULT NOW(),
	data JSONB,
	model TEXT,
	prospect_id INTEGER REFERENCES prospects(id)
);
