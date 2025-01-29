-- Active: 1728531296965@@127.0.0.1@3306
# 1. tracks 테이블의 모든 데이터를 조회
SELECT 
    * 
FROM
    tracks;

# 2. 특정한 필드의 데이터만 조회
SELECT
    Name, Milliseconds, UnitPrice
FROM
    tracks;

# 3. 조건을 활용한 데이터 조회
SELECT
    *
FROM
    tracks
WHERE
    GenreId = 1;

# 4. order by를 활용한 데이터 정렬 
SELECT 
    *
FROM
    tracks
ORDER BY
    Name;

# 5. limit을 활용한 제한적 데이터 조회
SELECT
    *
FROM
    tracks
LIMIT 10