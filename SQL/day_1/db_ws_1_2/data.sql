-- Active: 1728546047452@@127.0.0.1@3306
-- 1. age < 18 인 유저만 내림차순 정렬
SELECT
    *
FROM
    users
WHERE
    age < 18
ORDER BY
    age DESC;

-- 2. lastname, age 필드만 출력 / lastname 기준 오름차순 정렬
-- lastname이 같은 경우 age 기준 내림차순 정렬 조회 

# 3. 조회(접근)하여
SELECT 
    last_name,
    age
--  1. users 테이블에서
FROM
    users
-- 2. age가 18 미만인 경우의 모든 데이터를
WHERE
    age < 18
-- 4. last_name 기준 오름차순 정렬 후 age를 기준으로 내림차순 정렬하여
-- 값으로 출력함
ORDER BY
    last_name,
    age DESC;

-- 3. 2번과 동일한 조회를 하되, 중복데이터를 제외하고 조회결과 출력

SELECT DISTINCT
    last_name,
    age
FROM
    users
WHERE
    age < 18
ORDER BY
    last_name,
    age DESC;