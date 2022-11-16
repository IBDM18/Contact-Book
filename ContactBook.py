import sys
def contactbook():
    a, b = int(input("\tEnter The Number Of Contacts You Want To Add: ")), 5
    book = []
    print(book)
    for i in range(a):
        print("Enter Contact %d Details: " % (i + 1))
        temp = []
        for j in range(b):
            if j == 0:
                temp.append(str(input("Enter User Name: ")))
                if temp[j] == '' or temp[j] == ' ':
                    sys.exit("Name Is Mandatory, Please Don't Leave It Empty.")
            if j == 1:
                temp.append(int(input("Enter User Number: ")))
            if j == 2:
                temp.append(str(input("Enter User's Date Of Birth - dd/mm/yyyy: ")))
                if temp[j] == '' or temp[j] == ' ':
                    temp[j] = None
            if j == 3:
                temp.append(str(input("Enter Category (Friend/Family/Work/Others): ")))
                if temp[j] == '' or temp[j] == ' ':
                    temp[j] = None
        book.append(temp)
    print(book)
    return book

def menu():
    print("----------------------------------------------------")
    print("\t\t\t PHONE DIRECTORY", flush = False)
    print()
    print("Enter The Operation To Perform: ")
    print()
    print("1. Add A New Contact.")
    print("2. Remove A Contact.")
    print("3. Delete All Contact.")
    print("4. Search For A Contact.")
    print("5. Display All Contact.")
    print("6. Exit Phone Directory.")
    print()
    choice = int(input("Enter Your Choice: "))
    print()
    return choice

def add(ph):
    dip = []
    for i in range(len(ph[0])):
        if i == 0:
            dip.append(str(input("Enter User Name: ")))
        if i == 1:
            dip.append(int(input("Enter User Phone Number: ")))
        if i == 2:
            dip.append(str(input("Enter User Date Of Birth (dd/mm/yyyy): ")))
        if i == 3:
            dip.append(str(input("Enter Category (Firend/Family/Work/Other): ")))
    ph.append(dip)
    return ph

def remove(ph):
    query = str(input("Please Enter The User Name You Want To Remove: "))
    temp = 0
    for i in range(len(ph)):
        if query == ph[i][0]:
            temp += 1
            print(ph.pop(i))
            print("This Query Has Been Removed.")
            return ph
        if temp == 0:
            print("Sorry You've Entered Invalid Query!")
            return ph

def delete(ph):
    return ph.clear()

def search(ph):
    choice = int(input("Enter Search Criteria: \n\n\t1. Name \n\t2. Number \n\t3. DOB \n\t4. Category(Firend/Family/Work/Others) \n\tPlease Enter Your Choice: "))
    temp = []
    check = -1
    if choice == 1:
        query = str(input("Enter User Name To Search: "))
        for i in range(len(ph)):
            if query == ph[i][0]:
                check = i
                temp.append(ph[i])
    elif choice == 2:
        query = int(input("Enter Phone Number To Search: "))
        for i in range(len(ph)):
            if query == ph[i][1]:
                check = i
                temp.append(ph[i])
    elif choice == 3:
        query = str(input("Enter The DOB of The User To Search: "))
        for i in range(len(ph)):
            if query == ph[i][2]:
                check = i
                temp.append(ph[i])
    elif choice == 4:
        query = str(input("Enter The Category Of The User To Search: "))
        for i in range(len(ph)):
            if query == ph[i][3]:
                check = i
                temp.append(ph[i])
    else:
        print("Invalid Search Criteria.")
        return -1
    if check == -1:
        return -1
    else:
        display(temp)
        return check

def display(ph):
    if not ph:
        print("List Is Empty []")
    else:
        for i in range(len(ph)):
            print(ph[i])

def thanks():
    print("\n")
    print("\t Thank You For Visiting Our Phone Directory.")
    print("\t Please Do Visit Again!")
    print("\n")
    sys.exit("Have A Nice Day!")
print("\n")
print("\tHello User, Welcome To Our Phone Directory.")
print("----------------------------------------------------")
print("\tYou May Now Proceed To Explore This Directory.")
print("----------------------------------------------------")
choice = 1
ph = contactbook()
while choice in(1, 2, 3, 4, 5):
    choice = menu()
    if choice == 1:
        ph = add(ph)
    elif choice == 2:
        ph = remove(ph)
    elif choice == 3:
        ph = delete(ph)
    elif choice == 4:
        d = search(ph)
        if d == -1:
            print("The Contact Does Not Exist, Please Try Again Later!")
    elif choice == 5:
        display(ph)
    else:
        thanks()






