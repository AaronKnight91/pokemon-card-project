import sqlite3

class CardDatabase():

    def __init__(self, database):

        self.database = database
        self.create_connection()

    def create_connection(self):

        self._conn = sqlite3.connect(self.database)
        self._cur = self._conn.cursor()

    def create_test_db(self):

        self._cur.execute('''CREATE TABLE IF NOT EXISTS deck_info
                             (year_released date,
                              series_name text,
                              num_cards integer)''')


if __name__ == "__main__":

    db = CardDatabase("test.db")
    db.create_test_db()
