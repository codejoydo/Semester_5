--
-- SQL Quiz Tuesday 16-08-2016, 02:00PM
--  
--
-- USAGE
--      mysql -u <username> -p<password> < company.sql 
--
--


CREATE database COMPANY;
use COMPANY;

CREATE TABLE BONUS
        (ENAME VARCHAR(10),
         JOB   VARCHAR(9),
         SAL   integer,
         COMM  integer);

CREATE TABLE EMP
       (EMPNO integer(4) NOT NULL,
        ENAME VARCHAR(10),
        JOB VARCHAR(9),
        MGR integer(4),
        HIREDATE DATE,
        SAL float(7, 2),
        COMM float(7, 2),
        DEPTNO integer(2));

INSERT INTO EMP VALUES
        (7369, 'SMITH',  'CLERK',     7902,
        STR_TO_DATE('17-DEC-1980', '%d-%M-%Y'),  800, NULL, 20);
INSERT INTO EMP VALUES
        (7499, 'ALLEN',  'SALESMAN',  7698,
        STR_TO_DATE('20-FEB-1981', '%d-%M-%Y'), 1600,  300, 30);
INSERT INTO EMP VALUES
        (7521, 'WARD',   'SALESMAN',  7698,
        STR_TO_DATE('22-FEB-1981', '%d-%M-%Y'), 1250,  500, 30);
INSERT INTO EMP VALUES
        (7566, 'JONES',  'MANAGER',   7839,
        STR_TO_DATE('2-APR-1981', '%d-%M-%Y'),  2975, NULL, 20);
INSERT INTO EMP VALUES
        (7654, 'MARTIN', 'SALESMAN',  7698,
        STR_TO_DATE('28-SEP-1981', '%d-%M-%Y'), 1250, 1400, 30);
INSERT INTO EMP VALUES
        (7698, 'BLAKE',  'MANAGER',   7839,
        STR_TO_DATE('1-MAY-1981', '%d-%M-%Y'),  2850, NULL, 30);
INSERT INTO EMP VALUES
        (7782, 'CLARK',  'MANAGER',   7839,
        STR_TO_DATE('9-JUN-1981', '%d-%M-%Y'),  2450, NULL, 10);
INSERT INTO EMP VALUES
        (7788, 'SCOTT',  'ANALYST',   7566,
        STR_TO_DATE('09-DEC-1982', '%d-%M-%Y'), 3000, NULL, 20);
INSERT INTO EMP VALUES
        (7839, 'KING',   'PRESIDENT', NULL,
        STR_TO_DATE('17-NOV-1981', '%d-%M-%Y'), 5000, NULL, 10);
INSERT INTO EMP VALUES
        (7844, 'TURNER', 'SALESMAN',  7698,
        STR_TO_DATE('8-SEP-1981', '%d-%M-%Y'),  1500, NULL, 30);
INSERT INTO EMP VALUES
        (7876, 'ADAMS',  'CLERK',     7788,
        STR_TO_DATE('12-JAN-1983', '%d-%M-%Y'), 1100, NULL, 20);
INSERT INTO EMP VALUES
        (7900, 'JAMES',  'CLERK',     7698,
        STR_TO_DATE('3-DEC-1981', '%d-%M-%Y'),   950, NULL, 30);
INSERT INTO EMP VALUES
        (7902, 'FORD',   'ANALYST',   7566,
        STR_TO_DATE('3-DEC-1981', '%d-%M-%Y'),  3000, NULL, 20);
INSERT INTO EMP VALUES
        (7934, 'MILLER', 'CLERK',     7782,
        STR_TO_DATE('23-JAN-1982', '%d-%M-%Y'), 1300, NULL, 10);


INSERT INTO EMP VALUES
        (7935, 'RAJ', 'CLERK',     7782,
        STR_TO_DATE('23-JAN-1984', '%d-%M-%Y'), 1300, NULL, 20);
INSERT INTO EMP VALUES
        (7848, 'QUEEN',   'PRESIDENT', NULL,
        STR_TO_DATE('17-NOV-1979', '%d-%M-%Y'), 5000, NULL, 30);
 INSERT INTO EMP VALUES
         (3333,'ACHILLES','SALESMAN',7782,
        STR_TO_DATE('17-DEC-1980', '%d-%M-%Y'),7000,0,10);
 INSERT INTO EMP VALUES
         (8236,'CARL','OPMANAGER',7839,
        STR_TO_DATE('27-FEB-1982', '%d-%M-%Y'),6000,0,40);






CREATE TABLE DEPT
       (DEPTNO integer(2),
        DNAME VARCHAR(14),
        LOC VARCHAR(30) );

INSERT INTO DEPT VALUES (10, 'ACCOUNTING', 'NEW YORK');
INSERT INTO DEPT VALUES (20, 'RESEARCH',   'DALLAS');
INSERT INTO DEPT VALUES (30, 'SALES',      'CHICAGO');
INSERT INTO DEPT VALUES (40, 'OPERATIONS', 'BOSTON');

CREATE TABLE SALGRADE
        (GRADE integer,
         LOSAL integer,
         HISAL integer);

INSERT INTO SALGRADE VALUES (1,  700, 1200);
INSERT INTO SALGRADE VALUES (2, 1201, 1400);
INSERT INTO SALGRADE VALUES (3, 1401, 2000);
INSERT INTO SALGRADE VALUES (4, 2001, 3000);
INSERT INTO SALGRADE VALUES (5, 3001, 9999);

