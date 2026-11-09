# Personal Mini-Toolkit
# A menu-driven program with four tools:
# a guessing game, a to-do list, a calculator and a name formatter.

import random

# This list lives outside the main loop so tasks are kept
# every time the user comes back to the To-Do List tool.
todo_list = []

print("Welcome to your Personal Mini-Toolkit!")

running = True

# MAIN MENU LOOP: shows the menu again after every tool until the user quits.
while running:
    print()
    print("=============================")
    print("   PERSONAL MINI-TOOLKIT")
    print("=============================")
    print("1. Number Guessing Game")
    print("2. To-Do List")
    print("3. Simple Calculator")
    print("4. Name Formatter")
    print("5. Quit")
    print("-----------------------------")
    choice = input("Choose an option (1-5): ").strip()

    # ------------------------------------------------------------
    # TOOL 1: Number Guessing Game
    # The computer picks a number from 1 to 20. The user keeps
    # guessing and gets "too low" / "too high" hints until correct.
    # ------------------------------------------------------------
    if choice == "1":
        secret_number = random.randint(1, 20)
        attempts = 0
        playing = True

        print()
        print("--- Number Guessing Game ---")
        print("I'm thinking of a number between 1 and 20. Type 'q' to give up.")

        while playing:
            guess = input("Your guess: ").strip().lower()

            if guess == "q":
                print(f"No worries! The number was {secret_number}.")
                playing = False
            elif not guess.isdigit():
                print("Please enter a whole number (or 'q' to quit).")
            else:
                guess = int(guess)
                attempts += 1

                if guess < secret_number:
                    print(f"{guess} is too low. Try a bigger number!")
                elif guess > secret_number:
                    print(f"{guess} is too high. Try a smaller number!")
                else:
                    print(f"Brilliant! You got it in {attempts} attempt(s)!")
                    playing = False

    # ------------------------------------------------------------
    # TOOL 2: To-Do List
    # Uses a list that changes while the program runs: tasks can be
    # added, viewed and removed.
    # ------------------------------------------------------------
    elif choice == "2":
        in_todo = True

        print()
        print("--- To-Do List ---")

        while in_todo:
            print()
            print("1. Add a task")
            print("2. View tasks")
            print("3. Remove a task")
            print("4. Back to main menu")
            todo_choice = input("Choose (1-4): ").strip()

            if todo_choice == "1":
                task = input("What is the task? ").strip()
                if task == "":
                    print("A task can't be empty. Nothing was added.")
                else:
                    todo_list.append(task)
                    print(f'Added "{task}". You now have {len(todo_list)} task(s).')

            elif todo_choice == "2":
                if len(todo_list) == 0:
                    print("Your to-do list is empty. Nice and clear!")
                else:
                    print("Your tasks:")
                    for number, task in enumerate(todo_list, start=1):
                        print(f"  {number}. {task}")

            elif todo_choice == "3":
                if len(todo_list) == 0:
                    print("There is nothing to remove yet.")
                else:
                    for number, task in enumerate(todo_list, start=1):
                        print(f"  {number}. {task}")
                    remove_choice = input("Number of the task to remove: ").strip()

                    if remove_choice.isdigit() and 1 <= int(remove_choice) <= len(todo_list):
                        removed = todo_list.pop(int(remove_choice) - 1)
                        print(f'Done! Removed "{removed}".')
                    else:
                        print("That number isn't on the list.")

            elif todo_choice == "4":
                in_todo = False

            else:
                print(f'"{todo_choice}" is not an option. Please choose 1 to 4.')

    # ------------------------------------------------------------
    # TOOL 3: Simple Calculator
    # Takes two numbers and an operator, then uses conditionals
    # to pick the right calculation.
    # ------------------------------------------------------------
    elif choice == "3":
        print()
        print("--- Simple Calculator ---")
        first = input("First number: ").strip()
        operator = input("Operator (+, -, *, /): ").strip()
        second = input("Second number: ").strip()

        # try/except stops the program from crashing if a number is typed wrongly
        try:
            num1 = float(first)
            num2 = float(second)

            if operator == "+":
                print(f"{num1} + {num2} = {num1 + num2}")
            elif operator == "-":
                print(f"{num1} - {num2} = {num1 - num2}")
            elif operator == "*":
                print(f"{num1} * {num2} = {num1 * num2}")
            elif operator == "/":
                if num2 == 0:
                    print("Oops! You can't divide by zero.")
                else:
                    print(f"{num1} / {num2} = {num1 / num2}")
            else:
                print(f'Sorry, "{operator}" is not a supported operator.')
        except ValueError:
            print("Please enter valid numbers, like 4 or 3.5.")

    # ------------------------------------------------------------
    # TOOL 4: Name Formatter
    # Shows a name in different styles and builds the initials
    # using a loop.
    # ------------------------------------------------------------
    elif choice == "4":
        print()
        print("--- Name Formatter ---")
        name = input("Enter your full name: ").strip()

        if name == "":
            print("You didn't type a name. Try again from the menu!")
        else:
            initials = ""
            for part in name.split():
                initials += part[0].upper() + "."

            print(f"Proper format : {name.title()}")
            print(f"UPPERCASE     : {name.upper()}")
            print(f"lowercase     : {name.lower()}")
            print(f"Initials      : {initials}")
            print(f"Letters in name (no spaces): {len(name.replace(' ', ''))}")

    # QUIT: ends the main loop
    elif choice == "5":
        running = False

    # INVALID CHOICE: polite message, program keeps running
    else:
        print(f'Oops! "{choice}" is not on the menu. Please pick a number from 1 to 5.')

print()
print("Thanks for using the toolkit. Goodbye and keep coding!")