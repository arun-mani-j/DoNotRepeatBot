DROP TABLE IF EXISTS snippets;

CREATE TABLE snippets (
       chat_id BIGINT,
       title TEXT,
       snippet TEXT NOT NULL,
       PRIMARY KEY (user_id, title)
);
