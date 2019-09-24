-- File: War.sql
-- Description: Create Sql Commands for War DB
-- Date: 2019-09-20
-- Author: Dayna Eidle

-- create statements --

--Reviewers--
create table Reviewers(
	reviewerId    integer not null,
	emailAddress  char not null,
	firstName     text not null,
	lastName      text not null,
	checkAdmin    text not null CHECK(checkAdmin = 'YES' or checkAdmin = 'NO'),
	reputation    integer not null,
  primary key (reviewerId)
);

--Sentences--
create table Sentences(
	sentenceId integer not null,
	userId     integer not null,
	sentence   text not null,
	rule1      bytea not null,
	rule2      bytea not null,
	rule3      bytea not null,
	rule4      bytea not null,
	rule5      bytea not null,
	dateAdded  timestamp not null,
  primary key(sentenceId)
);

--Reviews--
create table Reviews(
	reviewId      integer not null,
	reviewerId    integer not null references Reviewers(reviewerId),
	sentenceId    integer not null references Sentences(sentenceId),
	rule1         bytea not null,
	rule2         bytea not null,
	rule3         bytea not null,
	rule4         bytea not null,
	rule5         bytea not null,
	dateAdded     timestamp not null,
  primary key (reviewId)
);

--Dataset--
create table Dataset(
	sentenceId    integer not null references Sentences(sentenceId),
	sentence      text not null,
	rule1         bytea not null,
	rule2         bytea not null,
	rule3         bytea not null,
	rule4         bytea not null,
	rule5         bytea not null,
	dateAdded     timestamp not null,
  primary key (sentenceId)
);

--Versions--
create table Versions(
	modelId     integer not null,
	balAccuracy decimal not null,
	ruleNum     integer not null,
	loc         text not null,
	dateAdded   timestamp not null,
  primary key (modelId)
);


