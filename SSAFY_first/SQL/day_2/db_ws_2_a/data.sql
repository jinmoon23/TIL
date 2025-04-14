-- Active: 1728631404942@@127.0.0.1@3306
-- 1. 모든 데이터 조회
SELECT
    *
FROM
    artists;

-- 2. 모든 데이터의 수를 조회
SELECT
    COUNT(*)
FROM
    artists;

-- 3. 특정 레코드 조회
SELECT
    *
FROM
    artists
WHERE
    Name = 'AC/DC';

-- 4. 특정 컬럼만 출력
SELECT
    ArtistId,
    Name
FROM
    artists;
    
-- 5. 조건 충족하는 레코드 출력
SELECT
    *
FROM
    artists
WHERE
    Name = 'Gilberto Gil'
    OR Name = 'Ed Motta';

-- 6. 소팅
SELECT
    *
FROM
    artists
ORDER BY
    Name DESC;

-- 7. 시작하는 정보 조회 및 LIMIT
SELECT
    *
FROM
    artists
WHERE
    Name LIKE 'Vinícius%'
LIMIT 2;

-- 8. 특정한 데이터만 골라서 조회
SELECT
    ArtistId
FROM
    artists
WHERE
    ArtistId BETWEEN 50 AND 70;