print("""*****************************************
    "Welcome to Cash Machine"
    "1 - Check Balance"
    "2 - Deposit Money"
    "3 - Withdraw Money"
    "q - Exit"
*************************************************
    """)

balance = 1000

while True:
    operation = input("Select operation: ")

    if operation == "q":
        print("Thank you!")
        break

    elif operation == "1":
        print("Your balance is: {} TRY".format(balance))

    elif operation == "2":
        amount = int(input("Amount: "))
        balance += amount

    elif operation == "3":
        amount = int(input("Amount: "))
        if balance < amount:
            print("Insufficient balance")
            continue
        balance -= amount

    else:
        print("Invalid operation!")

