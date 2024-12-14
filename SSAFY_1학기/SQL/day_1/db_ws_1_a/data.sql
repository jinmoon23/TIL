-- Active: 1728528815469@@127.0.0.1@3306
CREATE TABLE songs (
    id INTEGER,
    title TEXT,
    artists TEXT,
    album TEXT,
    genre TEXT,
    duration INTEGER
);

INSERT INTO songs (
  id, title, artists, album, genre, duration
)
VALUES (
	1, 'Song 1', 'Artists 1', 'Album 1', 'Pop', 200
);

INSERT INTO songs (
  id, title, artists, album, genre, duration
)
VALUES (
	2, 'Song 2', 'Artists 2', 'Album 2', 'Rock', 300
);

INSERT INTO songs (
  id, title, artists, album, genre, duration
)
VALUES (
	3, 'Song 3', 'Artists 3', 'Album 3', 'Hip Hop', 150
);


INSERT INTO songs (
  id, title, artists, album, genre, duration
)
VALUES (
	4, 'Song 4', 'Artists 4', 'Album 4', 'Electronic', 180
);

INSERT INTO songs (
  id, title, artists, album, genre, duration
)
VALUES (
	5, 'Song 5', 'Artists 5', 'Album 5', 'R&B', 230
);

UPDATE songs
SET title = 'changed Song 1'
WHERE
	id = 1