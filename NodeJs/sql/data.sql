DROP TABLE IF EXISTS students;
DROP TABLE IF EXISTS events;
DROP TABLE IF EXISTS combination;

CREATE TABLE students{
  ID smallint NOT NULL,
  name character varying(15) NOT NULL,
  email character varying(30) NOT NULL,
  password character varying(15) NOT NULL,
  studentId smallint NOT NULL,
  major character varying(10) NOT NULL
};

CREATE TABLE Teststudents{
  ID smallint NOT NULL,
  name character varying(15) NOT NULL,
  email character varying(30) NOT NULL,
  password character varying(15) NOT NULL,
  studentId smallint NOT NULL,
  major character varying(10) NOT NULL
};

CREATE TABLE events{
  ID smallint NOT NULL,
  discription character varying(300) NOT NULL,
  title character varying(15) NOT NULL,
  eventdate date NOT NULL,
  major character varying(10) NOT NULL
};

CREATE TABLE combination{
  ID smallint NOT NULL,
  userID smallint NOT NULL,
  eventID smallint NOT NULL
};

INSERT INTO students VALUES(1, 'Bobby', 'robert961@me.com', 'asdf1234', 123456789, 'computer science');
INSERT INTO students VALUES(2, 'Mitch', 'mitch961@me.com', 'asdf1234', 987654321, 'math');
INSERT INTO students VALUES(3, 'Will', 'will961@me.com', 'asdf1234', 456372891, 'history');

INSERT INTO events VALUES(1, 'bunch of theorems', 'math101', '2020-10-10', 'math');
INSERT INTO events VALUES(2, 'bunch of history', 'hist101', '2020-11-10', 'history');
INSERT INTO events VALUES(3, 'bunch of comp', 'csci101', '2020-12-10', 'computer science');

INSERT INTO combination VALUES(1, 1, 2);
INSERT INTO combination VALUES(2, 1, 3);
INSERT INTO combination VALUES(3, 2, 1);
INSERT INTO combination VALUES(4, 2, 3);
INSERT INTO combination VALUES(5, 3, 2);
INSERT INTO combination VALUES(6 ,3, 3);
