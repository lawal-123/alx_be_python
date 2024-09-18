num1 = float(input("enter the first number: "))
num2 = float(input("enter the second number: "))
operation = input("choose the operation (+, -, *, /): ")
match operation:
    case '+':
        result = num1 + num2
        print(result)
    case '-':
        result = num1 - num2
        print(result)    
    case '*':
        result = num1 * num2
        print(result)
    case '/':
        if num1/num2 == 0:
            print("error: Division by zero is not allowed")  
        else:
            result = num1/num2
            print(result)      