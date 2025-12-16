# Personal finance app
# Mini project - Expense Tracker

expenselist = [] #list of all expenses in form of dictionary
print("Welcome to Expense Tracker : Kharcha kam kiya karo :)")

while True:
    print("===MENU===")
    print("1. Add Expenses")
    print("2. View All Expenses ")
    print("3. View total Kharcha")
    print("4. Exit")

    choice = int(input("Please enter your choice : "))

    if(choice == 1):
        #Add Expenses
        date = input("Enter the date when you spend your money : ")
        categeory = input("Enter the categories of spending money(like, Food, Travel, Makeup, Books) : ")
        description =input("Enter short description : ")
        amount = float(input("Enter the Amount : "))

        expense= {
            "date":date,
            "categeory":categeory,
            "description":description,
            "amount":amount
        }

        expenselist.append(expense)
        print("DONE Bro! Expenses Added Successfully :)")

    elif(choice == 2):
        # iew all expenses
        if (len(expenselist)==0):
            print("No Expenses Added, Go and Update the list firsttt")
        else:
            print("=== Here is you Total Expenses ===")
            count = 1
            for eachKharcha in expenselist:
                print(f"{count} -> {eachKharcha["date"]},{eachKharcha["categeory"]},{eachKharcha["description"]},{eachKharcha["amount"]}")
                count+=1
    elif(choice == 3):
        # Total kharcha
        total = 0
        for eachkharcha in expenselist:
            total = total + eachkharcha["amount"]

        print("\n TOTAL KHARCHA = ",total)

    elif(choice == 4):
        # EXIT
        print("Thank you for using our system")
        break

    else:
        print("Invalid Choice, Try Again :(")
        

 