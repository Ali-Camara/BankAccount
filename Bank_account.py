balance = 0.0

while True:
    print("Bank Account Options:")
    print("1) Check Balance")
    print("2) Deposit")
    print("3) Withdraw")
    print("4) Quit")
    choice = input("Enter choice: ")

    if choice == '4':
        print("Exiting bank account.")
        break

    elif choice == '1':
        print("Your balance is:", balance)

    elif choice == '2':
        amount = float(input("Enter amount to deposit: "))
        if amount > 0:
            balance += amount
            print("Deposited:", amount)
        else:
            print("Invalid deposit amount")

    elif choice == '3':
        amount = float(input("Enter amount to withdraw: "))
        if amount > balance:
            print("Insufficient funds")
        elif amount <= 0:
            print("Invalid withdrawal amount")
        else:
            balance -= amount
            print("Withdrawn:", amount)

    else:
        print("Invalid input")
