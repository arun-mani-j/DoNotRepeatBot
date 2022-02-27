DROP TABLE IF EXISTS snippets;
DROP TABLE IF EXISTS chats;

CREATE TABLE chats (
       chat_id BIGINT PRIMARY KEY,
       lang TEXT NOT NULL DEFAULT 'en'
);

CREATE TABLE snippets (
       snippet_id TEXT GENERATED ALWAYS AS (MD5(chat_id::TEXT || title)) STORED,
       chat_id BIGINT REFERENCES chats ON DELETE CASCADE,
       title TEXT,
       body TEXT,
       file_id TEXT,
       file_type INTEGER,
       vectorized TSVECTOR GENERATED ALWAYS AS
                  (TO_TSVECTOR('english', COALESCE(title, '') || ' ' || COALESCE(body, ''))) STORED,
       usage INTEGER DEFAULT 0,
       PRIMARY KEY (chat_id, title)
);

CREATE INDEX vectorized_idx ON snippets USING GIN (vectorized);
