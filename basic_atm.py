print("ATM")
print("Welcome,what would you like to do?")
print("1.Select_Language\n2.Withdraw_Cash\n3.Deposit_Cash\n4.Check_Balance\n5.Exit")
z={"Account_Number":1234,"Pin":2468,"Balance":0}
while True:
    try:
        n=int(input("Enter your choice: "))
        if n==5:
            print("Exit is success")
            break
        if 0<n<=4:
            if n==1:
                a=input("Select your language: 1.English\tMarathi?:")
                if a=="English":
                    print("Ok our conversation will be in english")
                else:
                    print("This language is not yet supported but it will be soon!")
            elif n==2:
                print("You are in withdrawl section")
                b=int(input("Enter your Account_Number:"))
                d=int(input("Enter your security pin:"))
                if b == z["Account_Number"] and d == z["Pin"]:
                    c=int(input("Enter the amount to withdraw: "))
                    if c<=z["Balance"]:
                        z["Balance"]-=c
                        print("Amount is withdrawn successfully")
                    else:
                        print("Ask yourself do have such amount,then why are you trying?")
                else:
                    print("Unauthorized INPUTS5")
            elif n==3:
                print("You are in Deposit Section")
                e=int(input("Enter the account_number you want to deposit:"))
                f=int(input("Enter the amount: "))
                g=int(input("Enter the security pin:"))
                if e == z["Account_Number"] and g == z["Pin"]:
                    z["Balance"]+=f
                    print("Amount deposited successfully")
                else:
                    print("Inputs are wrong,try again")
            elif n==4:
                h=int(input("Enter the account number:"))
                i=int(input("Enter security pin: "))
                if h == z["Account_Number"]and i == z["Pin"]:
                    print("Your Account Balance is: ",z["Balance"])
                else:
                    print("You have incorretly entered account number/pin,try again")
        else:
            print("You should enter choice between 1-5")
    except ValueError:
        print("We accept only int values,try again")
        
            
