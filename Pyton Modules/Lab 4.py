while(True):
    userId=input("set ID number: ")
    userPassword=input("set password: ")
    login1=input("Enter ID number:")
    login2=input("Enter password:")
    account=100
    while(login1!=userId and login2!=userPassword):
        print("Incorect password try again")
        login1=input("Enter ID number:")
        login2=input("Enter password:")
    while(login1==userId and login2==userPassword):
        selection=input("Choose withdrawl, deposit, balance check, or logout: ")
        if(selection=="balance check"):
            print(account)
            transaction=input("Would you like to make another transaction? Yes or No: ")
            if(transaction=="no"):
                print("Transaction Complete!")
            else:
                print(selection)
        elif(selection=="deposit"):
            moreMoney=int(input("Enter amount you want to add to your account: "))
            if(moreMoney<0 or account<0):
                print("Incorrect amount")
            else:
                account=account+moreMoney
                print(account)
                transaction=input("Would you like to make another transaction? Yes or No: ")
                if(transaction=="no"):
                    print("Transaction Complete!")
        elif(selection=="withdrawl"):
            lessMoney=int(input("Enter amount you want to take out of your account: "))
            if(lessMoney<0 or account<0):
                print("Incorrect amount")
            else:
                account=account-lessMoney
                print(account)
                transaction=input("Would you like to make another transaction? Yes or No: ")
                if(transaction=="no"):
                    print("Transaction Complete!")
        if(selection=="logout"):
            print("Transaction Complete!")
            print("Total balance:",account)
            login1=int(input("Enter ID number:"))
            login2=int(input("Enter password:"))



