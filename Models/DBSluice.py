import sqlite3


class DataBaseSluice:
    def __init__(self,db_name):
        self.db_name = db_name
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()

    async def execute(self,command):
        self.cursor.execute(command)
        self.connection.commit()

    async def fetch_changes(self,rows:str):
        if rows=="all":
            return self.cursor.fetchall()
        else:
            try:
                return self.cursor.fetchmany(int(rows))
            except TypeError:
                return -1

    async def close(self):
        self.connection.close()
