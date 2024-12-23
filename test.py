from Models.CRUD import CRUD
import asyncio


class cruder(CRUD):
    async def test(self,num):
        col_value_dict={"name":"Pavel",
                        "email":"kurwa@gmail.com",
                        "phone":123}
        print(await self.delete(table_name="Customers",conditions="name = Yarik"))
        print(await self.read("Customers",columns_names=["*"],conditions=None))
        await self.finish_transaction()

async def lol():
    c=cruder("/home/rencoryf/PycharmProjects/EndemicBot/DataBase/Endemic.db")
    await c.test(1)

def run_async_function(coroutine):
    asyncio.run(coroutine)

run_async_function(lol())