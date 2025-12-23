**ASSIGNMENT NO : 2**



**1) Create the table Member, Books and Issue without any constraints as**

**mentioned in the schema description above.**



FOR MEMBER

mysql> create table Member

&nbsp;   -> (Member\_id int, Member\_name varchar(30), Member\_address varchar(50

&nbsp;   -> ), Acc\_Open\_Date date, Membership\_type varchar(20), Fees\_paid int, Max\_Book\_Allowed int, Penalty\_Amount decimal(7,2));

Query OK, 0 rows affected (0.14 sec)





FOR BOOKS

mysql> create table Books

&nbsp;   -> (Book\_No int, Book\_Name Varchar(30), Author\_Name varchar(30), Cost int, Category char(10));

Query OK, 0 rows affected (0.20 sec)



FOR ISSUE

mysql> create table issue

&nbsp;   -> (Book\_No int, Member\_id int, issue\_date date,

&nbsp;   -> Return\_date date);

Query OK, 0 rows affected (0.04 sec)





**2) View the structure of the tables.**





mysql> desc Member;

+------------------+--------------+------+-----+---------+-------+

| Field            | Type         | Null | Key | Default | Extra |

+------------------+--------------+------+-----+---------+-------+

| Member\_id        | int          | YES  |     | NULL    |       |

| Member\_name      | varchar(30)  | YES  |     | NULL    |       |

| Member\_address   | varchar(50)  | YES  |     | NULL    |       |

| Acc\_Open\_Date    | date         | YES  |     | NULL    |       |

| Membership\_type  | varchar(20)  | YES  |     | NULL    |       |

| Fees\_paid        | int          | YES  |     | NULL    |       |

| Max\_Book\_Allowed | int          | YES  |     | NULL    |       |

| Penalty\_Amount   | decimal(7,2) | YES  |     | NULL    |       |

+------------------+--------------+------+-----+---------+-------+







mysql> desc Books;

+-------------+-------------+------+-----+---------+-------+

| Field       | Type        | Null | Key | Default | Extra |

+-------------+-------------+------+-----+---------+-------+

| Book\_No     | int         | YES  |     | NULL    |       |

| Book\_Name   | varchar(30) | YES  |     | NULL    |       |

| Author\_Name | varchar(30) | YES  |     | NULL    |       |

| Cost        | int         | YES  |     | NULL    |       |

| Category    | char(10)    | YES  |     | NULL    |       |

+-------------+-------------+------+-----+---------+-------+





mysql> desc issue;

+-------------+------+------+-----+---------+-------+

| Field       | Type | Null | Key | Default | Extra |

+-------------+------+------+-----+---------+-------+

| Book\_No     | int  | YES  |     | NULL    |       |

| Member\_id   | int  | YES  |     | NULL    |       |

| issue\_date  | date | YES  |     | NULL    |       |

| Return\_date | date | YES  |     | NULL    |       |

+-------------+------+------+-----+---------+-------+

4 rows in set (0.01 sec)





**3) Drop the Member table**





mysql> drop table Member;

Query OK, 0 rows affected (0.07 sec)



mysql> desc Member

&nbsp;   -> ;

ERROR 1146 (42S02): Table 'fbs.member' doesn't exist

mysql>





**4) Create the table Member again as per the schema description with the**

**following constraints.**



a. Member\_Id – Primary Key





mysql> create table Member

&nbsp;   -> (Member\_id int primary key, Member\_name varchar(30), Member\_address varchar(50), Acc\_open\_Date date, Membership\_type varchar(20), Fees\_paid int,

&nbsp;   -> Max\_Books\_Allowed int, Penalty\_Amount decimal(7,2));

Query OK, 0 rows affected (0.07 sec)







mysql> desc Member;

+-------------------+--------------+------+-----+---------+-------+

| Field             | Type         | Null | Key | Default | Extra |

+-------------------+--------------+------+-----+---------+-------+

| Member\_id         | int          | NO   | PRI | NULL    |       |

| Member\_name       | varchar(30)  | YES  |     | NULL    |       |

| Member\_address    | varchar(50)  | YES  |     | NULL    |       |

| Acc\_open\_Date     | date         | YES  |     | NULL    |       |

| Membership\_type   | varchar(20)  | YES  |     | NULL    |       |

| Fees\_paid         | int          | YES  |     | NULL    |       |

| Max\_Books\_Allowed | int          | YES  |     | NULL    |       |

| Penalty\_Amount    | decimal(7,2) | YES  |     | NULL    |       |

+-------------------+--------------+------+-----+---------+-------+





b. Membership\_type - ‘Lifetime’,’ Annual’, ‘Half Yearly’,’ Quarterly’



mysql> alter table Member

&nbsp;   -> modify column Membership\_type varchar(20)

&nbsp;   -> check (Membership\_type in("lifetime", "Annual", "Half Yearly", "Quarterly"));

Query OK, 0 rows affected (0.11 sec)

Records: 0  Duplicates: 0  Warnings: 0





mysql> show create table Member;

| Table  | Create Table                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |

| Member | CREATE TABLE `member` (

&nbsp; `Member\_id` int NOT NULL,

&nbsp; `Member\_name` varchar(30) DEFAULT NULL,

&nbsp; `Member\_address` varchar(50) DEFAULT NULL,

&nbsp; `Acc\_open\_Date` date DEFAULT NULL,

&nbsp; `Membership\_type` varchar(20) DEFAULT NULL,

&nbsp; `Fees\_paid` int DEFAULT NULL,

&nbsp; `Max\_Books\_Allowed` int DEFAULT NULL,

&nbsp; `Penalty\_Amount` decimal(7,2) DEFAULT NULL,

&nbsp; PRIMARY KEY (`Member\_id`),

&nbsp; CONSTRAINT `member\_chk\_1` CHECK ((`Membership\_type` in (\_utf8mb4'lifetime',\_utf8mb4'Annual',\_utf8mb4'Half Yearly',\_utf8mb4'Quarterly')))

) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4\_0900\_ai\_ci |

1 row in set (0.01 sec)



mysql>





**5) Modify the table Member increase the width of the member name to 30**

**characters.**





mysql> alter table Member

&nbsp;   -> modify column Member\_name varchar(30);

Query OK, 0 rows affected (0.02 sec)

Records: 0  Duplicates: 0  Warnings: 0





**6) Add a column named as Reference of Char(30) to Issue table.**



mysql> alter table issue

&nbsp;   -> add column refernces char(30);

Query OK, 0 rows affected (0.17 sec)

Records: 0  Duplicates: 0  Warnings: 0



mysql> desc issue;

+-------------+----------+------+-----+---------+-------+

| Field       | Type     | Null | Key | Default | Extra |

+-------------+----------+------+-----+---------+-------+

| Book\_No     | int      | YES  |     | NULL    |       |

| Member\_id   | int      | YES  |     | NULL    |       |

| issue\_date  | date     | YES  |     | NULL    |       |

| Return\_date | date     | YES  |     | NULL    |       |

| refernces   | char(30) | YES  |     | NULL    |       |

+-------------+----------+------+-----+---------+-------+

5 rows in set (0.05 sec)





**7) Delete/Drop the column Reference from Issue.**





mysql> alter table issue

&nbsp;   -> drop column refernces;

Query OK, 0 rows affected (0.09 sec)

Records: 0  Duplicates: 0  Warnings: 0



mysql> desc issue;

+-------------+------+------+-----+---------+-------+

| Field       | Type | Null | Key | Default | Extra |

+-------------+------+------+-----+---------+-------+

| Book\_No     | int  | YES  |     | NULL    |       |

| Member\_id   | int  | YES  |     | NULL    |       |

| issue\_date  | date | YES  |     | NULL    |       |

| Return\_date | date | YES  |     | NULL    |       |

+-------------+------+------+-----+---------+-------+

4 rows in set (0.01 sec)





**7) Delete/Drop the column Reference from Issue.**



mysql> rename table issue to Lib\_Issue;

Query OK, 0 rows affected (0.05 sec)



mysql> desc Lib\_Issue;

+-------------+------+------+-----+---------+-------+

| Field       | Type | Null | Key | Default | Extra |

+-------------+------+------+-----+---------+-------+

| Book\_No     | int  | YES  |     | NULL    |       |

| Member\_id   | int  | YES  |     | NULL    |       |

| issue\_date  | date | YES  |     | NULL    |       |

| Return\_date | date | YES  |     | NULL    |       |

+-------------+------+------+-----+---------+-------+

4 rows in set (0.01 sec)



**8)rename tohe table issue to lib\_issue**



mysql> rename table Issue to Lib\\\_Issue;

Query OK, 0 rows affected (0.02 sec)





mysql> desc Lib\\\_Issue;

+--------------+------+------+-----+---------+-------+

| Field        | Type | Null | Key | Default | Extra |

+--------------+------+------+-----+---------+-------+

| Lib\\\_Issue\\\_Id | int  | YES  |     | NULL    |       |

| Book\\\_No      | int  | YES  |     | NULL    |       |

| Member\\\_Id    | int  | YES  |     | NULL    |       |

| Issue\\\_Date   | date | YES  |     | NULL    |       |

| Return\\\_date  | int  | YES  |     | NULL    |       |

+--------------+------+------+-----+---------+-------+



5 rows in set (0.00 sec)



**9) Insert following data in table Member**





mysql> insert into Member

&nbsp;   -> (Member\_id, Member\_name, Member\_address, Acc\_open\_Date, Membership\_type, Fees\_paid, Max\_Books\_Allowed, Penalty\_Amount)values(1,"Richa Sharma","Pune","2010-12-05","Lifetime",25000,5,50);

Query OK, 1 row affected (0.02 sec)



mysql> table Member;

+-----------+--------------+----------------+---------------+-----------------+-----------+-------------------+----------------+

| Member\_id | Member\_name  | Member\_address | Acc\_open\_Date | Membership\_type | Fees\_paid | Max\_Books\_Allowed | Penalty\_Amount |

+-----------+--------------+----------------+---------------+-----------------+-----------+-------------------+----------------+

|         1 | Richa Sharma | Pune           | 2010-12-05    | Lifetime        |     25000 |                 5 |          50.00 |

+-----------+--------------+----------------+---------------+-----------------+-----------+-------------------+----------------+

1 row in set (0.01 sec)



mysql> insert into Member

&nbsp;   -> (Member\_id, Member\_name, Member\_address, Acc\_open\_Date, Membership\_type, Fees\_paid, Max\_Books\_Allowed)values(2,"Garima Sen","Pune","2025-12-19","Annual",1000,3);

Query OK, 1 row affected (0.07 sec)



mysql> table Member;

+-----------+--------------+----------------+---------------+-----------------+-----------+-------------------+----------------+

| Member\_id | Member\_name  | Member\_address | Acc\_open\_Date | Membership\_type | Fees\_paid | Max\_Books\_Allowed | Penalty\_Amount |

+-----------+--------------+----------------+---------------+-----------------+-----------+-------------------+----------------+

|         1 | Richa Sharma | Pune           | 2010-12-05    | Lifetime        |     25000 |                 5 |          50.00 |

|         2 | Garima Sen   | Pune           | 2025-12-19    | Annual          |      1000 |                 3 |           NULL |

+-----------+--------------+----------------+---------------+-----------------+-----------+-------------------+----------------+

2 rows in set (0.01 sec)



mysql>





**10) Insert at least 5 records with suitable data.**







mysql> insert into Member

&nbsp;   -> (Member\_id, Member\_name, Member\_address, Acc\_open\_Date, Membership\_type, Fees\_paid, Max\_Books\_Allowed, Penalty\_Amount)values(3,"Pranali Jadhav","Satara","2015-02-21", "Half Yearly",2500,4,70);

Query OK, 1 row affected (0.01 sec)



mysql> insert into Member

&nbsp;   -> (Member\_id, Member\_name, Member\_address, Acc\_open\_Date, Membership\_type, Fees\_paid, Max\_Books\_Allowed, Penalty\_Amount)values(4,"Ankita Jadhav","Mumbai","2017-02-23", "Quarterly",2500,4,70);

Query OK, 1 row affected (0.01 sec)



mysql> insert into Member

&nbsp;   -> (Member\_id, Member\_name, Member\_address, Acc\_open\_Date, Membership\_type, Fees\_paid, Max\_Books\_Allowed, Penalty\_Amount)values(5,"Sayali lad","Dhule","2022-04-20", "Annual",3000,9,60);

Query OK, 1 row affected (0.01 sec)



mysql> insert into Member

&nbsp;   -> (Member\_id, Member\_name, Member\_address, Acc\_open\_Date, Membership\_type, Fees\_paid, Max\_Books\_Allowed, Penalty\_Amount)values(6,"Sahil Jamdade","Kolhapur","2024-07-21", "Half Yearly",4500,6,87);

Query OK, 1 row affected (0.01 sec)



mysql> insert into Member

&nbsp;   -> (Member\_id, Member\_name, Member\_address, Acc\_open\_Date, Membership\_type, Fees\_paid, Max\_Books\_Allowed, Penalty\_Amount)values(7,"Sumit Jadhav","Chattisgadh","2023-07-25", "Quarterly",3300,7,67);

Query OK, 1 row affected (0.01 sec)



mysql> table Member;

+-----------+----------------+----------------+---------------+-----------------+-----------+-------------------+----------------+

| Member\_id | Member\_name    | Member\_address | Acc\_open\_Date | Membership\_type | Fees\_paid | Max\_Books\_Allowed | Penalty\_Amount |

+-----------+----------------+----------------+---------------+-----------------+-----------+-------------------+----------------+

|         1 | Richa Sharma   | Pune           | 2010-12-05    | Lifetime        |     25000 |                 5 |          50.00 |

|         2 | Garima Sen     | Pune           | 2025-12-19    | Annual          |      1000 |                 3 |           NULL |

|         3 | Pranali Jadhav | Satara         | 2015-02-21    | Half Yearly     |      2500 |                 4 |          70.00 |

|         4 | Ankita Jadhav  | Mumbai         | 2017-02-23    | Quarterly       |      2500 |                 4 |          70.00 |

|         5 | Sayali lad     | Dhule          | 2022-04-20    | Annual          |      3000 |                 9 |          60.00 |

|         6 | Sahil Jamdade  | Kolhapur       | 2024-07-21    | Half Yearly     |      4500 |                 6 |          87.00 |

|         7 | Sumit Jadhav   | Chattisgadh    | 2023-07-25    | Quarterly       |      3300 |                 7 |          67.00 |

+-----------+----------------+----------------+---------------+-----------------+-----------+-------------------+----------------+

7 rows in set (0.00 sec)



mysql>





**11) Modify the column Member\_name. Decrease the width of the member**

**name to 20 characters. (If it does not allow state the reason for that)**



mysql> alter table Member

&nbsp;   -> modify column Member\_name varchar(20);

Query OK, 7 rows affected (0.20 sec)

Records: 7  Duplicates: 0  Warnings: 0



mysql>



myql> insert into Member values

**->** 

**12)Try to insert a record with Max Books\_Allowed 110, Observe error that comes.**



mysql> insert into member values

-> (8, 'aseet tayade', 'beed', curdate(), 'annual', 1200,110,0);

ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '

insert into member values(8, 'aseet tayade', 'beed', curdate(), 'annual', 1200, 110,0' at line 2







**13) Generate another table named Member101 using a Create command**

**along with a simple SQL query on member table.**







mysql> create table Member101(select\*from Member);

Query OK, 7 rows affected (0.06 sec)

Records: 7  Duplicates: 0  Warnings: 0





**14) Add the constraints on columns max\_books\_allowed and penalty\_amt**

**as follows**

a. max\_books\_allowed < 100





mysql> alter table Member

&nbsp;   -> modify column max\_books\_allowed int check(max\_books\_allowed < 100);

Query OK, 7 rows affected (0.34 sec)

Records: 7  Duplicates: 0  Warnings: 0



b. penalty\_amt maximum 1000

Also give names to the constraints.





mysql> alter table Member

&nbsp;   -> modify column Penalty\_Amount decimal(7,2) check(Penalty\_Amount <= 1000);

Query OK, 7 rows affected (0.35 sec)

Records: 7  Duplicates: 0  Warnings: 0



mysql>





mysql> show create table Member;

| Table  | Create Table                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |

| Member | CREATE TABLE `member` (

&nbsp; `Member\_id` int NOT NULL,

&nbsp; `Member\_name` varchar(20) DEFAULT NULL,

&nbsp; `Member\_address` varchar(50) DEFAULT NULL,

&nbsp; `Acc\_open\_Date` date DEFAULT NULL,

&nbsp; `Membership\_type` varchar(20) DEFAULT NULL,

&nbsp; `Fees\_paid` int DEFAULT NULL,

&nbsp; `max\_books\_allowed` int DEFAULT NULL,

&nbsp; `Penalty\_Amount` decimal(7,2) DEFAULT NULL,

&nbsp; PRIMARY KEY (`Member\_id`),

&nbsp; CONSTRAINT `member\_chk\_1` CHECK ((`Membership\_type` in (\_utf8mb4'lifetime',\_utf8mb4'Annual',\_utf8mb4'Half Yearly',\_utf8mb4'Quarterly'))),

&nbsp; CONSTRAINT `member\_chk\_2` CHECK ((`max\_books\_allowed` < 100)),

&nbsp; CONSTRAINT `member\_chk\_3` CHECK ((`Penalty\_Amount` <= 1000))

) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4\_0900\_ai\_ci |

1 row in set (0.01 sec)



mysql>



**15) Drop the table books.**



mysql> drop table Books;

Query OK, 0 rows affected (0.04 sec)



mysql> desc Books;

ERROR 1146 (42S02): Table 'fbs.books' doesn't exist

mysql>





**16) Create table Books again as per the schema description with the**

**following constraints.**

**a. Book\_No – Primary Key**

**b. Book\_Name – Not Null**

**c. Category – System, Fiction, Database, RDBMS, Others.**





mysql> create table Books

&nbsp;   -> (Book\_No int primary key, Book\_Name Varchar(30) not null, Author\_Name varchar(30), Cost int, Category char(10));

Query OK, 0 rows affected (0.05 sec)



mysql> desc Books;

+-------------+-------------+------+-----+---------+-------+

| Field       | Type        | Null | Key | Default | Extra |

+-------------+-------------+------+-----+---------+-------+

| Book\_No     | int         | NO   | PRI | NULL    |       |

| Book\_Name   | varchar(30) | NO   |     | NULL    |       |

| Author\_Name | varchar(30) | YES  |     | NULL    |       |

| Cost        | int         | YES  |     | NULL    |       |

| Category    | char(10)    | YES  |     | NULL    |       |

+-------------+-------------+------+-----+---------+-------+

5 rows in set (0.02 sec)





mysql> alter table Books

&nbsp;   -> modify column Category char(10)

&nbsp;   -> check(Category in("system","fiction","databse", "RDBMS","Others"));

Query OK, 0 rows affected (0.09 sec)

Records: 0  Duplicates: 0  Warnings: 0







mysql> show create table Books;

| Table | Create Table                                                                                                                                                                                                                                                                                                                                                                                                                           |

| Books | CREATE TABLE `books` (

&nbsp; `Book\_No` int NOT NULL,

&nbsp; `Book\_Name` varchar(30) NOT NULL,

&nbsp; `Author\_Name` varchar(30) DEFAULT NULL,

&nbsp; `Cost` int DEFAULT NULL,

&nbsp; `Category` char(10) DEFAULT NULL,

&nbsp; PRIMARY KEY (`Book\_No`),

&nbsp; CONSTRAINT `books\_chk\_1` CHECK ((`Category` in (\_utf8mb4'system',\_utf8mb4'fiction',\_utf8mb4'databse',\_utf8mb4'RDBMS',\_utf8mb4'Others')))

) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4\_0900\_ai\_ci |

-1 row in set (0.00 sec)



mysql>



**17) Insert data in Book table as follows:**





mysql> insert into Books

&nbsp;   -> (Book\_No,Book\_Name,Author\_Name,Cost,Category)values

&nbsp;   -> (101,"Let us c","Dennis Ritchie",450,"system"),

&nbsp;   -> (102,"Oracle-Complete Ref","Loni",250,"databse"),

&nbsp;   -> (103,"Mastering SQL","Loni",250,"databse"),

&nbsp;   -> (104,"PL SQL-Ref","Scott Urman",750,"databse");

Query OK, 4 rows affected (0.02 sec)

Records: 4  Duplicates: 0  Warnings: 0





**18) Insert more records in Book table.**



mysql> table Books;

+---------+---------------------+----------------+------+----------+

| Book\_No | Book\_Name           | Author\_Name    | Cost | Category |

+---------+---------------------+----------------+------+----------+

|     101 | Let us c            | Dennis Ritchie |  450 | system   |

|     102 | Oracle-Complete Ref | Loni           |  250 | databse  |

|     103 | Mastering SQL       | Loni           |  250 | databse  |

|     104 | PL SQL-Ref          | Scott Urman    |  750 | databse  |

+---------+---------------------+----------------+------+----------+

4 rows in set (0.01 sec)



mysql>



mysql> insert into books

&nbsp;   -> (Book\_No,Book\_Name,Author\_Name,Cost,Category)values(105,"Goshti Mansanchya","Sudha Murthy",280,"Others");

Query OK, 1 row affected (0.02 sec)



mysql> insert into books

&nbsp;   -> (Book\_No,Book\_Name,Author\_Name,Cost,Category)values(106,"Wings of fire","Dr. APJ Abdul kalam",180,"Others");

Query OK, 1 row affected (0.01 sec)



mysql> insert into books

&nbsp;   -> (Book\_No,Book\_Name,Author\_Name,Cost,Category)values(107,"Operating system Concepts","WILEY",400,"system");

Query OK, 1 row affected (0.06 sec)





**19) View the data in the tables using simple SQL query.** 





mysql> table Books;

+---------+---------------------------+---------------------+------+----------+

| Book\_No | Book\_Name                 | Author\_Name         | Cost | Category |

+---------+---------------------------+---------------------+------+----------+

|     101 | Let us c                  | Dennis Ritchie      |  450 | system   |

|     102 | Oracle-Complete Ref       | Loni                |  250 | databse  |

|     103 | Mastering SQL             | Loni                |  250 | databse  |

|     104 | PL SQL-Ref                | Scott Urman         |  750 | databse  |

|     105 | Goshti Mansanchya         | Sudha Murthy        |  280 | Others   |

|     106 | Wings of fire             | Dr. APJ Abdul kalam |  180 | Others   |

|     107 | Operating system Concepts | WILEY               |  400 | system   |

+---------+---------------------------+---------------------+------+----------+

7 rows in set (0.00 sec)



mysql>





**20) Insert into Book following data.**



105, National Geographic, Adis Scott, 1000, Science



mysql> alter table Books

&nbsp;   -> drop constraint books\_chk\_1;

Query OK, 0 rows affected (0.12 sec)

Records: 0  Duplicates: 0  Warnings: 0





mysql> insert into Books

&nbsp;   -> (Book\_No,Book\_Name,Author\_Name,Cost,Category)values(105,"National geograhic","Adis scott",1000,"science");

Query OK, 1 row affected (0.02 sec)



mysql> table Books;

+---------+---------------------------+---------------------+------+----------+

| Book\_No | Book\_Name                 | Author\_Name         | Cost | Category |

+---------+---------------------------+---------------------+------+----------+

|     101 | Let us c                  | Dennis Ritchie      |  450 | system   |

|     102 | Oracle-Complete Ref       | Loni                |  250 | databse  |

|     103 | Mastering SQL             | Loni                |  250 | databse  |

|     104 | PL SQL-Ref                | Scott Urman         |  750 | databse  |

|     105 | National geograhic        | Adis scott          | 1000 | science  |

|     106 | Wings of fire             | Dr. APJ Abdul kalam |  180 | Others   |

|     107 | Operating system Concepts | WILEY               |  400 | system   |

+---------+---------------------------+---------------------+------+----------+

7 rows in set (0.01 sec)



mysql>









**21) Rename the table Lib\_Issue to Issue.**





mysql> rename table Lib\_Issue to issue;

Query OK, 0 rows affected (0.06 sec)



**22) Drop table Issue.**





mysql> drop table issue;

Query OK, 0 rows affected (0.09 sec)



mysql> table issue;

ERROR 1146 (42S02): Table 'fbs.issue' doesn't exist

mysql>



**23) As per the given structure Create table Issue again with following**

**constraints.**



 Lib\_Issue\_Id-Primary key

 Book\_No- foreign key

 Member\_id - foreign key

 Issue\_date

 Return\_date



mysql> create table Lib\_books

&nbsp;   -> (Lib\_Issue\_id int primary key, Book\_No int, Member\_id int, issue\_date date, return\_date date);

Query OK, 0 rows affected (0.10 sec)



mysql> alter table Lib\_Books

&nbsp;   -> add foreign key(Book\_No)

&nbsp;   -> references Books(Book\_No);

Query OK, 0 rows affected (0.15 sec)

Records: 0  Duplicates: 0  Warnings: 0





mysql> alter table Lib\_Books

&nbsp;   -> add foreign key(Member\_id)

&nbsp;   -> references Member(Member\_id);

Query OK, 0 rows affected (0.16 sec)

Records: 0  Duplicates: 0  Warnings: 0







mysql> desc Lib\_Books;

+--------------+------+------+-----+---------+-------+

| Field        | Type | Null | Key | Default | Extra |

+--------------+------+------+-----+---------+-------+

| Lib\_Issue\_id | int  | NO   | PRI | NULL    |       |

| Book\_No      | int  | YES  | MUL | NULL    |       |

| Member\_id    | int  | YES  | MUL | NULL    |       |

| issue\_date   | date | YES  |     | NULL    |       |

| return\_date  | date | YES  |     | NULL    |       |

+--------------+------+------+-----+---------+-------+

5 rows in set (0.01 sec)



mysql>



**24) Insert following data into Issue table.**





mysql> insert into Lib\_Books

&nbsp;   -> (Lib\_Issue\_id, Book\_No, Member\_id, Issue\_date)values

&nbsp;   -> (7001,101,1,"2006-12-15"),

&nbsp;   -> (7002,102,2,"2006-12-15"),

&nbsp;   -> (7003,104,1,"2006-01-06"),

&nbsp;   -> (7004,101,1,"2006-07-04"),

&nbsp;   -> (7005,104,2,"2006-11-15"),

&nbsp;   -> (7006,101,3,"2006-02-18");

Query OK, 5 rows affected (0.08 sec)

Records: 5  Duplicates: 0  Warnings: 0



mysql> table Lib\_Books;

+--------------+---------+-----------+------------+-------------+

| Lib\_Issue\_id | Book\_No | Member\_id | issue\_date | return\_date |

+--------------+---------+-----------+------------+-------------+

|         7001 |     101 |         1 | 2006-12-15 | NULL        |

|         7002 |     102 |         2 | 2006-12-15 | NULL        |

|         7003 |     104 |         1 | 2006-01-06 | NULL        |

|         7004 |     101 |         1 | 2006-07-04 | NULL        |

|         7005 |     104 |         2 | 2006-11-15 | NULL        |

|         7006 |     101 |         3 | 2006-02-18 | NULL        |

+--------------+---------+-----------+------------+-------------+

6 rows in set (0.01 sec)



mysql>





**25) Remove the constraints on Issue table**





mysql> alter table Lib\_Books

&nbsp;   -> drop primary key;

Query OK, 6 rows affected (0.18 sec)

Records: 6  Duplicates: 0  Warnings: 0





mysql> alter table Lib\_Books

&nbsp;   -> drop constraint lib\_books\_ibfk\_1;

Query OK, 0 rows affected (0.04 sec)

Records: 0  Duplicates: 0  Warnings: 0



mysql> alter table Lib\_Books

&nbsp;   -> drop constraint lib\_books\_ibfk\_2;

Query OK, 0 rows affected (0.04 sec)

Records: 0  Duplicates: 0  Warnings: 0





mysql> desc Lib\_Books;

+--------------+------+------+-----+---------+-------+

| Field        | Type | Null | Key | Default | Extra |

+--------------+------+------+-----+---------+-------+

| Lib\_Issue\_id | int  | NO   |     | NULL    |       |

| Book\_No      | int  | YES  | MUL | NULL    |       |

| Member\_id    | int  | YES  | MUL | NULL    |       |

| issue\_date   | date | YES  |     | NULL    |       |

| return\_date  | date | YES  |     | NULL    |       |

+--------------+------+------+-----+---------+-------+

5 rows in set (0.14 sec)



mysql> show create table Lib\_Books;

| Table     | Create Table                                                                                                                                                                                                                                                                                                                 | Lib\_Books | CREATE TABLE `lib\_books` (

&nbsp; `Lib\_Issue\_id` int NOT NULL,

&nbsp; `Book\_No` int DEFAULT NULL,

&nbsp; `Member\_id` int DEFAULT NULL,

&nbsp; `issue\_date` date DEFAULT NULL,

&nbsp; `return\_date` date DEFAULT NULL,

&nbsp; KEY `Book\_No` (`Book\_No`),

&nbsp; KEY `Member\_id` (`Member\_id`)

) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4\_0900\_ai\_ci |

1 row in set (0.01 sec)



mysql>



**26) Insert a record in Issue table. The member\_id should not exist in**

**member table.**



mysql> INSERT INTO Lib\_Books

&nbsp;   -> (Lib\_Issue\_Id, Book\_No, Member\_Id, Issue\_Date, Return\_Date)

&nbsp;   -> VALUES

&nbsp;   -> (7001, 101, 4, '2006-12-01', NULL);

Query OK, 1 row affected (0.04 sec)



mysql> table Lib\_Books;

+--------------+---------+-----------+------------+-------------+

| Lib\_Issue\_id | Book\_No | Member\_id | issue\_date | return\_date |

+--------------+---------+-----------+------------+-------------+

|         7001 |     101 |         1 | 2006-12-15 | NULL        |

|         7002 |     102 |         2 | 2006-12-15 | NULL        |

|         7003 |     104 |         1 | 2006-01-06 | NULL        |

|         7004 |     101 |         1 | 2006-07-04 | NULL        |

|         7005 |     104 |         2 | 2006-11-15 | NULL        |

|         7006 |     101 |         3 | 2006-02-18 | NULL        |

|         7001 |     101 |         4 | 2006-12-01 | NULL        |

+--------------+---------+-----------+------------+-------------+

7 rows in set (0.01 sec)



mysql>



**27) Now enable the constraints of Issue table. Observe the error.**





mysql> alter table issue

-> add primary key(lib\_issue\_id);

ERROR 1068 (42000): Multiple primary key defined



mysql> alter table issue

-> add foreign key(book\_no)

-> references books (book\_no); affected (0.07 sec)

Query OK, 7 rows Records: 7 Duplicates: 0 Warnings:



mysql> alter table issue

-> add foreign key(member\_id)

-> references member(member\_id);

ERROR 1452 (23000): Cannot add or update a child row: a foreign key constraint fails (store. @sql-12cc\_2c", CONSTRAINT "issue\_ibfk 2 FOREIGN KEY (member id') REFERENCES `member` (`member\_id')) I



28\) Delete the record inserted at Q-27) and enable the constraints.



mysql> delete from issue

-> where member id 999;

Query OK, 1 row affected (0.00 sec)



mysql> alter table issue

-> add primary key(lib\_issue\_id); 

ERROR 1068 (42000): Multiple primary key defined



mysql> alter table issue

->add foreign key(book\_no)

-> references books (book\_no);

Query OK, 6 rows affected (0.09 sec) Records: 6 Duplicates: 0 Warnings: 0



mysql>alter table issue

->add foreign key(member\_id)

->references member(member\_id);

Query OK, 6 rows affected (0.09 sec) Records: 6 Duplicates: 0 Warnings: 0







**29) Try to delete the record of member id 1 from member table and**



**observe the error .**



mysql> delete from Member

&nbsp;   -> where Member\_id = 1;

Query OK, 1 row affected (0.06 sec)



mysql> table Member;

+-----------+----------------+----------------+---------------+-----------------+-----------+-------------------+----------------+

| Member\_id | Member\_name    | Member\_address | Acc\_open\_Date | Membership\_type | Fees\_paid | max\_books\_allowed | Penalty\_Amount |

+-----------+----------------+----------------+---------------+-----------------+-----------+-------------------+----------------+

|         2 | Garima Sen     | Pune           | 2025-12-19    | Annual          |      1000 |                 3 |           NULL |

|         3 | Pranali Jadhav | Satara         | 2015-02-21    | Half Yearly     |      2500 |                 4 |          70.00 |

|         4 | Ankita Jadhav  | Mumbai         | 2017-02-23    | Quarterly       |      2500 |                 4 |          70.00 |

|         5 | Sayali lad     | Dhule          | 2022-04-20    | Annual          |      3000 |                 9 |          60.00 |

|         6 | Sahil Jamdade  | Kolhapur       | 2024-07-21    | Half Yearly     |      4500 |                 6 |          87.00 |

|         7 | Sumit Jadhav   | Chattisgadh    | 2023-07-25    | Quarterly       |      3300 |                 7 |          67.00 |

+-----------+----------------+----------------+---------------+-----------------+-----------+-------------------+----------------+

6 rows in set (0.05 sec)



mysql>







**30) View the data and structure of all the three tables Member,**



**Issue, Book.**



mysql> desc Member;

+-------------------+--------------+------+-----+---------+-------+

| Field             | Type         | Null | Key | Default | Extra |

+-------------------+--------------+------+-----+---------+-------+

| Member\_id         | int          | NO   | PRI | NULL    |       |

| Member\_name       | varchar(20)  | YES  |     | NULL    |       |

| Member\_address    | varchar(50)  | YES  |     | NULL    |       |

| Acc\_open\_Date     | date         | YES  |     | NULL    |       |

| Membership\_type   | varchar(20)  | YES  |     | NULL    |       |

| Fees\_paid         | int          | YES  |     | NULL    |       |

| max\_books\_allowed | int          | YES  |     | NULL    |       |

| Penalty\_Amount    | decimal(7,2) | YES  |     | NULL    |       |

+-------------------+--------------+------+-----+---------+-------+

8 rows in set (0.01 sec)



mysql> desc Books;

+-------------+-------------+------+-----+---------+-------+

| Field       | Type        | Null | Key | Default | Extra |

+-------------+-------------+------+-----+---------+-------+

| Book\_No     | int         | NO   | PRI | NULL    |       |

| Book\_Name   | varchar(30) | NO   |     | NULL    |       |

| Author\_Name | varchar(30) | YES  |     | NULL    |       |

| Cost        | int         | YES  |     | NULL    |       |

| Category    | char(10)    | YES  |     | NULL    |       |

+-------------+-------------+------+-----+---------+-------+

5 rows in set (0.01 sec)



mysql> desc Lib\_Books;

+--------------+------+------+-----+---------+-------+

| Field        | Type | Null | Key | Default | Extra |

+--------------+------+------+-----+---------+-------+

| Lib\_Issue\_id | int  | NO   |     | NULL    |       |

| Book\_No      | int  | YES  | MUL | NULL    |       |

| Member\_id    | int  | YES  | MUL | NULL    |       |

| issue\_date   | date | YES  |     | NULL    |       |

| return\_date  | date | YES  |     | NULL    |       |

+--------------+------+------+-----+---------+-------+

5 rows in set (0.01 sec)





mysql> table Member;

+-----------+----------------+----------------+---------------+-----------------+-----------+-------------------+----------------+

| Member\_id | Member\_name    | Member\_address | Acc\_open\_Date | Membership\_type | Fees\_paid | max\_books\_allowed | Penalty\_Amount |

+-----------+----------------+----------------+---------------+-----------------+-----------+-------------------+----------------+

|         2 | Garima Sen     | Pune           | 2025-12-19    | Annual          |      1000 |                 3 |           NULL |

|         3 | Pranali Jadhav | Satara         | 2015-02-21    | Half Yearly     |      2500 |                 4 |          70.00 |

|         4 | Ankita Jadhav  | Mumbai         | 2017-02-23    | Quarterly       |      2500 |                 4 |          70.00 |

|         5 | Sayali lad     | Dhule          | 2022-04-20    | Annual          |      3000 |                 9 |          60.00 |

|         6 | Sahil Jamdade  | Kolhapur       | 2024-07-21    | Half Yearly     |      4500 |                 6 |          87.00 |

|         7 | Sumit Jadhav   | Chattisgadh    | 2023-07-25    | Quarterly       |      3300 |                 7 |          67.00 |

+-----------+----------------+----------------+---------------+-----------------+-----------+-------------------+----------------+

6 rows in set (0.00 sec)



mysql> table Books;

+---------+---------------------------+---------------------+------+----------+

| Book\_No | Book\_Name                 | Author\_Name         | Cost | Category |

+---------+---------------------------+---------------------+------+----------+

|     101 | Let us c                  | Dennis Ritchie      |  450 | system   |

|     102 | Oracle-Complete Ref       | Loni                |  250 | databse  |

|     103 | Mastering SQL             | Loni                |  250 | databse  |

|     104 | PL SQL-Ref                | Scott Urman         |  750 | databse  |

|     105 | National geograhic        | Adis scott          | 1000 | science  |

|     106 | Wings of fire             | Dr. APJ Abdul kalam |  180 | Others   |

|     107 | Operating system Concepts | WILEY               |  400 | system   |

+---------+---------------------------+---------------------+------+----------+

7 rows in set (0.01 sec)



mysql> table Lib\_Books;

+--------------+---------+-----------+------------+-------------+

| Lib\_Issue\_id | Book\_No | Member\_id | issue\_date | return\_date |

+--------------+---------+-----------+------------+-------------+

|         7001 |     101 |         1 | 2006-12-15 | NULL        |

|         7002 |     102 |         2 | 2006-12-15 | NULL        |

|         7003 |     104 |         1 | 2006-01-06 | NULL        |

|         7004 |     101 |         1 | 2006-07-04 | NULL        |

|         7005 |     104 |         2 | 2006-11-15 | NULL        |

|         7006 |     101 |         3 | 2006-02-18 | NULL        |

|         7001 |     101 |         4 | 2006-12-01 | NULL        |

+--------------+---------+-----------+------------+-------------+

7 rows in set (0.00 sec)



mysql>



**31) Modify the Return\_Date of 7004,7005 to 15 days after the**



Issue\_date.



mysql> UPDATE Lib\_Books

&nbsp;   -> SET Return\_Date = Issue\_Date + 15

&nbsp;   -> WHERE Lib\_Issue\_Id IN (7004, 7005);

Query OK, 2 rows affected (0.03 sec)

Rows matched: 2  Changed: 2  Warnings: 0



mysql> table Lib\_Books;

+--------------+---------+-----------+------------+-------------+

| Lib\_Issue\_id | Book\_No | Member\_id | issue\_date | return\_date |

+--------------+---------+-----------+------------+-------------+

|         7001 |     101 |         1 | 2006-12-15 | NULL        |

|         7002 |     102 |         2 | 2006-12-15 | NULL        |

|         7003 |     104 |         1 | 2006-01-06 | NULL        |

|         7004 |     101 |         1 | 2006-07-04 | 2006-07-19  |

|         7005 |     104 |         2 | 2006-11-15 | 2006-11-30  |

|         7006 |     101 |         3 | 2006-02-18 | NULL        |

|         7001 |     101 |         4 | 2006-12-01 | NULL        |

+--------------+---------+-----------+------------+-------------+

7 rows in set (0.00 sec)



mysql>



**32) Remove all the records from Issue table where member\_ID is 1**



**and Issue date in before 10-Dec-06.**



mysql> DELETE FROM Lib\_Books

&nbsp;   -> WHERE Member\_Id = 1

&nbsp;   -> AND Issue\_Date < '2006-12-10';

Query OK, 0 rows affected (0.00 sec)



mysql> table Lib\_Books;

+--------------+---------+-----------+------------+-------------+

| Lib\_Issue\_id | Book\_No | Member\_id | issue\_date | return\_date |

+--------------+---------+-----------+------------+-------------+

|         7001 |     101 |         1 | 2006-12-15 | NULL        |

|         7002 |     102 |         2 | 2006-12-15 | NULL        |

|         7005 |     104 |         2 | 2006-11-15 | 2006-11-30  |

|         7006 |     101 |         3 | 2006-02-18 | NULL        |

|         7001 |     101 |         4 | 2006-12-01 | NULL        |

+--------------+---------+-----------+------------+-------------+

5 rows in set (0.00 sec)



mysql>



**33) Remove all the records from Book table with category other**

**than RDBMS and Database.**





mysql> delete from Books

&nbsp;   -> where Category not in("RDBMS","Database");

Query OK, 7 rows affected (0.01 sec)



mysql> table Books;

Empty set (0.00 sec)



mysql>

**34) Remove the table Member**.



mysql> drop table Member;

Query OK, 0 rows affected (0.10 sec)



mysql> table Member;

ERROR 1146 (42S02): Table 'fbs.member' doesn't exist

mysql>



**35) Remove the table book**



mysql> drop table book;

Query OK, 0 rows affected (0.19 sec)



ERROR 1146 (42S02): Table 'fbs.book' doesn't exist

mysql>





