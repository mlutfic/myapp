CREATE TABLE IF NOT EXISTS friends (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100)
);

INSERT INTO friends (name) VALUES ('Nindya'), ('Ratna'), ('Lutfi');

