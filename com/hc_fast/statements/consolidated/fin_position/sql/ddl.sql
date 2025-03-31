-- ddl.sql
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE TABLE fin_position (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    company_id UUID NOT NULL,
    name TEXT NOT NULL,
    indent INTEGER NOT NULL CHECK (indent >= 0),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
