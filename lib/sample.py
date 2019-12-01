
person = input("type 1 to create or type 2 to search ")
if person == '1':
    name = input("Add contact's name: ")
    phone = input("what is their phone number? ")
    email = input("email: ")
    new_year = int(input('Please enter the birth year: '))
    new_month = int(input('Please enter the birth month (number): '))
    new_day = int(input('Please enter the birth day: '))
    new_person = contact(name=name, phone_number=phone, email=email, birthday=date(new_year, new_month, new_day))
    new_person.save()  # new person is stored in the db
    print("")
    print("")
    print(f"Looks like you and {new_person.name} really connected!")
    print(new_person.name)
    print(f"{new_person.phone_number}")
    print(new_person.email)
    print(f"{new_person.birthday}")
    print("")
    print("")
if person == '2':
    find = input("search by name: ")
    output = contact.select().where(contact.name == find).get()
    print(output.name)
    print(output.phone_number)
    print(output.birthday)
else:
    print("Please come back when you're ready to add more contacts!")