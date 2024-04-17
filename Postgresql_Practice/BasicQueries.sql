create table p1.students(
student_id serial PRIMARY KEY,
first_name varchar(50) NOT NULL,
last_name varchar(50) NOT NULL,
house_number integer,
phone varchar(255) NOT NULL Unique,
email varchar(50) Unique,
year integer
);

Select * from p1.students;

-- changing column name
Alter table p1.students 
rename column year to pass_year;

-- Double string will not work for varchar
insert into p1.students(first_name, last_name, house_number,phone, email, pass_year)
Values
('Shubham', 'Singh', 56756, '6757473745', 'shubham@gmail.com', 2022),
('Imran', 'Khan', 67656, '7858334857', 'imran@gmail.com', 2021),
('Abhijeet', 'Tripathi', 45654, '8574734567', 'abhi@gmail.com', 2021),
('Tejas', 'Sharma', 67665, '8594939456', 'tejas@gmail.com', 2023),
('Viney', 'Khaneja',67543, '7485858567', 'viney@gmail.com', 2022);

SELECT first_name FROM p1.students;

SELECT first_name, last_name, email FROM p1.students

SELECT  first_name || ' ' || last_name, email FROM p1.students;

SELECT  first_name || ' ' || last_name AS Full_name FROM p1.students;

SELECT first_name, last_name AS surname FROM p1.students;

-- If a column alias contains one or more spaces, you need to surround it with double quotes like this:
SELECT  first_name || ' ' || last_name AS "Full name" FROM p1.students;

SELECT first_name, last_name FROM p1.students ORDER BY first_name Desc;

SELECT 	first_name, LENGTH(first_name) len FROM p1.students ORDER BY len DESC;

insert into p1.students(first_name, last_name, house_number,phone, email, pass_year)
Values
('Shubham', 'Sharma', 56356, '6898478945', 'ss@gmail.com', 2019),
('Imran', 'moh', 67256, '7348334857', 'im@gmail.com', 2018)

-- delete duplicate columns
SELECT DISTINCT first_name FROM	p1.students;

-- delete duplicate rows
SELECT DISTINCT first_name, last_name FROM	p1.students;

-- first remove duplicate first_name 
SELECT DISTINCT on(first_name) first_name, last_name FROM	p1.students;


SELECT first_name, last_name FROM p1.students where first_name = 'Shubham';
                          or
SELECT first_name, last_name FROM p1.students where first_name Like 'Shubham';


SELECT first_name, last_name FROM p1.students where first_name = 'Shubham' and last_name = 'Singh';

SELECT first_name, last_name FROM p1.students where first_name = 'Shubham' or last_name = 'Sharma';

SELECT first_name, last_name FROM p1.students where first_name in ('Shubham', 'Imran', 'Rahul');

-- give rows whose last name starts with S
SELECT first_name, last_name FROM p1.students where last_name Like 'S%';

-- give rows whose last name starts with S and ends with a
SELECT first_name, last_name FROM p1.students where last_name Like 'S%a';

SELECT first_name, length(last_name) name_length FROM p1.students where last_name Like 'S%' and length(last_name) between 4 and 9 order by name_length;

-- using not equal to(<>) operator
SELECT first_name, last_name FROM p1.students where first_name Like 'Shubh%' and last_name <> 'Singh';
                           or
SELECT first_name, last_name FROM p1.students where first_name Like 'Shubh%' and last_name != 'Singh';

-- will give only top 3 rows out of total
SELECT student_id, first_name, last_name, house_number, phone from p1.students limit 3;
                          or
SELECT student_id, first_name, last_name, house_number, phone from p1.students fetch first 3 row only;


-- will give top 3 rows after deleting 2 top rows out of total
SELECT student_id, first_name, last_name, house_number, phone from p1.students limit 3 offset 2;
                          or
SELECT student_id, first_name, last_name, house_number, phone from p1.students offset 2 rows fetch first 3 row only ;

-- both will include
SELECT * from p1.students where pass_year between 2019 and 2021;

-- both will exclude
SELECT * from p1.students where pass_year NOT between 2019 and 2021;

-- Ilike is case insensitive means will give values for firstname start with shubh, Shubh, SHubh, SHUBH
SELECT first_name, last_name FROM p1.students where first_name ILike 'shubh%';

-- dont use last_name = NULL
SELECT * FROM p1.students WHERE last_name IS NULL;
SELECT * FROM p1.students WHERE last_name IS NOT NULL;
