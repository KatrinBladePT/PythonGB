import os

def show_contacts(file_name):
    os.system('CLS')
    with open(file_name, 'r') as file:
        data = file.readlines()
        
        for contact in data:
            print(contact)
    
    input("Press any key to continue...")        
                       
def add_contacts(file_name):
    os.system('CLS')
    with open(file_name, 'a') as file:
        res = ""
        res += input("Enter surname contact:") + " "
        res += input("Enter name contact:") + " "
        res += input("Enter phone number of contact:")

        file.write(res)
        
    input("Press any key to continue...")

def search_contacts(file_name):
    os.system('CLS')
    target = input("Input a name of contact for searching:")
    
    with open(file_name, 'r') as file:
        data = file.read()
        
        if target in data:
            for contact in data:
                if target in contact:
                    print(contact)
                    break
        else :
            print("No contact found")
            
    input("Press any key to continue...")

def drawing():
    print("1 - show contacts")
    print("2 - add contacts")
    print("3 - search contacts")
    print("4 - exit")

def main(file_name):
    while True:
        os.system('CLS')
        drawing()
        user_choice = int(input("Input a number from 1 to 4"))

        if user_choice == 1:
            show_contacts(file_name)
        elif user_choice == 2:
            add_contacts(file_name)
        elif user_choice == 3:
            search_contacts(file_name)
        elif user_choice == 4:
            print("GGWP guys")
            return
        
                