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

# create base model class 
class contact(BaseModel):
    name = CharField()
    phone_number = CharField()
    email = CharField()
    birthday = DateField()


# Create tables
# db.drop_tables([contact])
db.create_tables([contact])

# create input logic to where people can start adding
person = input("type 1 to create or type 2 to search ")
# if statement for when a person chooses to add. Below add input value for defined fields above.
if person == '1':
    name = input("Add contact's name: ")
    phone = input("what is their phone number? ")
    email = input("email: ")
    new_year = int(input('Please enter the birth year: '))
    new_month = int(input('Please enter the birth month (number): '))
    new_day = int(input('Please enter the birth day: '))