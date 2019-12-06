DROP TABLE IF EXISTS students;
DROP TABLE IF EXISTS events;
DROP TABLE IF EXISTS cobination;

CREATE TABLE students{
  ID smallint NOT NULL,
  name character varying(15) NOT NULL,
  username character varying(15) NOT NULL,
  password character varying(15) NOT NULL,
  major character varying(10) NOT NULL
};

CREATE TABLE events{
  ID smallint NOT NULL,
  discription character varying(300) NOT NULL,
  title character varying(15) NOT NULL,
  date date NOT NULL,
  major character varying(10) NOT NULL
};

CREATE TABLE combination{
  ID smallint NOT NULL,
  userID smallint NOT NULL,
  eventID smallint NOT NULL
};

INSERT INTO students VALUES(1, 'Bobby', 'robert961@me.com', 'asdf1234', 'computer science');
INSERT INTO students VALUES(2, 'Mitch', 'mitch961@me.com', 'asdf1234', 'math');
INSERT INTO students VALUES(3, 'Will', 'will961@me.com', 'asdf1234', 'history');

INSERT INTO events VALUES(1, 'bunch of shit', 'shit101', '2020-10-10', 'math');
INSERT INTO events VALUES(2, 'bunch of history', 'hist101', '2020-11-10', 'history');
INSERT INTO events VALUES(3, 'bunch of comp', 'csci101', '2020-12-10', 'computer science');

INSERT INTO combination VALUES(1, 1, 2);
INSERT INTO combination VALUES(2, 1, 3);
INSERT INTO combination VALUES(3, 2, 1);
INSERT INTO combination VALUES(4, 2, 3);
INSERT INTO combination VALUES(5, 3, 2);
INSERT INTO combination VALUES(6 ,3, 3);
