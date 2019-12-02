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
db.drop_tables([contact])
db.create_tables([contact])

# create input logic to where people can start adding
person = input("type 1 to create or type 2 to search or type 3 to update or type 4 to delete or 5 to see all contacts ")
# if statement for when a person chooses to add. Below add input value for defined fields above.
if person == '1':
    name = input("Add contact's name: ")
    phone = input("what is their phone number? ")
    email = input("email: ")
    new_year = int(input('Please enter the birth year: '))
    new_month = int(input('Please enter the birth month (number): '))
    new_day = int(input('Please enter the birth day: '))
    new_person = contact(name=name, phone_number=phone, email=email, birthday=date(new_year, new_month, new_day))
    new_person.save()
    print("")
    print(f"Looks like you and {new_person.name} really connected!")
    print(new_person.name)
    print(f"{new_person.phone_number}")
    print(new_person.email)
    print(f"{new_person.birthday}")
    print("")
if person == '2':
    find = input("search by name: ")
    output = contact.select().where(contact.name == find).get()
    print(output.name)
    print(output.phone_number)
    print(output.birthday)
if person == '3':
    find = input("search by name: ")
    output = contact.select().where(contact.name == find).get()
    print("")
    print(output.name)
    print(output.phone_number)
    print(output.email)
    print(output.birthday)
    name = input("Updated name is: ")
    phone = input("Updated phone is: ")
    email = input("Updated email is: ")
    query = contact.update(name=name, phone_number=phone, email=email).where(contact.name == find)
    n = query.execute()
    print('# of rows updated: {}'.format(n))
if person == '4':
    find = input("search by name: ")
    gone = contact.select().where(contact.name == find).get()
    gone.delete_instance()
    print("Contact has been deleted")  
if person == '5':
    amount = contact.select()
    for person in amount:
        print('{}'.format(person.name))
else:
    print("Please come back when you're ready to add more contacts!")


    