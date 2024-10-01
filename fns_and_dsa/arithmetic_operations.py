def perform_operation(num1, num2, operation):
    print("Arithmetic Operations")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()
<<<<<<< HEAD
    if num1 / num2 == 0:
        print("main.py script can recognize and display appropriately.")
=======
if operation == 'add':
        return num1 + num2
elif operation == 'subtract':
        return num1 - num2
elif operation == 'multiply':
        return num1 * num2
elif operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        return num1 / num2
    else:
        return "Error: Invalid operation. Please use 'add', 'subtract', 'multiply', or 'divide'."
>>>>>>> e9c974c89944f59c87549669ba30c9794e60d943
    result = perform_operation(num1, num2, operation)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()
