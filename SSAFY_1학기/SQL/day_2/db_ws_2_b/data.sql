-- Active: 1728632163389@@127.0.0.1@3306
-- 1. 특정 컬럼 데이터만 조회
SELECT
    InvoiceId,
    InvoiceDate
FROM
    invoices;

-- 2. 조건 만족하는 데이터 조회
SELECT
    *
FROM
    invoices
WHERE
    BillingCountry = 'USA'
    AND Total >= 10;

-- 3. 조건 만족하는 데이터 조회
SELECT
    *
FROM
    invoices
WHERE
    BillingCity = 'London'
    OR BillingCity = 'Berlin';

-- 4. Total 최대값 출력
SELECT
    *
FROM
    invoices
ORDER BY
    Total DESC
LIMIT 1;

-- 5. 이중 조건 조회
SELECT
    *
FROM
    invoices
WHERE
    InvoiceDate >= '2013-03-31'
    AND Total > 3;

-- 6. 조건 만족하는 데이터 조회
SELECT
    *
FROM
    invoices
WHERE
    BillingCountry = 'USA'
    AND BillingState = 'CA'
    AND Total > 10;

-- 7. 조건 만족하는 데이터 조회
SELECT
    *
FROM
    invoices
WHERE
    BillingCountry = 'Canada'
    AND BillingState = 'ON'
    AND BillingCity = 'Toronto';

-- 8. 조건 만족하는 데이터 조회
SELECT
    *
FROM
    invoices
WHERE
    InvoiceDate < '2023-01-01'
    AND (
        Total >= 50
        OR BillingCountry = 'Brazil'
    );