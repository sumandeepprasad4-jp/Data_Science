balance=0.0
def check_balance():
    print(f"Your current balance is {balance}")


def deposit(depamt):
    global balance
    if depamt <=0:

        print("Can't deposit negative amount")

    else:
        balance += depamt

        print("Your amount has successfully deposited")



def withdraw(widamt):
    global balance
    if widamt > balance:

        print("Can't withdraw! insufficient balance")

    elif widamt <=0:

        print("can't withdraw negative amount")

    else:
        balance -= widamt

        print("Amount has successfully withdrawn")

print("WELLCOME TO DEEP BANK")

while True:
    print("1.Check your balance")
    print("2.Deposit an amount")
    print("3.Withdraw an amount")
    print("4.Quit\n")
    # We take input as string so if user enters any type (int/float/str), no error occurs — just print custom message.
    choice = (input("Enter your choice(1-4):"))
    if choice=='1':
        check_balance()
    elif choice=='2':
        depamt = float(input("Enter your deposit amount:"))
        deposit(depamt)
    elif choice=='3':
        widamt = float(input("Enter the amount to be withdraw:"))
        withdraw(widamt)
    elif choice=='4':
        break
    else:

        print("Invalid choice choose between (1-4)")
print("Thankyou for banking with us...")