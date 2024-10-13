CREATE TABLE orders (
    order_date DATE,
    total_amount REAL
);

INSERT INTO orders (
    order_date, total_amount
)
VALUES 
('2024-10-01', 12.23),
('2024-10-02', 12.24);

CREATE TABLE customers (
    name TEXT,
    email TEXT,
    phone TEXT
);

INSERT INTO customers (
    name, email, phone
)
VALUES
('진문', 'rlawjsdlf13@naver.com','010-2922-8021'),
('가은', 'jgu1223@hanmail.net','010-3919-9677'),
('엄마', 'youngagu@naver.com','010-2435-8021');

DELETE FROM 
    orders
WHERE
    total_amount = 12.24;

UPDATE 
    customers
set 
    name = '홍길동'
WHERE
    name = '진문';

SELECT
    *
FROM
    orders;

SELECT
    *
FROM
    customers;