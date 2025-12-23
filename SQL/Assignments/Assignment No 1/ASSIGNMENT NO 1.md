**ASSIGNMENT NO 1**





**Q1.Login to MySQL and view all databases already present. You should get following result:**



mysql> show databases;

+--------------------+

| Database           |

+--------------------+

| emp                |

| eventmanagementdb  |

| fbs                |

| information\_schema |

| mysql              |

| performance\_schema |

| sys                |

+--------------------+

7 rows in set (0.17 sec)





**Q2.Write an SQL statement to create a simple table countries including columns**

**country\_id,country\_name and region\_id. After this display the structure of table as below:**



mysql> create table countries

    -> (Country\_id int,Country\_name varchar(20),region\_id int);

Query OK, 0 rows affected (0.09 sec)



mysql> desc countries;

+--------------+-------------+------+-----+---------+-------+

| Field        | Type        | Null | Key | Default | Extra |

+--------------+-------------+------+-----+---------+-------+

| Country\_id   | int         | YES  |     | NULL    |       |

| Country\_name | varchar(20) | YES  |     | NULL    |       |

| region\_id    | int         | YES  |     | NULL    |       |

+--------------+-------------+------+-----+---------+-------+

3 rows in set (0.08 sec)





**Q3. Write an SQL statement to create a table named jobs including columns**

**job\_id, job\_title, min\_salary, max\_salary and check whether the**

**max\_salary amount exceeding the upper limit 25000. Also set job\_id as**

**primary key and entering null values for job\_title is not allowed.?**





mysql> create table jobs

    -> (job\_id int,job\_title varchar(20),min\_salary int, max\_salary int);

Query OK, 0 rows affected (0.04 sec)



mysql> desc jobs;

+------------+-------------+------+-----+---------+-------+

| Field      | Type        | Null | Key | Default | Extra |

+------------+-------------+------+-----+---------+-------+

| job\_id     | int         | YES  |     | NULL    |       |

| job\_title  | varchar(20) | YES  |     | NULL    |       |

| min\_salary | int         | YES  |     | NULL    |       |

| max\_salary | int         | YES  |     | NULL    |       |

+------------+-------------+------+-----+---------+-------+

4 rows in set (0.01 sec)



mysql> alter table jobs

    -> add primary key(job\_id);

Query OK, 0 rows affected (0.10 sec)

Records: 0  Duplicates: 0  Warnings: 0



mysql> alter table jobs

    -> modify column job\_title varchar(20) not null;

Query OK, 0 rows affected (0.09 sec)

Records: 0  Duplicates: 0  Warnings: 0



mysql> alter table jobs

    -> modify column max\_salary int check(max\_salary <+ 25000);

Query OK, 0 rows affected (0.12 sec)

Records: 0  Duplicates: 0  Warnings: 0



mysql> desc jobs;

+------------+-------------+------+-----+---------+-------+

| Field      | Type        | Null | Key | Default | Extra |

+------------+-------------+------+-----+---------+-------+

| job\_id     | int         | NO   | PRI | NULL    |       |

| job\_title  | varchar(20) | NO   |     | NULL    |       |

| min\_salary | int         | YES  |     | NULL    |       |

| max\_salary | int         | YES  |     | NULL    |       |

+------------+-------------+------+-----+---------+-------+

4 rows in set (0.01 sec)





**Q4 Write a SQL statement to create a table named job\_histry including columns**

**employee\_id, start\_date, end\_date, job\_id and department\_id:**





mysql> create table job\_history

    -> (employee\_id int,start\_date int,end\_date int,job\_id int,department\_id int);

Query OK, 0 rows affected (0.24 sec)



mysql> desc job\_history;

+---------------+------+------+-----+---------+-------+

| Field         | Type | Null | Key | Default | Extra |

+---------------+------+------+-----+---------+-------+

| employee\_id   | int  | YES  |     | NULL    |       |

| start\_date    | int  | YES  |     | NULL    |       |

| end\_date      | int  | YES  |     | NULL    |       |

| job\_id        | int  | YES  |     | NULL    |       |

| department\_id | int  | YES  |     | NULL    |       |

+---------------+------+------+-----+---------+-------+

5 rows in set (0.05 sec)



mysql>





**Q5. Write an SQL statement to alter a table named countries to make sure that no**

**duplicate data against column country\_id will be allowed at the time of insertion:**





mysql> alter table countries

    -> modify column Country\_id int unique;

Query OK, 0 rows affected (0.16 sec)

Records: 0  Duplicates: 0  Warnings: 0



mysql> desc countries;

+--------------+-------------+------+-----+---------+-------+

| Field        | Type        | Null | Key | Default | Extra |

+--------------+-------------+------+-----+---------+-------+

| Country\_id   | int         | YES  | UNI | NULL    |       |

| Country\_name | varchar(20) | YES  |     | NULL    |       |

| region\_id    | int         | YES  |     | NULL    |       |

+--------------+-------------+------+-----+---------+-------+

3 rows in set (0.03 sec)



mysql>





**Q6.Write an SQL statement to create a table named jobs including columns job\_id,**

**job\_title, min\_salary and max\_salary, and make sure that, the default value**

**for job\_title is blank and min\_salary is 8000 and max\_salary is NULL will be**

**entered automatically at the time of insertion if no value assigned for the specified columns:**







mysql> alter table jobs

    -> modify column job\_title varchar(20) default '',

    -> modify column min\_salary int default 8000,

    ->  modify column max\_salary int default NULL;

Query OK, 0 rows affected (0.08 sec)

Records: 0  Duplicates: 0  Warnings: 0



mysql> desc jobs;

+------------+-------------+------+-----+---------+-------+

| Field      | Type        | Null | Key | Default | Extra |

+------------+-------------+------+-----+---------+-------+

| job\_id     | int         | NO   | PRI | NULL    |       |

| job\_title  | varchar(20) | YES  |     |         |       |

| min\_salary | int         | YES  |     | 8000    |       |

| max\_salary | int         | YES  |     | NULL    |       |

+------------+-------------+------+-----+---------+-------+

4 rows in set (0.00 sec)



mysql>







**Q7.Create a Department table with following structure:**





mysql> create table Dept

    -> (DEPARTMENT\_ID decimal(4,0),DEPARTMENT\_NAME varchar(30),

    -> MANAGER\_ID decimal(6,0),LOCATION\_ID decimal(4,0));

Query OK, 0 rows affected (0.04 sec)



alter table Dept

    -> add primary key(DEPARTMENT\_ID,MANAGER\_ID);

Query OK, 0 rows affected (0.08 sec)

Records: 0  Duplicates: 0  Warnings: 0





mysql> alter table Dept

    -> modify column DEPARTMENT\_ID DECIMAL(4,0) default 0,

    -> modify column MANAGER\_ID DECIMAL(6,0) default 0;

Query OK, 0 rows affected (0.01 sec)

Records: 0  Duplicates: 0  Warnings: 0



mysql> alter table Dept

    -> modify column DEPARTMENT\_NAME varchar(20) not null;

Query OK, 0 rows affected (0.09 sec)

Records: 0  Duplicates: 0  Warnings: 0





mysql> desc Dept;

+-----------------+--------------+------+-----+---------+-------+

| Field           | Type         | Null | Key | Default | Extra |

+-----------------+--------------+------+-----+---------+-------+

| DEPARTMENT\_ID   | decimal(4,0) | NO   | PRI | 0       |       |

| DEPARTMENT\_NAME | varchar(20)  | NO   |     | NULL    |       |

| MANAGER\_ID      | decimal(6,0) | NO   | PRI | 0       |       |

| LOCATION\_ID     | decimal(4,0) | YES  |     | NULL    |       |

+-----------------+--------------+------+-----+---------+-------+

4 rows in set (0.00 sec)









**Q8. Write an SQL statement to create a table employees including columns**

**employee\_id, first\_name, last\_name, email, phone\_number hire\_date, job\_id,**

**salary, commission, manager\_id and department\_id and make sure that, the**

**employee\_id column does not contain any duplicate value at the time of**

**insertion and the foreign key columns combined by department\_id and**

**manager\_id columns contain only those unique combination values, which**

**combinations are exists in the departments table:**









mysql> create table Employees

    -> (emp\_id int,first\_name varchar(20),last\_name varchar(20),

    -> email\_id varchar(20),phone\_number int,hire\_date int,job\_id int,

    -> salary int,commission int,manager\_id int,department\_id int);

Query OK, 0 rows affected (0.03 sec)





mysql> alter table Employees

    -> add primary key(emp\_id);

Query OK, 0 rows affected (0.05 sec)

Records: 0  Duplicates: 0  Warnings: 0



mysql> alter table Employees

    -> modify department\_id decimal(4,0),

    -> modify manager\_id decimal(6,0);

Query OK, 0 rows affected (0.07 sec)

Records: 0  Duplicates: 0  Warnings: 0



mysql> alter table Employees

    -> add constraint fk\_dept\_manager

    -> foreign key (department\_id,manager\_id)

    -> references department(department\_id,manager\_id);

Query OK, 0 rows affected (0.10 sec)

Records: 0  Duplicates: 0  Warnings: 0



mysql> desc Employees;

+---------------+--------------+------+-----+---------+-------+

| Field         | Type         | Null | Key | Default | Extra |

+---------------+--------------+------+-----+---------+-------+

| emp\_id        | int          | NO   | PRI | NULL    |       |

| first\_name    | varchar(20)  | YES  |     | NULL    |       |

| last\_name     | varchar(20)  | YES  |     | NULL    |       |

| email\_id      | varchar(20)  | YES  |     | NULL    |       |

| phone\_number  | int          | YES  |     | NULL    |       |

| hire\_date     | int          | YES  |     | NULL    |       |

| job\_id        | int          | YES  |     | NULL    |       |

| salary        | int          | YES  |     | NULL    |       |

| commission    | int          | YES  |     | NULL    |       |

| manager\_id    | decimal(6,0) | YES  |     | NULL    |       |

| department\_id | decimal(4,0) | YES  | MUL | NULL    |       |

+---------------+--------------+------+-----+---------+-------+



mysql> alter table Employees

    -> add index idx\_manager(manager\_id);

Query OK, 0 rows affected (0.03 sec)

Records: 0  Duplicates: 0  Warnings: 0



mysql> desc Employees;

+---------------+--------------+------+-----+---------+-------+

| Field         | Type         | Null | Key | Default | Extra |

+---------------+--------------+------+-----+---------+-------+

| emp\_id        | int          | NO   | PRI | NULL    |       |

| first\_name    | varchar(20)  | YES  |     | NULL    |       |

| last\_name     | varchar(20)  | YES  |     | NULL    |       |

| email\_id      | varchar(20)  | YES  |     | NULL    |       |

| phone\_number  | int          | YES  |     | NULL    |       |

| hire\_date     | int          | YES  |     | NULL    |       |

| job\_id        | int          | YES  |     | NULL    |       |

| salary        | int          | YES  |     | NULL    |       |

| commission    | int          | YES  |     | NULL    |       |

| manager\_id    | decimal(6,0) | YES  | MUL | NULL    |       |

| department\_id | decimal(4,0) | YES  | MUL | NULL    |       |

+---------------+--------------+------+-----+---------+-------+

11 rows in set (0.00 sec)

