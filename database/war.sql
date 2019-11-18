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

create or replace function getTopReviewers(reviewer int)
returns table(rid int, fname text, lname text, rep int) as $$
begin 
  if (reviewer not in (select reviewerid
                     from reviewers 
                     order by reputation desc
                     limit 2))
     then return query (select reviewerid, firstname, lastname, reputation
                     from reviewers 
                     order by reputation desc
                     limit 2 );
          return query (select reviewerid, firstname, lastname, reputation
                       from reviewers
                       where reviewerid = reviewer);
  else
    return query (select reviewerid, firstname, lastname, reputation
                 from reviewers
                 order by reputation desc
                 limit 3);
  end if;
end;
$$ language 'plpgsql';

create function getTotalCountOfReviews(sentence int)
returns int as $$
  begin
    return (select count(ruleReviewid)/5
            from peoplereviews
            where sentenceid = sentence);
  end;
$$ language 'plpgsql';

create function getCorrectReviewsCount(sentence int)
returns int as $$
  begin
    return(select count(pr.rulereview)
            from peoplereviews pr inner join sentencerules sr on pr.sentenceid = sr.sentenceid
            where pr.sentenceid = 1 and pr.rulereviewid = sr.taggedruleid and pr.rulereview = 1
            group by pr.rulereviewid);
  end;
$$ language 'plpgsql';

create function getIncorrectReviewsCount(sentence int)
returns int as $$
  begin
    return(select count(pr.rulereview)
            from peoplereviews pr inner join sentencerules sr on pr.sentenceid = sr.sentenceid
            where pr.sentenceid = 1 and pr.rulereviewid = sr.taggedruleid and pr.rulereview = 0
            group by pr.rulereviewid);
  end;
$$ language 'plpgsql';

CREATE OR REPLACE PROCEDURE getSentenceReviewStatus(sentence int)
AS $$
  begin
    if (getTotalCountOfReviews(sentence) == 5) then
      if (getCorrectReviewsCount(sentence) == 5) or (getIncorrectReviewsCount(sentence) == 5) then
        perform sendToDataset(sentence);
      end if;
    elsif (getTotalCountOfReviews(sentence) > 5) then
      if ((getCorrectReviewsCount(sentence) / getIncorrectReviewsCount(sentence)) >= .75 and
          (getCorrectReviewsCount(sentence) / getIncorrectReviewsCount(sentence)) < 1) then
          perform sendToDataset(sentence);
      elsif ((getIncorrectReviewsCount(sentence) / getCorrectReviewsCount(sentence)) >= .75 and
                (getIncorrectReviewsCount(sentence) / getCorrectReviewsCount(sentence)) < 1) then
         perform sendToDataset(sentence);
      end if;
    end if;
  end;
$$ language plpgsql;


create function getSentenceFromID(sentID int)
returns text as $$
begin
  return (select sentence
          from sentences
          where sentenceid = sentID);
   end;
$$ language 'plpgsql';

create or replace procedure sendToDataset(sentence int)
as $$
BEGIN
   insert into TrainingDataSet(sentenceId, sentence, ruleCorrectId, ruleCorrect, dateAdded)
     select sentence, getSentenceFromId(sentence), rulereviewid, avg(rulereview), current_timestamp
     from peoplereviews 
     where sentenceid = sentence
     group by rulereviewid; 
END
$$ 
LANGUAGE plpgsql;