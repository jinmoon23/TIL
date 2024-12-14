-- 1. species 컬럼 추가. 이 시점에서는 모든 species 열에 null 값이 들어가 있음
ALTER TABLE
    zoo
ADD COLUMN
    species TEXT;

-- 2. species 값 수정
UPDATE
    zoo
SET
    species = '3'
WHERE
    name = 'Monkey'

-- 3. height 값 수정
UPDATE
    zoo
SET
    height = height * 2.54

SELECT
    *
FROM
    zoo