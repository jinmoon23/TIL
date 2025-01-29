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
-- 2. reservations 테이블과 hotels / customers 테이블 관계 맺기
CREATE TABLE reservations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    room INTEGER NOT NULL,
    customer INTEGER NOT NULL,
    Foreign Key (room) 
        REFERENCES hotels(room_num)
    Foreign Key (customer) 
        REFERENCES customers(id)
);

INSERT INTO customers (
    name, email, id
)
VALUES
('홍길동', '1234@naver.com',1),
('나선욱', '5678@naver.com',2),
('홍발동', '91011@naver.com',3),
('비비빅', '121314@naver.com',4);