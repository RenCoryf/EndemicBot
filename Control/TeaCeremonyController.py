from Models.tea_ceremony_class import TeaCeremony as TC
from Data.db_data import db_path


async def create_ceremony(participant_number,begin_time,date,comment,customer_id,tea_master):
        tc=TC(db_path)
        data=[participant_number,begin_time,date,comment,customer_id,tea_master]
        await tc.book_ceremony(data)
