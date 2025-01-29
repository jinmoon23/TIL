-- Active: 1728531936731@@127.0.0.1@3306
# 1. 모든 데이터 조회
SELECT
    *
FROM
    users;

# 2. age 필드의 값이 18 미만인 유저 찾기
SELECT
    *
FROM
    users
WHERE
    age < 18

# 3. age가 18세 미만인 age와 phone 필드만 조회

SELECT
    age,
    phone
FROM
    users
WHERE
    age < 18
    