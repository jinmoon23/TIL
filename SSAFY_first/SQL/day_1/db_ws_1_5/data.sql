-- Active: 1728616066303@@127.0.0.1@3306
-- 1. 이중 조건 처리
SELECT
    *
FROM
    users
WHERE
    age >= 30
    AND balance >= 1000

-- 2. 이중 조건 처리
SELECT
    *
FROM
    users
WHERE
    age <= 20
    AND balance <= 1000;

-- 3. 이중 조건 및 최대 나이 구하기
SELECT
    *
FROM
    users
WHERE
    first_name LIKE '현%'
    AND country = '제주특별자치도'
ORDER BY
    age DESC
LIMIT 1;

-- 4. 이중 조건 및 최소 나이 구하기
SELECT
    *
FROM
    users
WHERE
    last_name = '박'
    AND age >= 25
ORDER BY
    age
LIMIT 1;

-- 5. 이중 조건 및 소팅
SELECT
    *
FROM
    users
WHERE
    first_name = '재은'
    OR first_name = '영일'
ORDER BY
    balance DESC
LIMIT 1;

-- 6. 그룹화 및 소팅
SELECT 
    first_name,
    last_name,
    age,
    country,
    phone,
    max(balance) AS max_balance
FROM
    users
GROUP BY
    country
ORDER BY
    balance DESC;

-- 7. age >= 30 and balance > age>=30의 평균 balance
-- 괄호가 중요하다!!
SELECT
    *
FROM
    users
WHERE
    age >= 30
    AND balance > (SELECT
    avg(balance)
FROM
    users
WHERE
    age >= 30);
