-- File: War.sql
-- Description: Create Sql Commands for War DB
-- Date: 2019-09-20
-- Author: Dayna Eidle

\c war;

-- create statements --

--Reviewers--
create table Reviewers(
	reviewerId    integer not null,
	emailAddress  text not null,
	firstName     text not null,
	lastName      text not null,
	isAdmin       bool not null,
	reputation    integer not null,
  primary key (reviewerId)
);

--Rules--
create table Rules(
	ruleId      SERIAL PRIMARY KEY,
	ruleName    text not null,
	description text not null,
	priority    decimal not null
);

--Sentences--
create table Sentences(
	sentenceId   SERIAL PRIMARY KEY,
	userId       integer not null,
	sentence     text not null,
	taggedRuleId integer not null references Rules(ruleId),
	dateAdded 	 timestamp not null
);


--People Reviews--
create table PeopleReviews(
	sentenceId    integer not null references Sentences(sentenceId),
	reviewerId   integer not null references Reviewers(reviewerId),
	ruleReviewId integer not null references Rules(ruleId),
	ruleReview   integer not null,
	dateAdded    timestamp not null,
  primary key(sentenceId, reviewerId, ruleReviewId)
);

--Models--
create table Models(
	modelId   SERIAL PRIMARY KEY,
    modelVersion SERIAL,
	balAccuracy  decimal not null,
	loc          text not null,
	dateAdded    timestamp not null
    UNIQUE(modelId, modelVersion)
);

--Model Reviews--
create table ModelReviews(
	sentenceId   integer not null references Sentences(sentenceId),
	ruleId       integer not null references Rules(ruleId),
	modelId      integer not null,
	modelVersion integer not null,
	foreign key (modelID, modelVersion) references Models(modelId, modelVersion),
  primary key(sentenceId, ruleId, modelId, modelVersion)
);

--TrainingDataset
create table TrainingDataset(
	sentenceId    integer not null,
	sentence      text not null,
	ruleCorrectId integer not null,
	ruleCorrect   decimal not null,
	dateAdded     timestamp not null,
  primary key(sentenceId, ruleCorrectId)
);

--SentenceRules--
create table SentenceRules(
	sentenceId   integer not null references Sentences(sentenceId),
	taggedRuleId integer not null references Rules(ruleId),
	status       text not null,
  primary key(sentenceId, taggedRuleId)
);