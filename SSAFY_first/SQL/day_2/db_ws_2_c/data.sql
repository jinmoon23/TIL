-- Active: 1728808817146@@127.0.0.1@3306
-- 1. 그룹화 / 각 나라별 총 판매액 조회
SELECT
    BillingCountry
    ,SUM(Total) AS TotalSales
FROM
    invoices
GROUP BY
    BillingCountry;

-- 2. 연도별 그룹화 / 각 연도별 총 판매액 조회
SELECT
    STRFTIME('%Y', InvoiceDate) AS Year,
    SUM(Total) AS Total_Sales
FROM
    invoices
GROUP BY
    Year;

-- 3. 조건 이후 그룹화 -> where
-- where과 having의 중요한 차이
-- 그룹화 하기 전에 조건을 설정하고 싶은 경우 where을 사용해야 하고
-- 그룹화 후에 해당 그룹에 대해 조건을 설정하고 싶은 경우 having을 사용해야 한다. 
SELECT
    BillingState,
    sum(Total) AS TotalSales
FROM
    invoices
WHERE
    BillingCountry = 'USA'
    AND InvoiceDate >= '2010-01-01'
GROUP BY
    BillingState;

-- 4. 조건 이후 그룹화 -> where
SELECT
    BillingCountry,
    max(Total) AS Max_Order_Amount
FROM
    invoices
WHERE
    BillingCountry = 'Germany'
    OR BillingCountry = 'France'
GROUP BY
    BillingCountry;
