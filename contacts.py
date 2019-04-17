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
    print("about, exit.")


def about():
    """Simple about me"""
    print("Contacts App.\nDeveloped by: Iseah Olguin\n")


def read():
    """Read info from csv file"""
    # List of dictionaries
    data = []

    with open("sample.csv", 'r') as f:
        lines = f.readlines()

    for line in lines:
        values = line.split(',')

        # Creates an empty dictionary
        row = dict()

        row["Name"] = values[0]
        row["Phone"] = values[1]
        row["Company"] = values[2]
        row["Email"] = values[3]
        # List index out of range for some reason
        # row["Note"] = values[4]
        data.append(row)

    print(row)


def main():
    """
    Function Calls
    """

    welcomeMessage()

    while(1):
        cmd = input('Please enter a command: ')

        if(cmd == 'about'):
            about()

        if(cmd == 'read'):
            read()

        if(cmd == 'exit'):
            print('Goodbye\n')
            return -1


if __name__ == "__main__":
    main()
