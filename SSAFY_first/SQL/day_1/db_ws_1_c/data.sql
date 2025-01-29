-- Active: 1728530829054@@127.0.0.1@3306
# 1. 장르를 기준으로 그룹화
SELECT 
    genre, COUNT(*) AS count
FROM
    songs
GROUP BY
    genre;

# 2. 그룹별 집계함수 사용
SELECT 
    genre, COUNT(*) AS count, AVG(duration) AS average_duration
FROM
    songs
GROUP BY
    genre;