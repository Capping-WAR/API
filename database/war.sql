-- File: War.sql
-- Description: Create Sql Commands for War DB
-- Date: 2019-09-20
-- Author: Dayna Eidle 
-- Updated By: Daniel Gisolfi

-- create statements --

--Reviewers--
create table Reviewers(
	reviewerId    SERIAL PRIMARY KEY,
	emailAddress  char not null,
	firstName     text not null,
	lastName      text not null,
	checkAdmin    text not null CHECK(checkAdmin = 'YES' or checkAdmin = 'NO'),
	reputation    integer not null,
);

--Sentences--
create table Sentences(
	sentenceId SERIAL PRIMARY KEY,
	userId     integer not null,
	sentence   text not null,
	rule1      integer not null,
	rule2      integer not null,
	rule3      integer not null,
	rule4      integer not null,
	rule5      integer not null,
	dateAdded  timestamp not null,
);

--Reviews--
create table Reviews(
	reviewId      SERIAL PRIMARY KEY,
	reviewerId    integer not null references Reviewers(reviewerId),
	sentenceId    integer not null references Sentences(sentenceId),
	rule1         integer not null,
	rule2         integer not null,
	rule3         integer not null,
	rule4         integer not null,
	rule5         integer not null,
	dateAdded     timestamp not null,
);

--Dataset--
create table Dataset(
	sentenceId    integer not null references Sentences(sentenceId),
	sentence      text not null,
	rule1         integer not null,
	rule2         integer not null,
	rule3         integer not null,
	rule4         integer not null,
	rule5         integer not null,
	dateAdded     timestamp not null,
  primary key (sentenceId)
);

--Versions--
create table Versions(
	modelId     SERIAL PRIMARY KEY,
	balAccuracy decimal not null,
	ruleNum     integer not null,
	loc         text not null,
	dateAdded   timestamp not null,
);