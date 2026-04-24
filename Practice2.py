phonebook ={}

def add_record():
    call_id = input("Enter call id:")
    if call_id in phonebook:
        print("Invalid id")
        return
    if call_id == "":
        print("Call ID canot be empty")
        return
    
    name = input("Enter name:")
    
    if name == "":
        print("Name cannot be empty")
        return
    
    contact = input("Enter contact number:")
    if contact in phonebook:
        print("Contact already exists")
        return
    
    phonebook[call_id]={
        "ID" : call_id,
        "Name": name,
        "contact" : contact
    }
    print("Record added succesfully")

def search_record():
    call_id = input("Enter name to search:")

    if name not in phonebook:
        print("not found")
        return
    details = phonebook[name]
    for key in details:
        print(key, ":", details[key])    

def delete_record():
    call_id = input("Enter id to delete:")
    if call_id not in phonebook:
        print("Not found")
        return
    
    confirm = input("Are you sure you want to delete? (y/n):")
    if confirm == "y":
        del phonebook[call_id]
        print("Deleted succesfully")
    else:
        print("Cancelled")

def update_record():
    call_id = input("Enter id to update:")
    if call_id not in phonebook:
        print("Not found")
        return
    
    newname = input("Enter new name:")
    newcontact = input("Enter new contact:")

    details = phonebook[call_id]
    details["Name"] = newname
    details["Contact"] = newcontact

    print("Updated succesfullly")

def display_record():
    if phonebook =={}:
        print("Nothing to display")
        return
    
    for call_id in phonebook:
        details = phonebook[call_id]
        for key in details:
            print(key,":", details[key])
while True:
    print("1.Add record")
    print("2.Update record")
    print("3.Delete record")
    print("4.Search record")
    print("5.Display record")
    print("5.Exit")

    ch = input("Enter your choice:")

    if ch == "1":
        add_record()
    elif ch == "2":
        update_record()
    elif ch == "3":
        delete_record()
    elif ch == "4":
        search_record()
    elif ch == "5":
        display_record()
    elif ch == "6":
        break
    else:
        print("Invalid choice")
