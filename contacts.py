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


def main():
    """
    Function Calls
    """

    welcomeMessage()

    while(1):
        cmd = input('Please enter a command: ')

        if(cmd == 'about'):
            about()

        if(cmd == 'exit'):
            print('Goodbye\n')
            return -1


if __name__ == "__main__":
    main()
