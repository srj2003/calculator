# Dark Rounded Calculator

A simple, visually appealing calculator application built using **Tkinter** with a dark-themed interface and rounded buttons. It supports basic arithmetic operations.

## Features

- Dark mode UI for a sleek look.
- Rounded buttons with vibrant colors for better user experience.
- Supports basic operations: addition (+), subtraction (-), multiplication (x), division (/), and modulus (%).
- Includes Clear (`C`) button to reset the input.
- Error handling for invalid expressions.


## Prerequisites

- Python 3.x
- Tkinter (built-in with Python)

## How to Run

1. Clone the repository or copy the `calculator.py` file.
   ```bash
   git clone <repo-url>
   cd <repo-folder>
   ```

2. Run the script using Python.
   ```bash
   python calculator.py
   ```

3. The calculator window will open, and you can start using it.

## File Structure

```
DarkRoundedCalculator/
|── calculator.py   # Main script for the calculator
|── README.md         # Documentation (this file)
```

## Controls and Buttons

| Button | Description              |
|--------|--------------------------|
| C      | Clear the display input  |
| ( )    | Add parentheses          |
| x      | Multiplication operator  |
| /      | Division operator        |
| %      | Modulus operator         |
| =      | Calculate the result     |

## Demo

### Basic Usage:
1. Enter numbers and operators using the on-screen buttons.
2. Press `=` to evaluate the expression.
3. Press `C` to clear the display.

## Error Handling
- If an invalid expression is entered, the display shows `Error`.

## Customization

- Modify button colors and fonts in the code:
  ```python
  button_font = tkfont.Font(family="Sans Serif", size=18, weight="bold")
  button_configs = [(text, color, command), ...]
  ```

