-- Active: 1728633022769@@127.0.0.1@3306
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