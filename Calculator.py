def main():
    # Prompt for first number
    num1_input = input("Enter the first number: ")
    
    # Validate first number
    try:
        num1 = float(num1_input)
    except ValueError:
        print("Error: Please enter a valid number.")
        return
    
    # Prompt for operation
    operation = input("Enter an operation (+, -, *, /): ")
    
    # Validate operation
    if operation not in ['+', '-', '*', '/']:
        print("Error: Please enter a valid operation (+, -, *, /).")
        return
    
    # Prompt for second number
    num2_input = input("Enter the second number: ")
    
    # Validate second number
    try:
        num2 = float(num2_input)
    except ValueError:
        print("Error: Please enter a valid number.")
        return
    
    # Check for division by zero
    if operation == '/' and num2 == 0:
        print("Error: Cannot divide by zero. Please try again with a different number.")
        return
    
    # Perform calculation
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        result = num1 / num2
    
    # Display result in human-readable format
    print(f"\n{num1} {operation} {num2} = {result}")

if __name__ == "__main__":
    main()