DROP TABLE IF EXISTS snippets;
DROP TABLE IF EXISTS common_snippets;

CREATE TABLE snippets (
       user_id BIGINT,
       title TEXT,
       snippet TEXT NOT NULL,
       PRIMARY KEY (user_id, title)
);

CREATE TABLE common_snippets (
       title TEXT PRIMARY KEY,
       snippet TEXT NOT NULL
);
