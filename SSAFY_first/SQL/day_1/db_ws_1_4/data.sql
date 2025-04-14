-- 1. 전체 사용자 평균 나이
SELECT
    avg(age) as average_age
FROM
    users;

-- 2. 각 country 별 사용자 카운트하기
SELECT
    country,
    count(*) AS user_count
FROM
    users
GROUP BY
    country;

-- 3. 가장 많은 잔액 누구?
SELECT
    *
FROM
    users
ORDER BY
    balance DESC
LIMIT 1;

-- 4. 각 country별 평균 balance
SELECT
    country,
    avg(balance)
FROM   
    users
GROUP BY
    country;

-- 5. 가장 큰 잔고 - 가장 작은 잔고
SELECT
    max(balance)-min(balance) AS balance_difference
FROM
    users
ORDER BY
    balance DESC
LIMIT 1;