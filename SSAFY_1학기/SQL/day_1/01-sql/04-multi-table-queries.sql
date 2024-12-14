-- 공통
SELECT * FROM articles;
SELECT * FROM users;
DROP TABLE articles;
DROP TABLE users;
PRAGMA table_info('articles');


-- 실습용 데이터
CREATE TABLE users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name VARCHAR(50) NOT NULL
);

CREATE TABLE articles (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title VARCHAR(50) NOT NULL,
  content VARCHAR(100) NOT NULL,
  userId INTEGER NOT NULL,
  -- userId 컬럼은 외래키로 지정할 거야.
  -- 외래키로 지정 시 반드시 따라붙는 옵션이 있는데 그것은 REFERENCES
  -- userId 외래키는 users 테이블의 id 컬럼을 참조한다.
  FOREIGN KEY (
    userId
    ) 
    REFERENCES users(id)
);

INSERT INTO 
  users (
    name
  )
VALUES 
  ('하석주'),
  ('송윤미'),
  ('유하선');

INSERT INTO
  articles (title, content, userId)
VALUES 
  ('제목1', '내용1', 1),
  ('제목2', '내용2', 2),
  ('제목3', '내용3', 1),
  ('제목4', '내용4', 4),
  ('제목5', '내용5', 1);
-- INNER JOIN
  -- 교집합이라고 생각하면 편함
SELECT
  *
FROM
  articles
INNER JOIN
  users
  ON users.id = articles.userId;

-- '하석주'라는 이름의 작성자가 작성한 모든 articles를 조회하는 문장
-- LEFT JOIN
SELECT
  *
FROM
  articles
LEFT JOIN
  users
  ON users.id = articles.userId;
-- rightjoin
SELECT
  *
FROM
  articles
RIGHT JOIN
  users
  ON users.id = articles.userId;