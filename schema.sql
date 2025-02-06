-- schema.sql
CREATE TABLE users (
    me_id TEXT PRIMARY KEY CHECK(me_id LIKE 'Me#%'),
    location TEXT,  -- 'LAT,LNG' format
    skills JSON DEFAULT '[]',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE help_relations (
    helper_id TEXT REFERENCES users(me_id),
    helped_id TEXT REFERENCES users(me_id),
    rating INTEGER CHECK (rating BETWEEN 1 AND 5),
    problem_type TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (helper_id, helped_id)
);
