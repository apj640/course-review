class Model():
    def select(self):
        """
        Gets all entries from the database
        :return: Tuple containing all rows of database
        """
        pass

    def insert(self, author, dept, crnum, qtr, year, instructor, review, rating):
        """
        Inserts entry into database
        :param author: String
        :param dept: String
        :param crnum: Integer
        :param qtr: Integer
        :param year: Integer
        :param instructor: String
        :param review: String
        :param rating: Integer
        :return: none
        :raises: Database errors on connection and insertion
        """
        pass
