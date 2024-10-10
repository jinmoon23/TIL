-- 공통
SELECT * FROM articles;
DROP TABLE articles;
PRAGMA table_info('articles');

CREATE TABLE articles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(100) NOT NULL,
    content text NOT NULL,
    created_at DATE NOT NULL
);
-- 1. Insert data into table
INSERT INTO 
    articles(
        title, content, created_at
    )
VALUES (
    '제목 5', '내용 5', '2000-01-01'
);
-- 2. Update data in table
UPDATE
    articles
-- 어떤 컬럼에 어떤 data를 set 할거야
SET
    title = 'update title'
WHERE
    id = 1;

-- 3. Delete data from table
DELETE FROM 
    articles
WHERE
    id = 1;

DELETE FROM 
    artists
WHERE
    ArtistId IN (
        SELECT
            ArtistId
        FROM
            artists
        ORDER BY
            Name
        LIMIT 2
    );

