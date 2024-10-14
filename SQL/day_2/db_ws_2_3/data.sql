SELECT
    *
FROM
    hotels

-- 1. grade 필드 값을 모두 대문자로 수정
UPDATE
    hotels
SET
    grade = upper(grade)

CREATE TABLE customers (
    name TEXT,
    email TEXT
);

ALTER TABLE 
    customers
ADD COLUMN
    id INT;

CREATE TABLE reservations (
    id INTEGER NOT NULL,
    Foreign Key () REFERENCES ()
)