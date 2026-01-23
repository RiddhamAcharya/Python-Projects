import datetime

def CheckBalance():
    f = open("./Data/balance.txt","r")
    data = f.read().strip()
    if data=='':
        return 0
    else:
        return int(data)

def DepositAmount():
    x = datetime.datetime.now()
    currentbalance = CheckBalance()
    amount = int(input("Enter the amount you want to deposit: "))
    balance = currentbalance + amount
    with open("./Data/balance.txt", "w") as f:
        f.write(str(balance))

    with open("./Data/statements.txt","a") as fi:
        fi.write(f"\n{x} -> Deposited Rs.{amount} to the account. Opening Balance=Rs{currentbalance}. Closing Balance=Rs.{balance}")

    print(f"You have deposited Rs.{amount} and Your current balance is Rs.{balance}")




def WithdrawAmount():
    x = datetime.datetime.now()
    currentbalance = CheckBalance()
    amount = int(input("Enter the amount you want to withdraw: "))
    balance = currentbalance - amount
    if balance < 0:
        print("Insuffucient Funds. You can't withdraw Money")
    else:
        with open("./Data/balance.txt", "w") as f:
            f.write(str(balance))

        with open("./Data/statements.txt","a") as fi:
            fi.write(f"\n{x} -> WithDrawn Rs.{amount} to the account. Opening Balance=Rs{currentbalance}. Closing Balance=Rs.{balance}")

        print(f"You have withdrawn Rs.{amount} and Your current balance is Rs.{balance}")


def CheckStatement():
    with open("./Data/statements.txt", "r") as fi:
        for x in fi:
            print(x)

def ChangePin():
    
    with open("./Data/pin.txt","r") as p:
        curpin = int(p.read())

    pin = int(input("Enter Your Current Pin: "))
    if(pin == curpin):
        npin = int(input("Enter Your New Pin: "))
        length = len(str(abs(npin)))
        if(length != 4):
            print("Pin must be of 4 characters.")
        else:
            cnpin = int(input("Confirm your New Pin: "))
            if(npin == cnpin):
                 x = datetime.datetime.now()
                 with open("./Data/pin.txt", "w") as pi:
                     pi.write(str(npin))
                     print("Successfully Changed Pin")

                 with open("./Data/statements.txt","a") as fi:
                    fi.write(f"\n{x} -> Pin Code changed from {curpin} to {npin}")
                    
                    
                
            else:
                print("Pin Doesn't match")
    else:
        print("Wrong Pin")

if __name__ == "__main__":
    print("\n\t--------Welcome to State Bank ATM!--------\n")
    f = open("./Data/pin.txt")

    CorrectPin = int(f.read())
    i=2
    while True:
        UserPin = int(input("Enter your pin to continue: "))
        length = len(str(abs(UserPin)))
        if(length != 4):
            print(f"The Pin must be of 4 digits {i} attempts left")
            if(i==0):
                print("Attempt Over. Sorry You have been blocked.")
                break
            else:
                i -= 1

        elif(UserPin != CorrectPin):
            print(f"❌ Wrong Pin! {i} attemps left")
            if(i==0):
                print("Attempt Over. Sorry You have been blocked.")
                break
            else:
                i -= 1
        else:
            print("\nWelcome User!\n")
            break

    if(UserPin ==  CorrectPin):
        while True:
            print("\nWhat do you want to do\n1.Check Balance\n2.Deposit Amount\n3.Withdraw balance\n4.Check Statements\n5.Change Pin\n6.Exit")
            userInput = int(input("Enter Your choice: "))
            if(userInput == 1):
                b=CheckBalance()
                print(f"Your Current Balance is Rs.{b}")
            elif(userInput == 2):
                DepositAmount()

            elif(userInput==3):
                WithdrawAmount()

            elif(userInput==4):
                CheckStatement()

            elif(userInput == 5):
                ChangePin()
            
            elif(userInput == 6):
                print("Thank You for comming. Have a Nice Day!")
                break
            else:
                print("Wrong Choice. Enter Again")
            