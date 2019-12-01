from peewee import *
from datetime import date

db = PostgresqlDatabase('rolodex', user='postgres', password='',
                        host='localhost', port=5432)

db.connect()

class BaseModel(Model):
    """A base model that will use our Postgresql database. We don't have to do
    this, but it makes connecting models to our database a lot easier."""
    class Meta:
        database = db


class contact(BaseModel):
    name = CharField()
    phone_number = CharField()
    email = CharField()
    birthday = DateField()


# Create tables
# db.drop_tables([contact])
db.create_tables([contact])


