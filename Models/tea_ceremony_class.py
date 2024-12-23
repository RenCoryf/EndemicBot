from Models.DBSluice import DataBaseSluice as dbs
from Data.db_data import db_path
from Models.CRUD import CRUD


class TeaCeremony(CRUD):

    async def book_ceremony(self,value_column_dict:dict):

        await self.create(table_name="TeaCeremony",value_column_dict=value_column_dict)

    async def cancel_ceremony(self):
        db = dbs(db_name=db_path)
        sql = f"DELETE FROM TeaCeremonies WHERE ceremony_id='{ceremony_id}'"
        await db.execute(sql)
        await db.close()
