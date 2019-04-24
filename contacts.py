def welcomeMessage():
    """
    Displays initial welcome messages
    """
    print(
        '\n"Intelligence is the ability to avoid doing work, yet getting the work done."'
    )
    print("\t\t\t\t\t\t - Linux Torvalds\n")
    print("Welcome to the text-based Contact Application!\n")
    print("There are various operations that may be performed: ")

    ## TODO: update this wich each function command created
    print("about, info, list, remove, load, save, exit.\n")


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

    def editNote(self, new):
        # Assign the value of this instance's note to whatever is passed as new
        self.note = new


# # TODO: need number of companies & contacts per company
def info(contactList):
    """
        Information about contact list: number of contacts, companies & contacts per company
    """
    numberofContacts = 0
    # numberofCompanies = 0
    # numberofContactsperCompany = 0

    for contacts in contactList:
        numberofContacts += 1

    print("The total number of contacts: " + str(numberofContacts - 1))


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
    # Error check if name dne
    ## TODO: Fist name on list will throw warning ?
    if contact.name != name:
        print("❌ WARNING ❌")
        print("Contact does not exist.")
        print("Please check contact list and return with valid name.\n")


def loadContacts(contactList):
    """Read info from csv file"""
    # List of dictionaries
    data = []
    try:
        with open("sample.csv", "r") as f:
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
        print('File "{}" not found.'.format("sample.csv"))
        print("Please enter a valid file name. ")


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
        cmd = input("Please enter a command: ")
        print("\n")

        if cmd == "about":
            about()

        if cmd == "info":
            info(contactList)

        if cmd == "list":
            list(contactList)

        if cmd == "remove":
            name = input("Enter the name for which you would like removed: ")
            remove(contactList, name)

        if cmd == "save":
            save(contactList)

        if cmd == "exit":
            print("Always update your contact list !")
            print("Goodbye.\n")
            return -1


if __name__ == "__main__":
    main()
