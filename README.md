# Function-Based Calculator 🧮

A simple **menu-driven calculator built with Python** using functions. The program performs basic arithmetic operations and continues running until the user chooses the exit option.

## Features

* Addition
* Subtraction
* Multiplication
* Division
* Function-based implementation
* Menu-driven interface
* Multiple calculations in one execution
* Division-by-zero validation
* Exit option

## Technologies Used

* **Python 3**

## Operations

| Choice | Operation      |
| ------ | -------------- |
| 1      | Addition       |
| 2      | Subtraction    |
| 3      | Multiplication |
| 4      | Division       |
| 5      | Exit           |

## Functions Used

The calculator uses separate functions for each arithmetic operation:

```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divided(a, b):
    return a / b
```

## How to Run

### 1. Install Python

Make sure Python 3 is installed on your computer.

### 2. Run the Program

Open the terminal in the project directory and run:

```bash
python calculator.py
```

## Example

```text
=== WELLCOME TO CALCULATOR ===

1. Add
2. Subtract
3. Multiply
4. Divide
5. Exit

Enter Your Choise: 1
Enter Your First Digit: 10
Enter Your Second Digit: 5

Your Result: 15
```

## Division by Zero

The program checks whether the second number is zero before performing division.

```text
Enter Your First Digit: 10
Enter Your Second Digit: 0

Cannot divided by zero.
```

## Project Structure

```text
Function-Based-Calculator/
│
├── calculator.py
└── README.md
```

## How the Program Works

1. The program displays the calculator menu.
2. The user selects an operation.
3. The program asks for two numbers.
4. The corresponding function is called.
5. The result is displayed.
6. The menu appears again for another calculation.
7. The program stops when the user selects **5. Exit**.

## Author

**Abhronil Jash**

CSE Student | Python Enthusiast


## How It Works

The program takes:

1. Two numbers as input.
2. An arithmetic operator.
3. Performs the selected operation.
4. Displays the result.

## Example

```text
Enter the number: 10
Enter the number: 5
Enter the symbol: +
10 + 5 = 15
```

## Project Structure

```text
Simple-Calculator/
│
├── calculator.py
└── README.md
```

## Author

**Abhronil Jash**

CSE Student | AGEMC
