def welcomeMessage():
    """
    Displays initial welcome messages
    """
    print(
        '\n"Intelligence is the ability to avoid doing work, yet getting the work done."'
    )
    print("\t\t\t\t\t\t - Linux Torvalds\n")
    print("Welcome to my text-based Contact Application!\n")


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
    numberofCompanies = 0

    for contact in contactList:
        numberofContacts += 1
        numberofCompanies += 1

    print("The total number of contacts: " + str(numberofContacts - 1))

    print("The total number of companies: " + str(numberofCompanies - 1))
    print("\n")


def list(contactList):
    """List the infromation of the entire contact list"""
    for contact in contactList:
        contact.listInfo()


def remove(contactList, name):
    """Removes contact by name from contact list"""
    if name is None:
        name = input("Enter the name for which you would like removed: ")
    for i, contact in enumerate(contactList):
        if contact.name == name:
            # Delete name from contact list
            del contactList[i]
            print("Contact Successfully Removed 🔫 !")
            return
    # Error check if name dne
    print("❌ Error")
    print("Contact does not exist.")
    print("Please check contact list and return with valid name.\n")


def noteText(contactList, name, answer, new):
    """Review Current Note or Edit existing Note"""
    if name is None:
        name = input(
            "Enter a name for which you would like to view/edit their note: ")
    if answer is None:
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
                return
        # Name does not exist
        print("❌ Error")
        print("Contact does not exist.")
        print("Please check contact list and return with valid name.\n")

    elif answer == "edit":
        for contact in contactList:
            if name == contact.name:
                if new is None:
                    new = input("Create your new note: ")
                contact.editNote(new)
                # Print the new note
                print("\nNew Note: ")
                print(new)
                print()
                return
        # Name does not exist
        print("❌ Error")
        print("Contact does not exist.")
        print("Please check contact list and return with valid name.\n")


def add(name, phone, company, email, note):
    """Add a new contact to the contact list"""
    print("⚠️  Warning: ")
    print("⚠️  Do not leave any of the following fields empty. \n")

    # Prompts for each field of contact
    # Error check to ensure each field is non-empty string
    # Save method parsing requires each field to be non-empty
    if name is None:
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
    if phone is None:
        phone = input("Phone: ")
        if len(phone) <= 10:
            print("❌ Error")
            print("Field is empty.\nExiting.")
            return -1
    if company is None:
        company = input("Company: ")
        if len(company) <= 0:
            print("❌ Error")
            print("Field is empty.\nExiting.")
            return -1
    if email is None:
        email = input("Email: ")
        if len(email) <= 0:
            print("❌ Error")
            print("Field is empty.\nExiting.")
            return -1
    if note is None:
        note = input("Note: ")
        if len(note) <= 0:
            print("❌ Error")
            print("Field is empty.\nExiting.")
            return -1

    # New contact instance
    contact = Contact(name, phone, company, email, note)
    return contact


def loadContacts(contactList, fileIn):
    """Read info from csv file"""
    # List of dictionaries
    data = []
    try:
        if fileIn is None:
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


def save(contactList, saveFile):
    """Saves contactList to a file in CSV format"""

    print(
        "Note: This file will be saved in comma separated format, please mark your file as a '.csv' "
    )
    if saveFile is None:
        saveFile = input(
            "Please enter the filename in which you would like to save your file: "
        )
    with open(saveFile, "w") as file:
        for contact in contactList:
            file.write(contact.name + ",")
            file.write(contact.phone + ",")
            file.write(contact.company + ",")
            file.write(contact.email + ",")
            file.write(contact.note)


def commands(contactList):
    """Executes a list of commands from a .txt file"""
    # Store words into a new list
    instructions = []
    try:
        fileIn = input("Which file of commands would you like to execute? ")
        with open(fileIn, "r") as f:
            for line in f:
                line = line.strip()
                instructions.append(line)
            # When you see add in the list, expect the following
            for index, i in enumerate(instructions):
                if i == "add":
                    name = instructions[index + 1]
                    phone = instructions[index + 2]
                    company = instructions[index + 3]
                    email = instructions[index + 4]
                    note = instructions[index + 5]
                    newContact = add(name, phone, company, email, note)

                    contactList.append(newContact)

                if i == "list":
                    list(contactList)

                if i == "info":
                    info(contactList)

                if i == "remove":
                    name = instructions[index + 1]
                    remove(contactList, name)

                if i == "about":
                    about()

                if i == "note":
                    answer = instructions[index + 2]
                    name = instructions[index + 1]
                    new = instructions[index + 3]
                    noteText(contactList, name, answer, new)

                if i == "load":
                    fileIn = instructions[index + 1]
                    loadContacts(contactList, fileIn)

                if i == "save":
                    saveFile = instructions[index + 1]
                    save(contactList, saveFile)

                if i == "exit":
                    exit()

    except FileNotFoundError:
        print('\nFile "{}" not found.'.format(fileIn))
        print("Please enter a valid file name.")
        print("And ensure the file is within the current working directory.\n")
        return


def main():
    """
    Function Calls
    """

    welcomeMessage()
    contactList = []
    # Load a default contacts file when app starts
    loadContacts(contactList, fileIn=None)

    while 1:
        print("There are various operations that may be performed: ")
        print("about, info, list, remove, note, add, load, save, commands, exit.\n")
        cmd = input("Please enter a command: ")

        if cmd == "about":
            about()

        if cmd == "info":
            info(contactList)

        if cmd == "list":
            list(contactList)

        if cmd == "remove":
            remove(contactList, name=None)

        if cmd == "note":
            noteText(contactList, name=None, answer=None, new=None)

        if cmd == "add":
            contact = add(name=None, phone=None,
                          company=None, email=None, note=None)
            contactList.append(contact)

        if cmd == "load":
            loadContacts(contactList, fileIn=None)

        if cmd == "save":
            save(contactList, saveFile=None)

        if cmd == "commands":
            print("⚠️  Warning: Please ensure file is in current directory. ")
            commands(contactList)

        if cmd == "exit":
            print("Always update your contact list !")
            print("Goodbye.\n")
            return -1


if __name__ == "__main__":
    main()
