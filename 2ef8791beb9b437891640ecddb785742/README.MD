# Quadratic Equation Solver Documentation

## Overview
This C# program is designed to solve a quadratic equation of the form \(x^2 + bx + c = 0\). It handles both real and complex roots and uses console-based user input and output.

## Usage
1. **Input**: The program prompts the user to enter the coefficients \(b\) and \(c\) of the quadratic equation.
2. **Processing**: It calculates the discriminant (\(b^2 - 4c\)) to determine the nature of the roots.
3. **Output**: Depending on the value of the discriminant, it displays the roots as real and different, real and same, or complex and different.

## Code Breakdown

### Main Method
- **User Input**:
  - The program asks the user to input the values of \(b\) and \(c\).
  - These values are read from the console and converted to `double`.

- **Discriminant Calculation**:
  - The discriminant is calculated using the formula \(b^2 - 4c\).

- **Root Calculation and Output**:
  - **Real and Different Roots**:
    - If the discriminant is greater than 0, the roots are real and different.
    - The roots are calculated using the quadratic formula and printed.
  - **Real and Same Roots**:
    - If the discriminant is equal to 0, the roots are real and the same.
    - The root is calculated and printed.
  - **Complex Roots**:
    - If the discriminant is less than 0, the roots are complex.
    - The real and imaginary parts of the roots are calculated and printed in the form \(a + bi\) and \(a - bi\).

## Example Interaction

### Real and Different Roots
```
Enter coefficient b: 5
Enter coefficient c: 6
The roots are real and different. Root1 = -2, Root2 = -3
```

### Real and Same Roots
```
Enter coefficient b: 4
Enter coefficient c: 4
The roots are real and same. Root = -2
```

### Complex Roots
```
Enter coefficient b: 2
Enter coefficient c: 5
The roots are complex and different.
Root1 = -1 + 2i
Root2 = -1 - 2i
```

## Notes
- The program assumes the coefficient of \(x^2\) is always 1, simplifying the quadratic equation to \(x^2 + bx + c = 0\).
- It handles all possible cases of roots (real and different, real and same, complex) and provides clear output for each case.