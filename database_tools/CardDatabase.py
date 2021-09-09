import sqlite3

class CardDatabase():

    def __init__(self, database):

        self.database = database
        self.create_connection()

    def create_connection(self):

        self._conn = sqlite3.connect(self.database)
        self._cur = self._conn.cursor()

    def create_deck_info_db(self):

        self._cur.execute('''CREATE TABLE IF NOT EXISTS deck_info
                             (year_released date,
                              series_name text,
                              num_cards integer)''')

    def create_series_info_db(self, name_of_series):

        name_of_series = self.clean_text(name_of_series)
        
        self._cur.execute('''CREATE TABLE IF NOT EXISTS %s
                             (number integer,
                              pokemon text,
                              card_type text,
                              owned text)''' % name_of_series)

    def clean_text(self, text):

        text = text.replace(" ", "_").lower()
        return text

if __name__ == "__main__":

    db = CardDatabase("test.db")
    db.create_deck_info_db()
    db.create_series_info_db("TEST DB")
