"""
Calculator CLI App
-------------------
A simple command-line calculator supporting basic operations:
addition, subtraction, multiplication, and division.

Task: Python Developer Internship - Task 1
"""


def add(a, b):
    """Return the sum of a and b."""
    return a + b


def subtract(a, b):
    """Return the difference of a and b."""
    return a - b


def multiply(a, b):
    """Return the product of a and b."""
    return a * b


def divide(a, b):
    """Return the quotient of a and b. Raises ZeroDivisionError if b is 0."""
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b


def get_number(prompt):
    """Prompt the user for a numeric value, re-asking until valid input is given."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def print_menu():
    print("\n===== CALCULATOR MENU =====")
    print("1. Add        (+)")
    print("2. Subtract   (-)")
    print("3. Multiply   (*)")
    print("4. Divide     (/)")
    print("5. Exit")
    print("============================")


def main():
    operations = {
        "1": ("Addition", add),
        "2": ("Subtraction", subtract),
        "3": ("Multiplication", multiply),
        "4": ("Division", divide),
    }

    print("Welcome to the Python CLI Calculator!")

    while True:
        print_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == "5":
            print("Goodbye! Thanks for using the calculator.")
            break

        if choice not in operations:
            print("Invalid choice. Please select a number between 1 and 5.")
            continue

        name, operation = operations[choice]
        num1 = get_number("Enter the first number: ")
        num2 = get_number("Enter the second number: ")

        try:
            result = operation(num1, num2)
            print(f"\n{name} Result: {num1} {['+','-','*','/'][int(choice) - 1]} {num2} = {result}")
        except ZeroDivisionError as e:
            print(f"\nError: {e}")

        again = input("\nDo you want to perform another calculation? (y/n): ").strip().lower()
        if again != "y":
            print("Goodbye! Thanks for using the calculator.")
            break


if __name__ == "__main__":
    main()
