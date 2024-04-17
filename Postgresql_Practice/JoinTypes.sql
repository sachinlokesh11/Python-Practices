CREATE TABLE p1.Company(
CompanyID INT PRIMARY KEY ,
CompanyName VARCHAR(30)
);
SELECT * FROM p1.Company
INSERT INTO p1.Company VALUES(1,'HCL'),(2,'INFOSYS');
INSERT INTO p1.Company VALUES(3,'TCS');

CREATE TABLE p1.Employee(
EmployeeID Serial PRIMARY KEY,
EmployeeName VARCHAR(30) NOT NULL,
Gender CHAR(1) NOT NULL,
PhoneNo BIGINT
);

SELECT * FROM p1.Employee

INSERT INTO p1.Employee (EmployeeName, Gender, PhoneNo) VALUES
('Shubham','M',9200590149),
('Rahul','M',7015906297),
('Abhishek','M',8950595579),
('Rashmika','F',7206504149),
('Naina','F',7306594149),
('Ajay','M',7206594109),
('Komal','F',9466365917);

-- using inner join 
SELECT * FROM p1.Employee INNER JOIN p1.students on employeename = first_name;

--using left join
SELECT * FROM p1.Employee LEFT JOIN p1.students on employeename = first_name;

--using Right join
SELECT * FROM p1.Employee RIGHT JOIN p1.students on employeename = first_name;

-- using full join
SELECT * FROM p1.Employee FULL JOIN p1.students on employeename = first_name;

-- all except common
SELECT * FROM p1.Employee FULL JOIN p1.students on employeename = first_name
WHERE p1.Employee.employeeid IS NULL OR  p1.students.student_id IS NULL;
                        or
-- using table alias
SELECT * FROM p1.Employee e FULL JOIN p1.students s on employeename = first_name
WHERE e.employeeid IS NULL OR  s.student_id IS NULL;

-- multiple tables
SELECT * FROM p1.Employee e FULL JOIN p1.students s on employeename = first_name
INNER JOIN p1.company c on c.companyid = e.employeeid

-- cross join
SELECT employeeid, companyid, employeename FROM p1.employee CROSS JOIN p1.company;
