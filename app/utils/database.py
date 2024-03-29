import sqlite3


class Database:

    def __init__(self):
        self._conn = sqlite3.connect("GAb_DB.db")
        self._cursor = self._conn.cursor()

        self.query("""CREATE TABLE IF NOT EXISTS platforms(
        user_id INTEGER NOT NULL PRIMARY KEY,
        user_platforms TEXT);
        """)

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()

    @property
    def connection(self):
        return self._conn

    @property
    def cursor(self):
        return self._cursor

    def commit(self):
        self.connection.commit()

    def close(self, commit=True):
        if commit:
            self.commit()
        self.connection.close()

    def execute(self, sql, params=None):
        self.cursor.execute(sql, params or ())

    def fetchall(self):
        return self.cursor.fetchall()

    def fetchone(self):
        return self.cursor.fetchone()

    def query(self, sql, params=None):
        self.cursor.execute(sql, params or ())
        return self.fetchall()
