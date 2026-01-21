def main():
    # ANSI color codes
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    RESET = '\033[0m'
    
    # Print header
    print(f"\n{CYAN}{'='*50}")
    print(f"{BOLD}          🧮  SIMPLE CALCULATOR  🧮{RESET}")
    print(f"{CYAN}{'='*50}{RESET}\n")
    
    # Prompt for first number
    num1_input = input(f"{YELLOW}Enter the first number: {RESET}")
    
    # Validate first number
    try:
        num1 = float(num1_input)
    except ValueError:
        print(f"\n{RED}❌ Error: Please enter a valid number.{RESET}\n")
        return
    
    # Prompt for operation
    print(f"\n{CYAN}Available operations: {BOLD}+  -  *  /{RESET}")
    operation = input(f"{YELLOW}Enter an operation: {RESET}")
    
    # Validate operation
    if operation not in ['+', '-', '*', '/']:
        print(f"\n{RED}❌ Error: Please enter a valid operation (+, -, *, /).{RESET}\n")
        return
    
    # Prompt for second number
    num2_input = input(f"{YELLOW}Enter the second number: {RESET}")
    
    # Validate second number
    try:
        num2 = float(num2_input)
    except ValueError:
        print(f"\n{RED}❌ Error: Please enter a valid number.{RESET}\n")
        return
    
    # Check for division by zero
    if operation == '/' and num2 == 0:
        print(f"\n{RED}❌ Error: Cannot divide by zero. Please try again!{RESET}\n")
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
    
    # Display result with styling
    print(f"\n{GREEN}{'─'*50}")
    print(f"{BOLD}   RESULT:{RESET}")
    print(f"{GREEN}{'─'*50}{RESET}")
    print(f"\n   {BOLD}{num1} {operation} {num2} = {result}{RESET}\n")
    print(f"{GREEN}{'─'*50}{RESET}\n")

if __name__ == "__main__":
    main()