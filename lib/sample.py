# from peewee import *
# from datetime import date

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
    # phone number should be a character field, error was getting thrown as integer field and confusing with date
    phone = input("what is their phone number? ")
    email = input("email: ")
    # date input below is always year, date, month in that order 
    new_year = int(input('Please enter the birth year: '))
    new_month = int(input('Please enter the birth month (number): '))
    new_day = int(input('Please enter the birth day: '))
    # new person contact below is how it is created with date in parenthesis
    new_person = contact(name=name, phone_number=phone, email=email, birthday=date(new_year, new_month, new_day))
    # new person is stored in the db
    new_person.save() 
    # Use prints below for space in between so it looks better aestetically
    print("")
    print(f"Looks like you and {new_person.name} really connected!")
    print(new_person.name)
    print(f"{new_person.phone_number}")
    print(new_person.email)
    print(f"{new_person.birthday}")
    print("")
    # below is logic on if person chose to search contact
if person == '2':
    find = input("search by name: ")
    # below is how to do a get request to find a person
    output = contact.select().where(contact.name == find).get()
    print(output.name)
    print(output.phone_number)
    print(output.birthday)
else:
    print("Please come back when you're ready to add more contacts!")