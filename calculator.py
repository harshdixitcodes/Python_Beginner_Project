def calculator():
    print("Welcome to the simple Calculator!")
    print("Operations you can perform: add, subtract, multiply, divide")
    
    while True:
        operation = input("Please choose an operation (add, subtract, multiply, divide) or 'exit' to quit > ").lower()
        if operation == "exit":
            print("Thankyou for using the Simple Calculator. Goodbye!")
            break
        
        if operation not in ['add', 'subtract', 'multiply', 'divide']:
            print("Invalid operation. Please try again.") 
            continue
        
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter a number. ")
            continue
        
        if operation == "add":
            result = num1 + num2
            print(f"The result is {result}")
            
        elif operation == "subtract":
            result = num1 - num2
            print(f"The result is {result}")
            
        elif operation == "multiply":
            result = num1*num2
            print(f"The result is {result}")
            
        elif operation == "divide":
            if num2 == 0:
                print("Error! Division by 0 is not allowed.")
            result = num1/num2
            print(f"The result is {result}")

calculator()
            
