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
    modelId SERIAL PRIMARY KEY,
    modelVersion text not null,
	balAccuracy  decimal not null,
	isActive     boolean not null,
	dateAdded    timestamp not null,
    ruleId       integer not null references Rules(ruleId)
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

--SentenceRules
create table SentenceRules(
	sentenceId   integer not null references Sentences(sentenceId),
	taggedRuleId integer not null references Rules(ruleId),
	status       text not null,
  primary key(sentenceId, taggedRuleId)
);

--UserStatistics
create table userStatistics(
    statisticsID SERIAL PRIMARY KEY,
    windowsCount integer not null,
    macosCount integer not null,
    otherCount integer not null,
    isDesktopCount integer not null,
    isMobileCount integer not null
);

insert into userStatistics (windowsCount, macosCount, otherCount, isDesktopCount, isMobileCount) values(0,0,0,0,0);

--loginStatistics
create table loginStatistics(
    dateID   SERIAL PRIMARY KEY,
    dayDate timestamp not null,
	loginCount   integer not null,
    reviewCount   integer not null
);

-- update these dates to today and the previous 6 days
insert into loginStatistics (dayDate, loginCount, reviewCount) values
(to_date('2019-11-13', 'YYYY-MM-DD'),0,0),
(to_date('2019-11-14', 'YYYY-MM-DD'),0,0),
(to_date('2019-11-15', 'YYYY-MM-DD'),0,0),
(to_date('2019-11-16', 'YYYY-MM-DD'),0,0),
(to_date('2019-11-17', 'YYYY-MM-DD'),0,0),
(to_date('2019-11-18', 'YYYY-MM-DD'),0,0),
(to_date('2019-11-19', 'YYYY-MM-DD'),0,0);

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

create or replace function getCorrectReviewsCount(sentence int)
returns int as $$
  begin
    return(select count(pr.rulereview)/5
            from peoplereviews pr inner join sentencerules sr on pr.sentenceid = sr.sentenceid
            where pr.sentenceid = 1 and pr.rulereviewid = sr.taggedruleid and pr.rulereview = 1
            group by pr.rulereviewid);
  end;
$$ language 'plpgsql';

create or replace function getIncorrectReviewsCount(sentence int)
returns int as $$
  begin
    return(select count(pr.rulereview)/5
            from peoplereviews pr inner join sentencerules sr on pr.sentenceid = sr.sentenceid
            where pr.sentenceid = 1 and pr.rulereviewid = sr.taggedruleid and pr.rulereview = 0
            group by pr.rulereviewid);
  end;
$$ language 'plpgsql';

CREATE OR REPLACE PROCEDURE getSentenceReviewStatus(sentence int)
AS $$
  begin
    if (getTotalCountOfReviews(sentence) = 5) then
      if (getCorrectReviewsCount(sentence) = 5) or (getIncorrectReviewsCount(sentence) == 5) then
        perform sendToDataset(sentence);
      end if;
    elsif (getTotalCountOfReviews(sentence) > 5) then
      if ((getCorrectReviewsCount(sentence) / getIncorrectReviewsCount(sentence)) >= .75 and
          (getCorrectReviewsCount(sentence) / getIncorrectReviewsCount(sentence)) < 1) then
          perform sendToDataset(sentence);
		  update sentenceRules
		  set status = 'Corrected'
		  where sentenceid = sentence;
      elsif ((getIncorrectReviewsCount(sentence) / getCorrectReviewsCount(sentence)) >= .75 and
                (getIncorrectReviewsCount(sentence) / getCorrectReviewsCount(sentence)) < 1) then
         perform sendToDataset(sentence);
		 update sentenceRules
		  set status = 'Corrected'
		  where sentenceid = sentence;
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

CREATE OR REPLACE FUNCTION SentenceToBeReviewed (userID INT)
RETURNS TABLE(sentenceid INT) AS $$
    BEGIN
        RETURN QUERY select sr.sentenceid
        from sentencerules sr inner join rules r on sr.taggedruleid = r.ruleid
        where sr.sentenceid not in (select sentenceid
                            from peoplereviews 
                            where reviewerid = userID)
        and sr.status = 'In Review'
        order by priority desc
        limit 1;
    END;
$$ LANGUAGE 'plpgsql';

create or replace procedure updatePriority()
as $$ 
declare temprow rules%rowtype;
declare counter int := 1;
  begin
    for temprow in select ruleid, count(sr.sentenceid) filter (where sr.status = 'Corrected')
                   from rules r left outer join sentencerules sr on r.ruleid = sr.taggedruleid
                   group by r.ruleid
                   order by count(sr.sentenceid) desc
    loop
	  update rules
	  set priority = counter
	  where ruleid = temprow.ruleid;
	  counter := counter + 1;
  end loop;
  end;
$$ language plpgsql;

create or replace function getRuleGrade(sentid int)
returns decimal as $$
  begin 
    return (select td.rulecorrect
            from trainingdataset td inner join sentencerules sr on td.sentenceid = sr.sentenceid
            where td.rulecorrectid = sr.taggedruleid
            and td.sentenceid = sentid);
  end;
$$ language plpgsql;


CREATE OR REPLACE PROCEDURE updateReputation(sentID int)
LANGUAGE sql
AS $$
  UPDATE reviewers r
  SET reputation = reputation + (CASE WHEN 
      (getRuleGrade(sentID) > .5)
    THEN
	  CASE WHEN pr.rulereview = 1 THEN
        +10
      ELSE
        -10
	  END
	ELSE
	  CASE WHEN pr.rulereview = 0 THEN
        +10
      ELSE
        -10
	  END
    END)
  FROM peoplereviews pr
  INNER JOIN sentencerules sr ON (pr.sentenceid = sr.sentenceid
                                  AND pr.rulereviewid = sr.taggedruleid)
  WHERE pr.reviewerid = r.reviewerid
    AND pr.sentenceid = sentID;
$$;