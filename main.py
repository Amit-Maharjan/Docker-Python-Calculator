import os

historyFile = "history.txt"

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def save_to_history(expression, result):
    with open(historyFile, "a") as file:
        file.write(f"{expression} = {result}\n")

def show_history():
    if os.path.exists(historyFile):
        with open(historyFile, "r") as file:
            print("\nCalculation History:")
            print(file.read())
    else:
        print("No history available.")

def main():
    while True:
        print("\nSimple Calculator with History")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Show History")
        print("6. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == '6':
            print("Exiting...")
            break
        elif choice == '5':
            show_history()
            continue
        
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        if choice == '1':
            result = add(num1, num2)
            operation = f"{num1} + {num2}"
        elif choice == '2':
            result = sub(num1, num2)
            operation = f"{num1} - {num2}"
        elif choice == '3':
            result = mul(num1, num2)
            operation = f"{num1} * {num2}"
        elif choice == '4':
            result = div(num1, num2)
            operation = f"{num1} / {num2}"
        else:
            print("Invalid choice, please try again.")
            continue
        
        print(f"Result: {result}")
        save_to_history(operation, result)

if __name__ == "__main__":
    main()
