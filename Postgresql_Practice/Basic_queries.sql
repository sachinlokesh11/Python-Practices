DROP TABLE IF EXISTS p2.links;

CREATE TABLE p2.links (
	id SERIAL PRIMARY KEY,
	url VARCHAR(255) NOT NULL,
	name VARCHAR(255) NOT NULL,
	description VARCHAR (255),
        last_update DATE
);

-- Will return whole thing after execution
INSERT INTO p2.links (url, name)
VALUES('https://www.postgresqltutorial.com','PostgreSQL Tutorial')Returning *;

-- Adding single quote value
INSERT INTO p2.links (url, name)
VALUES('http://www.oreilly.com','O''Reilly Media')Returning *;

-- Inserting a date value
INSERT INTO p2.links (url, name, last_update)
VALUES('https://www.google.com','Google','2013-06-01');

INSERT INTO p2.links (url, name)
VALUES('http://www.postgresql.org','PostgreSQL') 
RETURNING id;

SELECT * FROM p2.links

-- update value in column of a table
UPDATE p2.links SET description = 'Queries ' WHERE id IN(3, 4);
UPDATE p2.links SET description = 'Searcher ' WHERE id=3;

-- delete rows from table
DELETE FROM p2.links WHERE id=4;




