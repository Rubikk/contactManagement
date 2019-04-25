## TODO: Command & Note func -- Error check: break when file name is not found


def welcomeMessage():
    """
    Displays initial welcome messages
    """
    print(
        '\n"Intelligence is the ability to avoid doing work, yet getting the work done."'
    )
    print("\t\t\t\t\t\t - Linux Torvalds\n")
    print("Welcome to the text-based Contact Application!\n")


def about():
    """Simple about me"""
    print("Contacts App.\nDeveloped by: Iseah Olguin\n")


class Contact:
    """Stores contact Information"""

    def __init__(self, name, phone, company, email, note):

        # initial name
        self.name = name
        self.phone = phone
        self.company = company
        self.email = email
        # initial note
        self.note = note

    def listInfo(self):
        """Pretty prints the contact list"""
        print("Name: ", self.name)
        print("Phone: ", self.phone)
        print("Company: ", self.company)
        print("Email: ", self.email)
        print("Note: ", self.note)

    def editNote(self, newNote):
        # Assign the value of this instance's note to whatever is passed as new
        self.note = newNote


def info(contactList):
    """
        Information about contact list: number of contacts, companies & contacts per company
    """
    numberofContacts = 0

    for contact in contactList:
        numberofContacts += 1
        contact.companyInfo()

    print("The total number of contacts: " + str(numberofContacts - 1))
    print("\n")


def list(contactList):
    """List the infromation of the entire contact list"""
    for contact in contactList:
        contact.listInfo()


def remove(contactList, name):
    """Removes contact by name from contact list"""
    for i, contact in enumerate(contactList):
        if contact.name == name:
            # Delete name from contact list
            del contactList[i]
            print("Contact Successfully Removed 🔫 !")
            return
    # Error check if name dne
    if contact.name != name:
        print("❌ Error")
        print("Contact does not exist.")
        print("Please check contact list and return with valid name.\n")


def note(contactList, name):
    """Review Current Note or Edit existing Note"""
    print("Would you like to view or edit the existing note? ")
    answer = input("Type 'view' or 'edit': ")
    # User just wants to view the existing note
    if answer == "view":
        # Go through list searching for name
        for contact in contactList:
            if name == contact.name:
                # Print the note associated with name
                print("\nCurrent Note: ")
                print(contact.note)
                print()

    elif answer == "edit":
        myContact = Contact()
        newNote = input("Create your new note: ")
        myContact.editNote(newNote)
        # Print the new note
        print("\nNew Note: ")
        print(myContact.note)
        print()
        return


def add():
    """Add a new contact to the contact list"""
    print("⚠️  Warning: ")
    print("⚠️  Do not leave any of the following fields empty. \n")

    # Prompts for each field of contact
    # Error check to ensure each field is non-empty string
    # Save method parsing requires each field to be non-empty
    name = input("Name: ")
    if len(name) <= 0:
        print("❌ Error")
        print("Field is empty.\nExiting.")
        return -1
    # Name must not contain numbers
    elif name.isnumeric() == True:
        print("❌ Error")
        print("Name must not contain numbers, ONLY letters.")
        print("Exiting.")
        return -1

    phone = input("Phone: ")
    if len(phone) <= 0:
        print("❌ Error")
        print("Field is empty.\nExiting.")
        return -1

    company = input("Company: ")
    if len(company) <= 0:
        print("❌ Error")
        print("Field is empty.\nExiting.")
        return -1

    email = input("Email: ")
    if len(email) <= 0:
        print("❌ Error")
        print("Field is empty.\nExiting.")
        return -1

    note = input("Note: ")
    if len(note) <= 0:
        print("❌ Error")
        print("Field is empty.\nExiting.")
        return -1

    # New contact instance
    contact = Contact(name, phone, company, email, note)
    return contact


def loadContacts(contactList):
    """Read info from csv file"""
    # List of dictionaries
    data = []
    try:
        fileIn = input("Please enter a file to be loaded immediately: ")
        with open(fileIn, "r") as f:
            lines = f.readlines()

        for line in lines:
            values = line.split(",")

            # Creates an empty dictionary
            row = dict()

            name = row["Name"] = values[0]
            phone = row["Phone"] = values[1]
            company = row["Company"] = values[2]
            email = row["Email"] = values[3]
            note = row["Note"] = values[4]
            data.append(row)

            # new instance of contact
            contact = Contact(name, phone, company, email, note)
            # store as list
            contactList.append(contact)

    except FileNotFoundError:
        print('\nFile "{}" not found.'.format(fileIn))
        print("Please enter a valid file name.")
        print("And ensure the file is within the current working directory.\n")
        return


def save(contactList):
    """Saves contactList to a file in CSV format"""

    print(
        "Note: This file will be saved in comma separated format, please mark your file as a '.csv' "
    )
    savefile = input(
        "Please enter the filename in which you would like to save your file: "
    )
    with open(savefile, "w") as file:
        for contact in contactList:
            file.write(contact.name + ",")
            file.write(contact.phone + ",")
            file.write(contact.company + ",")
            file.write(contact.email + ",")
            file.write(contact.note)


def main():
    """
    Function Calls
    """

    welcomeMessage()
    contactList = []
    # Load a default contacts file when app starts
    loadContacts(contactList)

    while 1:
        print("There are various operations that may be performed: ")

        ## TODO: update this wich each function command created
        print("about, info, list, remove, note, add, load, save, exit.\n")
        cmd = input("Please enter a command: ")

        if cmd == "about":
            about()

        if cmd == "info":
            info(contactList)

        if cmd == "list":
            list(contactList)

        if cmd == "remove":
            name = input("Enter the name for which you would like removed: ")
            remove(contactList, name)

        if cmd == "note":
            name = input(
                "Enter a name for which you would like to view/edit their note: "
            )
            note(contactList, name)

        if cmd == "add":
            contact = add()
            contactList.append(contact)

        if cmd == "load":
            loadContacts(contactList)

        if cmd == "save":
            save(contactList)

        if cmd == "exit":
            print("Always update your contact list !")
            print("Goodbye.\n")
            return -1


if __name__ == "__main__":
    main()
