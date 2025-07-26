def calculator():
    print("=== Calculator ===")
    print("Operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus (%)")
    print("6. Square")
    print("7. Cube")
    print("8. Exit")

    while True:
        choice = input("\nEnter your choice (1-8): ")

        match choice:
            case '1':
                num1 = float(input("Enter num1: "))
                num2 = float(input("Enter num2: "))
                print(f"Result: {num1 + num2}")
            case '2':
                num1 = float(input("Enter num1: "))
                num2 = float(input("Enter num2: "))
                print(f"Result: {num1 - num2}")
            case '3':
                num1 = float(input("Enter num1: "))
                num2 = float(input("Enter num2: "))
                print(f"Result: {num1 * num2}")
            case '4':
                num1 = float(input("Enter num1: "))
                num2 = float(input("Enter num2: "))
                if num2 == 0:
                    print("Error: Division by zero!")
                else:
                    print(f"Result: {num1 / num2}")
            case '5':
                num1 = int(input("Enter num1: "))
                num2 = int(input("Enter num2: "))
                print(f"Result: {num1 % num2}")
            case '6':
                number = float(input("Enter a number: "))
                print(f"Square: {number ** 2}")
            case '7':
                number = float(input("Enter a number: "))
                print(f"Cube: {number ** 3}")
            case '8':
                print("Exiting...")
                break
            case _:
                print("Invalid choice. Try again!")

calculator()



