# MySQL DB 암호화

## 회원관리 테이블 생성 Query
```sql
CREATE TABLE members (
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(128) NOT NULL,
    email VARCHAR(255) NOT NULL,
    full_name VARCHAR(100) NOT NULL,
    account_number VARBINARY(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```
## 회원가입
```sql
SET @encryption_key = SHA2('MySecretKey', 256);

INSERT INTO members (username, password, email, full_name)
VALUES (
    'newuser',
    SHA2('user_password', 512),
    'user@example.com',
    AES_ENCRYPT('John Doe', @encryption_key)
);
```

## 회원정보조회
```sql
SET @encryption_key = SHA2('MySecretKey', 256);

SELECT 
    id,
    username,
    email,
    AES_DECRYPT(full_name, @encryption_key) AS full_name,
    created_at
FROM members
WHERE username = 'newuser';
```

## 회원정보수정
```sql
SET @encryption_key = SHA2('MySecretKey', 256);

UPDATE members
SET 
    email = 'newemail@example.com',
    full_name = AES_ENCRYPT('Jane Doe', @encryption_key)
WHERE username = 'newuser';
```

## 로그인
```sql
SELECT id 
FROM members 
WHERE username = 'newuser' 
AND password = SHA2('user_password', 512);
```

## 비밀번호 변경
```sql
UPDATE members
SET password = SHA2('new_password', 512)
WHERE username = 'newuser'
AND password = SHA2('old_password', 512);
```