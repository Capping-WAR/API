#!/usr/bin/python3
# Date: 2019-09-20
# Author: Daniel Nicolas Gisolfi

import os
import psycopg2
from typing import List

class ORM:
    """
    Object Relation Mapper

    All generic methods for interacting, connecting and 
    querying the database

    There are no public Attributes for this class
    """
    def __init__(self):
        self.db_info = {
            'database': os.getenv('DATABASE', 'postgres'),
            'user': os.getenv('USER', 'postgres'),
            'password': os.getenv('PASSWORD'),
            'host': os.getenv('HOST', 'database'),
            'port': os.getenv('PORT', 5432)
        }

        self.tables = {
            'TrainingDataset': 'sentenceID',
            'Rules':'ruleID',
            'Models':'modelID',
            'reviewers': 'reviewerID',
            'SentenceRules':'sentenceID',
            'sentences': 'sentenceID',
            'PeopleReviews': 'sentenceID',
            'ModelReviews':'sentenceID',
        }

        # create a connection, get a conn and a cursor back
        self._conn, self._cur = self._connect(self.db_info)
    
    def __del__(self):
        if hasattr(self, '_conn'):
            self._conn.close()

    def _connect(self, conn_info:dict) -> tuple:
        """Given the details of a postgres server a connection 
        will be created

        Parameters
        ----------
        conn_info : dict
            A dictionary containing the db name, user, password, 
            host, and port of a postgres server

        Returns
        -------
        conn : object
            psycopg2 connection object to the specifed server

        cur : object
            psycopg2 cursor object for the specified server

        Rasies
        ------
        Database Connection Error
            Occurs when the connection cannot be secured to 
            the postgres server
        """
        try:
            conn = psycopg2.connect(**conn_info)
            cur = conn.cursor()
            return conn, cur
        except:
            raise ValueError('Database Connection Error')


    # Run any query and return data if there is any
    def _query(self, sql:str) -> list or Exception:
        """Given a Query, it will be executed within the database

        Parameters 
        ----------
        sql : str
            A valid psql query

        Returns
        -------
        results : list
            All rows that meet the specifed query. if insert, 
            delete or update empty list is returned.
        error : Exception
            if an error occurs the exception will be returned
        """
        try:
            query = self._cur.mogrify(sql)
            self._cur.execute(query)
            self._conn.commit()
            results = self._cur.fetchall()

            if sql.split(' ')[0].lower() in ['insert','delete','update']:
                return []
            else:
                return results
        except Exception as err:
            return err

    """ Base Operations """

    def get(self, table:str, cols:str=None, 
        clause:str=None) -> list or Exception:
        """Returns all rows from the specified table meeting the 
        nessecary conditions

        Parameters 
        ----------
        table : str
            a valid table name from the database for
            the data to be inserted into.
        cols : str
            a string of comma seperated column names that corosponds 
            to the values, can be left out if all values are present.
        clause : str
            A condition to be met by the data, 
            EX: WHERE ID=3

        Returns
        -------
        response
            will return the response from the database.
        """

        sql = 'SELECT'
        if table.lower() not in self.tables.keys():
            return Exception(
                f'Invalid Table: {table}.'
                + f'Must be one of: {self.tables.keys()}'
            )
        
        if cols is not None:
            sql += cols
        else:
            sql += '*'

        sql += f"FROM {table}"

        if clause is not None:
            sql += f' {clause}'
        

        return self._query(f'{sql};')

    def insert(self, table:str, values:List[str], 
        cols:str=None) -> list or Exception:
        """Given data and a table the values will be inserted

        Parameters 
        ----------
        table : str
            a valid table name from the database for
            the data to be inserted into.
        values : list
            a list of strings holding the values to be inserted. EX:
            ["100, 1, '/home', current_timestamp"]
        cols : str
            a string of comma seperated column names that corosponds 
            to the values, can be left out if all values are present.

        Returns
        -------
        response
            will return the response from the database.
        """

        sql = f'INSERT INTO {table}'

        if cols is not None:
            sql += f' ({cols})'
        
        sql += f" VALUES ({','.join(values)})"

        return self._query(f'{sql};')

    def update(self, table:str, values:dict,
        clause:str=None) -> list or Exception:
        """Given a dict of cols and values, all rows that meet the 
        given clauses will be updated

        Parameters 
        ----------
        table : str
            a valid table name from the database for
            the data to be inserted into.
        values : dict
            Key value pairs of all updates to make. EX:
            {'col1': 'new_value'}
        clause : str
            A condition to be met by the data, 
            EX: WHERE ID=3
        
        Returns
        -------
        response
            will return the response from the database.
        """

        sql = f'UPDATE {table} SET'
        last_col = sorted(values.keys())[-1]
        for col, val in values.items():
            if col == last_col:
                sql += f' {col}={val}'
            else:
                sql += f' {col}={val},'
            
        if clause is not None:
            sql += f' {clause}'

        return self._query(f'{sql};')

    
    def delete(self, table:str, clause:str) -> list or Exception:
        """Given a clause all rows to meet it will be deleted 
        from the table

        Parameters 
        ----------
        table : str
            a valid table name from the database for
            the data to be inserted into.
        clause : str
            A condition to be met by the data, 
            EX: WHERE ID=3
        
        Returns
        -------
        response
            will return the response from the database.
        """

        sql = f"""
        DELETE FROM {table}
        {clause};
        """
        return self._query(sql)

    """ Add more here when nessecary """