# Hanisha A - Python Coding Solutions

## Programming Language:
Python

## Description:
This repository contains solutions to 4 Python programming problems. Each solution includes comments explaining the logic and example usage.

---

## Problems and Solutions:

### Problem 1: Simple Calculator
**Question**: Create a calculator class that can perform basic arithmetic operations (add, subtract, multiply, divide) with proper error handling.

**Solution**: `calculator.py`  
**Implementation**:
- Uses a class with constructor to initialize operands and operation
- If-else structure to handle different operations
- Special handling for division by zero
- Case-insensitive operation names

**Example Usage**:
```python
cal = Calculator(10, 39, "Add")
print(cal.calculate())  # Output: 49
````

---

### Problem 2: Generate Odd Number Series (First N odds)

**Question**: Write a function that generates the first N odd numbers.

**Solution**: `odd_series_n.py`
**Implementation**:

* Uses a for-loop with list comprehension
* Mathematical formula (`i*2 + 1`) to calculate odd numbers
* Returns results as an array

**Example Usage**:

```python
print(generate_odd_series_n(4))  # Output: [1, 3, 5, 7]
```

---

### Problem 3: Generate Odd Number Series (Up to limit)

**Question**: Write a function that generates all odd numbers up to a given number (adjusting even inputs).

**Solution**: `odd_series_limit.py`
**Implementation**:

* Adjusts even input to nearest lower odd
* Generates series using step-2 iteration
* Outputs as formatted comma-separated string

**Example Usage**:

```python
print(generate_odd_series_limit(6))  # Output: "1, 3, 5, 7"
```

---

### Problem 4: Count Multiples in Array

**Question**: Given an array of numbers, count how many are multiples of each digit from 1 to 9.

**Solution**: `count_multiples.py`
**Implementation**:

* Initializes counter dictionary for digits 1-9
* Nested loops to check all number-divisor combinations
* Returns comprehensive count dictionary

**Example Usage**:

```python
input_array = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]
print(count_multiples(input_array))
```

**Output**:

```python
{
 1: 11, 2: 8, 3: 4, 4: 4,
 5: 3, 6: 2, 7: 0, 8: 1,
 9: 1
}
```

---

## How to Run:

Clone this repository

Execute any solution file using Python:

```bash
python filename.py
```

## Author:

Hanisha A

---

## Key improvements:

1. **Explicit question statements** for each problem before the solution
2. **Clear separation** between different problems with divider lines
3. **Consistent structure** for each solution section:

   * Problem statement
   * Solution file name
   * Implementation approach
   * Example usage
4. **Better formatting** of the multiples count output for readability
5. **Standardized terminology** throughout the document
