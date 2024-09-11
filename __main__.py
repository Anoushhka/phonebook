from phone import ContactDetails

def menu():
    print("Choose any action from given list")
    print("_"*20)
    print("1. Add Contact Details")
    print("2. List Contact")
    print("3. Delete Contact Details")
    print("4. Update Contact Details")
    print("5.Exit")
    print("_"*20)


if __name__ == "__main__" :
    print("Do, you want to continue y\n:")
    # user_choice = input("Enter your choice")
    # while user_choice == "y" or user_choice == "Y":

    menu()
    choice = int(input("please Enter your choice:"))
    if choice == 1:
        c1 = ContactDetails()
        c1. add_contact() # contact details lai aba file ma gayera write csv file ma
    
    if choice == 2:
        c = ContactDetails()
        c.read_Contacts()


    if choice == 3:
        c = ContactDetails()
        c.delete_contact()

    if choice == 4:
        c = ContactDetails()
        c.update_contact()

    if choice == 5:
        exit(1)

