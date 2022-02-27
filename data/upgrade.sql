/*
Upgrade from DoNotRepeatBot v2 to DoNotRepeatBot v3.
*/

CREATE TEMPORARY TABLE snippets_temp (
       chat_id BIGINT,
       title TEXT,
       snippet TEXT NOT NULL,
       usage INTEGER DEFAULT 0,
       PRIMARY KEY (chat_id, title)
);

INSERT INTO snippets_temp (SELECT * FROM snippets);

\i data/schema.sql

INSERT INTO chats (SELECT DISTINCT chat_id, 'en' FROM snippets_temp);
INSERT INTO snippets (chat_id, title, body, file_type, usage) (SELECT chat_id, title, snippet, 30, usage FROM snippets_temp);
DROP TABLE snippets_temp;
COMMIT;
