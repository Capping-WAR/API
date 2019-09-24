#!/usr/bin/python3
# Date: 2019-09-20
# Author: Daniel Nicolas Gisolfi

import os
import psycopg2

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

        # create a connection, get a conn and a cursor back
        self._conn, self._cur = self._connect(self.db_info)

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
            # self._conn.close()

            if sql.split(' ')[0].lower() in ['insert','delete','update']:
                return []
            else:
                return results
        except Exception as err:
            return err