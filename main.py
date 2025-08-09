while True:
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid Input!! Please enter only numerical value")
        continue 

    choice = """
Select an operation:
 1 ➔ Addition (+)
 2 ➔ Subtraction (-)
 3 ➔ Multiplication (*)
 4 ➔ Division (/)
 5 ➔ Floor Division (//)
 6 ➔ Modulus (%)
 7 ➔ Power (**)
 8 ➔ Quit 
"""
    print(choice)


    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid Input!! Enter a Valid Choice")
        continue  

    if choice == 1:
        print(f"{num1} + {num2} = ", num1 + num2)
    elif choice == 2:
        print(f"{num1} - {num2} = ", num1 - num2)
    elif choice == 3:
        print(f"{num1} * {num2} = ", num1 * num2)
    elif choice == 4:
        try:
            print(f"{num1} / {num2} = ", num1 / num2)
        except ZeroDivisionError:
            print("Cannot divide by Zero! Enter a valid value")
    elif choice == 5:
        print(f"{num1} // {num2} = ", num1 // num2)
    elif choice == 6:
        print(f"{num1} % {num2} = ", num1 % num2)
    elif choice == 7:
        print(f"{num1} ** {num2} = ", num1 ** num2)
    else:
        print("Invalid Choice!!! Select a valid choice ")
    quit_choice=input("Would like to continue or willing to quit y/n: ")
    if quit_choice=='y':
        break
    else:
        continue
