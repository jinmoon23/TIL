-- Active: 1728529622210@@127.0.0.1@3306
# 1. 모든 데이터 조회
SELECT
	*
FROM
	songs;
# 2. 제목 기준 내림차순 정렬
SELECT
	*
FROM
	songs
ORDER BY
	title DESC;

# 3. 특정 장르의 음악만 조회
SELECT
	*
FROM
	songs
WHERE
	genre = 'Rock'

# 4. 플레이 시간이 3분 이상인 음악 데이터 조회
SELECT
	*
FROM
	songs
WHERE
	duration / 60 >= 3