CREATE TABLE p2.movies(
name VARCHAR(100) NOT NULL,
Review INT
);

INSERT INTO p2.movies(name, Review)Values('Pushpa', 4),('Avatar', 5),('Ratsasan', 4);

SELECT * FROM P2.movies

CREATE TABLE p2.top_movies(
name VARCHAR(100) NOT NULL,
Review INT
);

INSERT INTO p2.top_movies(name, Review)Values('Pushpa', 4),('Tummbad', 5),('Black', 4);

SELECT * FROM p2.top_movies;

-- Fetch all rows except duplicates
SELECT * FROM p2.movies UNION SELECT * FROM p2.top_movies;

-- Fetch all rows including duplicates
SELECT * FROM p2.movies UNION ALL SELECT * FROM p2.top_movies;

-- Fetch all rows common to both tables 
SELECT * FROM p2.movies INTERSECT SELECT * FROM p2.top_movies;

-- Fetch all rows from table movies which are not in table top_movies
SELECT * FROM p2.movies EXCEPT SELECT * FROM p2.top_movies;

-- subquery
SELECT * FROM p2.movies WHERE Review IN (SELECT review FROM p2.top_movies);
SELECT * FROM p2.movies WHERE Review = (SELECT review FROM p2.top_movies WHERE Review>4);

--ANY 
SELECT * FROM p2.movies WHERE Review = ANY(SELECT Review from p2.top_movies where Review=4);
                      or
SELECT * FROM p2.movies WHERE Review IN(SELECT Review from p2.top_movies where Review=4);

SELECT * FROM p2.movies WHERE Review > ANY(SELECT Review from p2.top_movies where Review=4);


