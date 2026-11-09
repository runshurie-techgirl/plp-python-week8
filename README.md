# Personal Mini-Toolkit

## What It Does
A menu-driven Python program with four tools that keeps running until the user chooses Quit:

1. **Number Guessing Game** – guess a secret number from 1 to 20 with higher/lower hints.
2. **To-Do List** – add, view and remove tasks; the list is kept while the program runs.
3. **Simple Calculator** – add, subtract, multiply or divide two numbers (with a divide-by-zero check).
4. **Name Formatter** – shows a name in proper case, UPPERCASE, lowercase, with initials and letter count.

Invalid menu choices get a polite message instead of crashing the program.

## How to Run
1. Install Python 3 from https://www.python.org/downloads/
2. Download or clone this repository.
3. Open a terminal in the project folder and run:

```
python toolkit.py
```

(On some systems use `python3 toolkit.py`.)

## Files
- `toolkit_plan.txt` – the plan: tools, menu text and concepts used
- `toolkit.py` – the program
- `screenshots/` – the menu (including an invalid choice) and each tool running

## Reflection
The hardest part was building the To-Do List, because it needed a loop inside the main menu loop plus a list that keeps changing. The bug that took longest to fix was making sure the program didn't crash when the user typed letters instead of numbers, which I solved with `.isdigit()` checks and a `try`/`except` in the calculator. Writing the plan first in `toolkit_plan.txt` made the build much faster because I already knew the menu text and which concepts each tool needed. I also learned that reading my code top to bottom and adding comments helps me spot mistakes early. With one more week, I would add a countdown timer, save the to-do list to a file so it survives after the program closes, and a score tracker for the guessing game.