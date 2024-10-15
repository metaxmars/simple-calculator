import sys

# Step 1: Welcome message and description
print("="*50)
print(" Welcome to the Simple Calculator Program! ".center(50, "="))
print("="*50)
print("""
This calculator will help you perform basic mathematical operations, including:
- Addition (+)
- Subtraction (-)
- Multiplication (*)
- Division (/)

You can perform as many calculations as you'd like. Just enter two numbers and choose an operation.

Let's begin!
""")

# Step 2: Game Logic
game_on = True
total_calcs = 0
results_list = []

while game_on:

# Step 3: Getting input from player and validating it
    try:
     first_number = float(input("\nEnter the first number: "))
     second_number = float(input("Enter the second number: "))
    except ValueError:
     print("Invalid input. Please enter numbers only.")
     continue  # Restart the loop to ask for input again

    # Step 4: Choosing the operation and validating it
    operation_choice = input("Which calculation would you like to execute? (+, -, *, /): ").strip()

    # Step 4: Perform the operation and handle division by zero
    result = None

    if operation_choice == "+":
        result = first_number + second_number
        print(f"\nResult: {first_number} + {second_number} = {result:.2f}")
    elif operation_choice == "-":
        result = first_number - second_number
        print(f"\nResult: {first_number} - {second_number} = {result:.2f}")
    elif operation_choice == "*":
        result = first_number * second_number
        print(f"\nResult: {first_number} * {second_number} = {result:.2f}")
    elif operation_choice == "/":
        if second_number == 0:
            print("\nError: Division by zero is not allowed.")
        else:
            result = first_number / second_number
            print(f"\nResult: {first_number} / {second_number} = {result:.2f}")
    else:
        print("\nUnknown operation. Please enter one of (+, -, *, /).")
        continue  # Restart the loop if the operation is invalid

    game_on = False
    # Count total executions number and print after every executed calculation
    total_calcs += 1
    print(f"Your total number of executions so far is: {total_calcs}")

    # Adding results into the list
    if result is not None:
        results_list.append(result)

    #Step 3: Asking the player for another execution
    while game_on is False:
        player_answer = input("\nWould you like to execute another operation? (Y)es or (N)o. ").capitalize()
        if player_answer == "Y":
            game_on = True
        elif player_answer == "N":
            # Provide a summary of all calculations before exiting
            print("\nThank you for using the calculator!")
            print(f"\nYou performed {total_calcs} calculations today.")
            print("Here are your results:")
            print("-" * 50)
            for result in results_list:
                print(result)
            print("-" * 50)
            print("\nGoodbye! Have a great day!")
            sys.exit()  # Exit the program
        else:
            print("Unknown command.")
