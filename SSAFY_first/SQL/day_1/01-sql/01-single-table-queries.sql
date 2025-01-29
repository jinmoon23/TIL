-- Active: 1728520727319@@127.0.0.1@3306
-- 01. Querying data
SELECT 
    FirstName AS '이름'
FROM 
    employees;

SELECT
    LastName, FirstName
FROM
    employees;

SELECT
    *
FROM
    employees;

SELECT
    Name,
    Milliseconds / 60000 AS '재생 시간(분)'
FROM
    tracks;
-- 02. Sorting data
-- 오름차순(기본값)
SELECT
    FirstName
FROM
    employees
ORDER BY
firstName;
# 내림차순
SELECT
    FirstName
FROM
    employees
ORDER BY
firstName DESC;

SELECT
    Country,
    city
FROM
    customers
ORDER BY
    Country DESC;
    city;

SELECT
    Name,
    Milliseconds / 60000 AS '재생 시간(분)'
FROM
    tracks
ORDER BY
    Milliseconds DESC;
-- NULL 정렬 예시
SELECT
    ReportsTo
FROM
    employees
ORDER BY
    ReportsTo;
-- 03. Filtering data
# 기존의 데이터(중복이 존재)
SELECT 
    Country
FROM
    customers
ORDER BY
    Country;
# 중복되는 데이터를 제거하여 모든 국가의 수를 헤아릴 수 있다.
SELECT DISTINCT
    Country
FROM
    customers
ORDER BY
    Country;

# where절. filter의 핵심!!
SELECT 
    LastName,FirstName, City
FROM
    customers
WHERE
    City = 'Prague';

SELECT
    LastName,FirstName, City,Company
FROM
    customers
WHERE
    Company IS NULL
    AND Country = 'USA';

SELECT
    LastName,FirstName, City, Company
FROM
    customers
WHERE
    Company IS NULL
    OR Country = 'USA';

SELECT 
  Name, Bytes
FROM
  tracks
WHERE
  -- Bytes >= 10000
  -- AND Bytes <= 500000;
  Bytes BETWEEN 10000 AND 500000;

SELECT 
  Name, Bytes
FROM
  tracks
WHERE
  Bytes BETWEEN 10000 AND 500000
ORDER BY
  Bytes;

SELECT 
  LastName, FirstName, Country
FROM
  customers
WHERE
  -- Country = 'Canada'
  -- or Country = 'Germany'
  -- or Country = 'France';
  Country IN ('Canada','Germany','France');
  
 SELECT 
  LastName, FirstName, Country
FROM
  customers
WHERE
  Country NOT IN ('Canada','Germany','France'); 

# %: wildcard Charactor
# 0개 이상의 문자열과 일치 하는지 확인
SELECT
  LastName, FirstName
FROM
  customers
WHERE
  LastName LIKE '%son';

# ___:wildcard charactor
# 단일 문자와 일치하는지 확인
SELECT
  LastName, FirstName
FROM
  customers
WHERE
  FirstName LIKE '___a';

SELECT
  trackId, Name, Bytes
FROM
  tracks
ORDER BY
  Bytes DESC 
LIMIT 7;

SELECT
  trackId, Name, Bytes
FROM
  tracks
ORDER BY
  Bytes DESC
# OFFSET, 얼마나 띄울거야?, 거기부터 얼마나 확인할거야? 
LIMIT 3,4;
-- 04. Grouping data

SELECT
  Country, COUNT(*)
FROM
  customers
GROUP BY
  Country;