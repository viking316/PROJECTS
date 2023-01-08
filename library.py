def main_menu():
    print("WELCOME TO LIBRARY")
    print("What would you like to do?")
    option=int(input("1. New user \n 2. Existing user "))
    

# choosing algo:
    if option == 1:
        new_user()
    if option == 2:
        old_user()
    else:
        print("please choose a correct value")
        main_menu()


#new user manager: 
def new_user():
    print("New user\n")


    a=(input("Username: "))
    uupath="C:/CHANDU/n00b/Librarymanager/useruname.txt"
    with open(uupath,"r") as reader:
         reading=reader.read()
         for i in reading:
            if a in i:
                print("username already exists!\n")
                main_menu()


    b=(input("Password: "))
    b2=input("re-enteryour Password: ")
    if b != b2:
        print("Passwords do not match.\n")
        new_user()

    # uppath="C:/CHANDU/n00b/Librarymanager/userpass.txt"
    with open("useruname.txt","a") as useruname:
        useruname.write(a+"\n")
    with open("userpass.txt","a") as userpass:
        userpass.write(b + "\n")
    print("user created!")


    main_menu()

# old user manager:
def old_user():

    print("Old User\n")


    a=input("Username: ")
    
    uupath="C:/CHANDU/n00b/Librarymanager/useruname.txt"

    with open(uupath,"r") as reader_a:
        reading_a=reader_a.read()

    if a not in reading_a:
        print("User does not exist!")
        old_user()

    b=input("Password: ")
    uppath="C:/CHANDU/n00b/Librarymanager/userpass.txt"

    with open(uppath,"r") as reader_b:
        
        reading_b=reader_b.read()


    if b not in reading_b:
        print("Password entered is wrong!")
        old_user()
    
    library_UI()


def library_UI():
    print("at libriary UI")
    exit()




main_menu()

