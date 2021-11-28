"""
A simple course review flask app.
Data is stored in a SQLite database that looks something like the following:
author, dept, crnum, qtr, year, instructor, review, rating
+--------+-----+-------+-----+------+---------------+----------------------------------------------------+--------+
| author |dept | crnum | qtr | year | instructor    | review                                             | rating |
+========+=====+=======+=====+======+===============+============================================+=======+========+
| Akasha | CS  | 430   | 1   | 2021 | Wu-Chang Feng | Great class, knowledgable and entertaining teacher | 5      |
+--------+-----+-------+-----+------+---------------+----------------------------------------------------+--------+

This can be created with the following SQL (see bottom of this file):

    create table CourseReview (dept text, crnum integer, qtr integer, year integer, instructor text, review text, rating integer);

"""

import sqlite3
from .Model import Model

# file for the database
DB_FILE = 'entries.db'


class model(Model):
    def __init__(self):
        # Make sure our database exists
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        try:
            cursor.execute("select count(rowid) from CourseReview")
        except sqlite3.OperationalError:
            cursor.execute(
                "CREATE TABLE CourseReview (author text, dept text, crnum integer, qtr integer, year integer, instructor text, review text, rating integer)")
        cursor.close()

    def select(self):
        """
        Gets all rows from the database
        Each row contains: author, dept, crnum, qtr, year, instructor, review, rating
        :return: List of lists containing all rows of database
        """
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM CourseReview")
        return cursor.fetchall()

    def insert(self, author, dept, crnum, qtr, year, instructor, review, rating):
        """
        Inserts entry into database
        :param author: String
        :param dept: String
        :param crnum: Integer
        :param qtr: String
        :param year: Integer
        :param instructor: String
        :param review: String
        :param rating: Integer
        :return: True
        :raises: Database errors on connection and insertion
        """
        params = {'author': author, 'dept': dept, 'crnum': crnum, 'qtr': qtr, 'year': year,
                  'instructor': instructor, 'review': review, 'rating': rating}

        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("INSERT INTO CourseReview (author, dept, crnum, qtr, year, instructor, review, rating) Values (:author, :dept, :crnum, :qtr, :year, :instructor, :review, :rating)", params)
        connection.commit()
        cursor.close()

        return True
