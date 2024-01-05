import art

print(art.calculator)
print(art.calculator_msg)


def number_input(s):
    """Asking for user input and returning it as a float number"""
    while True:

        number = input(s)
        try:
            number = float(number)
            break
        except:
            print("Please choose a number")
            continue
    return number


def calculating(num1, num2, operation=""):
    """Calculating result with 2 numbers, based on the chosen operation from user"""

    while operation not in ["+", "-", "*", "/", "**"]:
        operation = input("Pick an operation('+' '-' '/' '*' or '**' for squared): ")
        """
            Asking user to choose an operation from the list
            adding operation as a value, type srt right now
            returning result evaluating with chosen operator from operation
        """
    result = eval(f"{num1} {operation} {num2}")
    """Printing a message for the user with the whole operation executed"""
    print(f"{num1} {operation} {num2} = {result}")
    """User choosing to continue with the same value or new one or just stop"""
    user_continue = ""
    while user_continue not in ["y", "n", "stop"]:
        user_continue = input(
            f"Type 'y' to continue calculating with {result}, or type 'n' to start a "
            "new calculation or type 'stop' to stop: ").lower()
        if user_continue == "y":
            """
                If user chooses to continue with same value
                Asking for second value
            """
            calculating(num1=result, num2=number_input(s="Pick second number: "))

        elif user_continue == "n":
            """
            Taking input from two numbers
            """
            calculating(num1=number_input("Pick first number: "), num2=number_input(s="Pick second number: "))
        else:
            print(art.good_bye)
            break


calculating(num1=number_input("Pick first number: "), num2=number_input("Pick second number: "))

