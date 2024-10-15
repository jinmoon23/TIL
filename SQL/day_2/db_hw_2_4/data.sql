-- Active: 1728960066352@@127.0.0.1@3306
-- orders 테이블 생성: 주문 정보를 저장하기 위한 테이블
CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,   -- 주문 ID (기본 키)
    order_date DATE,                -- 주문 날짜 (날짜 타입)
    total_amount REAL               -- 총 주문 금액 (실수 타입)
);

-- orders 테이블에 데이터 삽입
INSERT INTO orders (order_id, order_date, total_amount) VALUES
    (1, '2023-07-15', 50.99),      -- 2023년 7월 15일 주문, 총 주문 금액: 50.99
    (2, '2023-07-16', 75.50),      -- 2023년 7월 16일 주문, 총 주문 금액: 75.50
    (3, '2023-07-17', 30.25);      -- 2023년 7월 17일 주문, 총 주문 금액: 30.25

-- customers 테이블 생성: 고객 정보를 저장하기 위한 테이블
CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY, -- 고객 ID (기본 키)
    name TEXT,                      -- 고객 이름 (텍스트 타입)
    email TEXT,                     -- 고객 이메일 (텍스트 타입)
    phone TEXT                      -- 고객 전화번호 (텍스트 타입)
);

-- customers 테이블에 데이터 삽입
INSERT INTO customers (name, email, phone) VALUES
    ('허균', 'hong.gildong@example.com', '010-1234-5678'),    -- 허균 고객 정보
    ('김영희', 'kim.younghee@example.com', '010-9876-5432'),  -- 김영희 고객 정보
    ('이철수', 'lee.cheolsu@example.com', '010-5555-4444');    -- 이철수 고객 정보

-- orders 테이블에서 order_id가 3인 주문 정보 삭제
DELETE FROM orders WHERE order_id = 3;

-- customers 테이블에서 customer_id가 1인 고객의 이름을 '홍길동'으로 수정
UPDATE customers SET name = '홍길동' WHERE customer_id = 1;

-- orders 테이블의 모든 데이터 조회
SELECT * FROM orders;

-- customers 테이블의 모든 데이터 조회
SELECT * FROM customers;

-- 1. orders 테이블 자체를 삭제
DROP TABLE orders;

-- 2. orders 테이블 재생성
CREATE TABLE orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_date DATE,
    total_amount REAL,
    customerId INTEGER,
    -- customers 테이블과 관계 맺기
    Foreign Key (customerId) 
        REFERENCES customers(customer_id)
);

-- 3-1. orders 테이블에 컬럼 추가
ALTER TABLE orders
ADD COLUMN
    price INTEGER;

-- 3-2. orders 테이블에서 컬럼 삭제
ALTER TABLE orders
DROP COLUMN
    total_amount;

-- 4. 3개 이상의 orders 레코드 생성
INSERT INTO orders (
    id, order_date, customerId, price
)
VALUES
(1, '2024-10-13', 1, 50 ),
(2, '2024-10-14', 2, 70 ),
(3, '2024-10-15', 2, 100 );

-- 5. orders의 모든 데이터 조회
-- but! 관계를 맺고 있는 customers의 name도 함께 조회한다. 
SELECT id, name, order_date, price
FROM orders
INNER JOIN customers
    ON customers.customer_id = orders.customerId; 