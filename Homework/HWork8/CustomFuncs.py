import os

def show_contacts(file_name):
    os.system('CLS')
    with open(file_name, 'r') as file:
        contacts = file.readlines()
        
        for contact in contacts:
            print(contact, end='')
    
    input("\nPress any key to continue...")        
                       
def add_contacts(file_name):
    os.system('CLS')
    with open(file_name, 'a') as file:
        res = "\n"
        res += input("Enter surname contact:") + " "
        res += input("Enter name contact:") + " "
        res += input("Enter phone number of contact:")

        file.write(res)
        
    input("Press any key to continue...")

def search_contacts(file_name):
    os.system('CLS')
    target = input("Input a name of contact for searching:")
    
    with open(file_name, 'r') as file:
        contacts = file.readlines()
        
        for contact in contacts:
            if target in contact:
                print(contact)
                break
        else :
            print("No contact found")
            
    input("Press any key to continue...")
    
def update_contacts(file_name):
    os.system('CLS')
    contact_to_update = input("Enter the name of the contact to update:")

    with open(file_name, 'r') as file:
        lines = file.readlines()

    with open(file_name, 'w') as file:
        updated = False
        
        for line in lines:
            if contact_to_update in line:
                updated_contact = "\n"
                updated_contact += input("Enter updated surname contact:") + " "
                updated_contact += input("Enter updated name contact:") + " "
                updated_contact += input("Enter updated phone number of contact:")
                file.write(updated_contact)
                updated = True
            else:
                file.write(line)
        
        if not updated:
            print("Contact not found")

    input("Press any key to continue...")

def delete_contacts(file_name):
    os.system('CLS')
    contact_to_delete = input("Enter the name of the contact to delete:")

    with open(file_name, 'r') as file:
        lines = file.readlines()

    with open(file_name, 'w') as file:
        deleted = False
        
        for line in lines:
            if contact_to_delete in line:
                deleted = True
            else:
                file.write(line)
        
        if deleted:
            print("Contact deleted")
        else:
            print("Contact not found")

    input("Press any key to continue...")


def drawing():
    print("1 - show contacts")
    print("2 - add contacts")
    print("3 - update contacts")
    print("4 - delete contacts")
    print("5 - search contacts")
    print("6 - exit")


def main(file_name):
    while True:
        os.system('CLS')
        drawing()
        user_choice = int(input("Input a number from 1 to 4 :"))

        if user_choice == 1:
            show_contacts(file_name)
        elif user_choice == 2:
            add_contacts(file_name)
        elif user_choice == 3:
            update_contacts(file_name)
        elif user_choice == 4:
            delete_contacts(file_name)
        elif user_choice == 5:
            search_contacts(file_name)
        elif user_choice == 6:
            print("GGWP guys")
            return
        
main('book.txt')        
       

