CREATE TABLE zoo (
    name TEXT,
    eat TEXT,
    weight INT,
    height INT,
    age INT
);

INSERT INTO zoo (
    name, eat, weight, height, age
)
VALUES
('Lion','Meat',200, 300, 10),
('Rabbit','Mix',20, 30, 2),
('Turttle','Fish',15, 10, 150),
('Fish','Flankton',2, 1, 1);

SELECT
    *
FROM
    zoo
    