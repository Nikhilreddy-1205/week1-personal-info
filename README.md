# Personal Information Manager

This is my first Python project. It stores and displays personal information in a nicely formatted way.

## What I Learned
- Variables and data types
- Input and output using `print()` and `input()` 
- String formatting with f-strings
- Basic input validation using `while` loops 

## How to Run
1. Install Python 3 on your system.
2. Open a terminal in this folder.
3. Run:
4. Follow the prompts to enter your information.

## Project Overview
A simple console application that:
- Stores static personal details (name, age, city).
- Asks the user for preferences like favourite food and place/color.
- Shows all information together in a clear summary.

## Setup Instructions
- Clone this repository or download the ZIP.
- Make sure Python 3 is installed.
- Optional: Create a virtual environment if you want.

## Technical Details
- Uses variables to store static data (name, age, city, hobby).
- Uses `input()` to read user values and `while` loops to prevent empty input.
- Uses f-strings to format the final output, including `age * 12` to show age in months.
- Prints a welcome message at the start and a goodbye message at the end.

## Features
- Static information: name, age, city, hobby.
- Dynamic information from user: favourite food and favourite place/color.
- Formatted summary with separators.
- Basic input validation for empty strings.
- Age calculation in months.

## Challenges & Solutions
- **Empty input:** Solved by repeating the question in a `while` loop until the user types something.

## Testing Evidence
See `test_inputs.txt` for manual test cases, including:
- Normal input (all fields filled correctly).
- Empty input once, then valid input (checks validation).
- Long text values to ensure the program still prints everything.
- Run `python personal_info.py` from the project folder.

