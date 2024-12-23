from abc import ABC, abstractmethod
from Models.DBSluice import DataBaseSluice as dbs
from typing import Protocol


class CRUD(ABC):
    def __init__(self,db_path):
        self.db = dbs(db_name=db_path)

    async def delete(self,table_name:str,conditions:dict):
        """ Write the conditions in sql
            To delete everything write ! in conditions variable"""
        if conditions=="":
            return -1
        elif conditions=="!":
            conditions=""
        sql = (f"DELETE FROM {table_name}"
               f"WHERE {conditions}")
        
        await self.db.execute(sql)
        return 1

    async def create(self,table_name:str,column_value_dict:dict):
        values_parsed = ''
        columns_names_parsed = ''
        try:
            for column_name in column_value_dict:
                print(column_name)
                values_parsed += "'"+str(column_value_dict[column_name]) + "', "
                columns_names_parsed += str(column_name) + ', '
            values_parsed = values_parsed[:-2]
            columns_names_parsed = columns_names_parsed[:-2]
        except IndexError:
            return -1
        print(values_parsed,columns_names_parsed,table_name)
        sql = (f"INSERT INTO {table_name} ({columns_names_parsed}) "
               f"VALUES ({values_parsed})")
        print(sql)
        await self.db.execute(sql)
        return 1

    async def read(self,table_name:str,columns_names:list[str],conditions:str|None):
        """ Write the conditions in sql
            To select everything write * in columns_names variable"""
        columns_names_parsed = ''
        for column_name in range(len(columns_names)):
            columns_names_parsed += str(columns_names[column_name]) + ','
        columns_names_parsed = columns_names_parsed[:-1]
        print(len(columns_names),columns_names[0])
        if len(columns_names)==1 and columns_names[0]=="*":
            sql = (f"SELECT * "
                   f"FROM {table_name} " + (f"WHERE{conditions}" if conditions is not None else f""))
        else:
            sql = (f"SELECT ({columns_names_parsed}) "
                   f"FROM {table_name} " + (f"WHERE{conditions}" if conditions is not None else f""))
        print(sql)
        await self.db.execute(sql)
        res=await self.db.fetch_changes('all')
        print(res)
        return res

    async def update(self,table_name:str,value_column_dict:dict,conditions:str):
        """ Write the conditions in sql
            To update everything write ! in conditions variable"""
        if conditions=="":
            return -1
        elif conditions=="!":
            conditions=""
        value_column_string=''
        try:
            for column_name in value_column_dict:
                value_column_string+=str(column_name)+'='+str(value_column_dict[column_name])+','
        except IndexError:
            return -1
        value_column_string = value_column_string[:-1]
        sql=(f"UPDATE {table_name}"
             f"SET{value_column_string}"
             f"WHERE{conditions}")
        await self.db.execute(sql)
        return 1

    async def finish_transaction(self):
        await self.db.close()