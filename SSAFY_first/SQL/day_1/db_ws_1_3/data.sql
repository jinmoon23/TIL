-- Active: 1728549124370@@127.0.0.1@3306
-- 1. first_name이 '하'로 시작하는 모든 데이터 조회
SELECT
    *
FROM
    users
WHERE
    first_name LIKE '하%';

-- 2. phone이 '555'로 끝나는 모든 데이터 조회
SELECT
    *
FROM
    users
WHERE
    phone LIKE '%555';
-- 3. country가 '경상'으로 시작하는 모든 데이터 조회
SELECT
    *
FROM
    users
WHERE
    country LIKE '경상%';
-- 4. 다중 조건 쿼리
SELECT
    *
FROM
    users
WHERE
    country LIKE '__남%'
    AND (country LIKE '경%'
    OR country LIKE '충%'); 
    
    