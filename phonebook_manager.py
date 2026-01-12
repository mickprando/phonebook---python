phonebook = []  # main list storing all contacts

def add_contact(first_name, last_name, phone_number):       # create a dictionary representing a single contact in the function
    contact = {"first_name": first_name, "last_name": last_name, "phone_number": phone_number}
    return contact                                          # returns the contact

def search_contact(phonebook):                              # asks the user what to search (first name or last name)
    query = input("Search by first name or last name: ")    # loops through all saved contacts
    for c in phonebook:                                     # compares the search string with the contact's first or last name
        if query == c["first_name"] or query == c["last_name"]:
            print("Contact found:", c)
            return c                                        # returns the found contact and stops the function      
    print("No matchng contact found")
    return None                                             # explicit return when nothing is found

def show_contacts(phonebook):                               # if the phonebook is empty, notify the user and stop
    if not phonebook:
        print("The phonebook is empty")
        return             
    for i, c in enumerate(phonebook, start=1):              # enumerate gives a counter starting from 1 together with each contact
        print(i, c)                                         # prints index and contact dictionary

def count_contacts(phonebook):
    return len(phonebook)                                   # returns the total number of saved contacts


while True:                                                 # main program loop: shows the menu until the user chooses to exit
    print("Phonebook Menu")
    print("1. Add contact") 
    print("2. Search contact") 
    print("3. Show all contacts") 
    print("4. Count contacts") 
    print("5. Exit")

    choice = input("Choose an option: ")                    # reads the user's choice as a string

    if choice == "1":                                       # data collection for a new contact
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        phone_number = input("Enter phone number: ")
        contact = add_contact(first_name, last_name, phone_number)   # creates the contact dictionary using the function
        phonebook.append(contact)                           # adds the contact to the phonebook list

    elif choice == "2":                                     # executes the search function
        search_contact(phonebook)

    elif choice == "3":                                     # prints all contacts with numbering
        show_contacts(phonebook)

    elif choice == "4":                                     # calculates and prints the total number of contacts
        total = count_contacts(phonebook)
        print("Total numbr of contacts:", total)

    elif choice == "5":                                     # exit message and break from the loop
        print("Closing program")
        break

    else:                                                   # executed if the user enters an invalid option
        print("Invalid choice, try again")
