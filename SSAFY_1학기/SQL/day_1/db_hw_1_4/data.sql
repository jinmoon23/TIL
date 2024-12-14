-- Active: 1728617737016@@127.0.0.1@3306
-- 1. 필드 내부에 포함여부 조회
SELECT
    *  
FROM
    tracks
WHERE
    Name LIKE '%love%';

-- 2. 다중 조건 및 소팅
SELECT
    *  
FROM
    tracks
WHERE
    GenreId = 1
    AND Milliseconds >= 300000
ORDER BY
    UnitPrice DESC;

-- 3. 그룹화 / 그룹 내부 데이터 카운팅
SELECT
    GenreId,
    COUNT(*) AS TotalTracks
FROM
    tracks
GROUP BY
    GenreId

-- 4. 그룹화 / 그룹 계 / 계 중 100 이상만 조회
SELECT
    GenreId,
    SUM(UnitPrice) AS TotalPrice 
FROM
    tracks
GROUP BY
    GenreId
HAVING
    TotalPrice >= 100;