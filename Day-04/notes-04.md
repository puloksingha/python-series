# Day 04 - Control Flow and Logical Operators

## What is Control Flow?

**Control flow** refers to the order in which statements are executed in a program. By default, Python executes statements from the top to the bottom, one after another. However, control flow structures allow you to change this execution order by making decisions based on certain conditions.

Control flow is essential for writing programs that can:
- Make decisions based on conditions
- Repeat actions multiple times
- Skip certain code blocks
- Execute different code based on different scenarios

---

## Conditional Statements (if/else)

A **conditional statement** is a programming construct that allows you to execute different blocks of code depending on whether a certain condition is true or false.

### The if Statement

The **if statement** is used to execute a block of code only if a condition is true.

### Syntax:

```python
if condition:
    # Code to execute if condition is True
    statement
```

### Key Points:
- The condition is evaluated to either `True` or `False`
- If the condition is `True`, the indented block of code is executed
- If the condition is `False`, the code block is skipped
- Indentation is crucial and defines the scope of the if block

### Example:

```python
age = 18
if age >= 18:
    print("You are an adult.")
```

In this example:
- We check if `age >= 18` (is age greater than or equal to 18?)
- Since `age` is 18, the condition is `True`
- The print statement is executed, outputting: "You are an adult."

---

### The if-else Statement

The **if-else statement** is used to execute one block of code if a condition is true, and another block of code if the condition is false. It allows you to provide two alternative paths of execution.

### Syntax:

```python
if condition:
    # Code to execute if condition is True
    statement1
else:
    # Code to execute if condition is False
    statement2
```

### Key Points:
- The `else` keyword introduces an alternative block
- The else block is executed only if the condition in the if statement is `False`
- Both blocks cannot be executed in the same run; only one will execute
- Proper indentation is necessary for both blocks

### Example:

```python
age = 16
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")
```

In this example:
- We check if `age >= 18`
- Since `age` is 16, the condition is `False`
- The else block is executed, printing: "You are a minor."

---

### The if-elif-else Statement

The **if-elif-else statement** is used when you need to check multiple conditions. The `elif` keyword stands for "else if" and allows you to test multiple conditions in sequence.

### Syntax:

```python
if condition1:
    # Code to execute if condition1 is True
    statement1
elif condition2:
    # Code to execute if condition1 is False and condition2 is True
    statement2
elif condition3:
    # Code to execute if condition1 and condition2 are False and condition3 is True
    statement3
else:
    # Code to execute if all conditions are False
    statement4
```

### Key Points:
- You can have multiple `elif` blocks
- Python checks conditions from top to bottom
- Once a condition is found to be `True`, that block is executed and the rest are skipped
- The `else` block at the end is optional and acts as a catch-all
- If none of the conditions are true and there's no `else`, nothing is executed

### Example:

```python
age = 65
if age < 18:
    print("You are a minor.")
elif age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")
```

In this example:
- First, we check if `age < 18` (is age less than 18?) → `False`
- Since the first condition is false, we check the next: `elif age < 65` (is age less than 65?) → `False`
- Since both conditions are false, we execute the `else` block
- Output: "You are a senior citizen."

---

## Logical Operators

**Logical operators** are used to combine multiple conditions in a single statement. They allow you to create more complex conditional expressions by combining simpler conditions.

Python has three logical operators:
1. **and** - Returns `True` if all conditions are true
2. **or** - Returns `True` if at least one condition is true
3. **not** - Reverses the result of a condition

---

### The and Operator

The **and** operator is used to combine multiple conditions. It returns `True` only if all conditions are `True`. If any condition is `False`, the entire expression is `False`.

### Syntax:

```python
if condition1 and condition2:
    # Code executes only if both condition1 AND condition2 are True
    statement
```

### Truth Table for and:

| condition1 | condition2 | condition1 and condition2 |
|------------|-----------|---------------------------|
| True       | True      | True                      |
| True       | False     | False                     |
| False      | True      | False                     |
| False      | False     | False                     |

### Example:

```python
age = 25
if age >= 18 and age < 65:
    print("You are an adult.")
```

In this example:
- First condition: `age >= 18` → `25 >= 18` → `True`
- Second condition: `age < 65` → `25 < 65` → `True`
- Both conditions are `True`, so the `and` operator returns `True`
- The print statement is executed, outputting: "You are an adult."

### More Examples:

```python
# Example 1: Both conditions are true
name = "Alice"
age = 30
if name == "Alice" and age > 25:
    print("This is Alice and she is over 25.")  # This will execute

# Example 2: One condition is false
score = 70
if score >= 80 and score <= 100:
    print("Excellent score!")  # This will NOT execute (70 is not >= 80)
```

---

### The or Operator

The **or** operator is used to combine multiple conditions. It returns `True` if at least one of the conditions is `True`. It returns `False` only if all conditions are `False`.

### Syntax:

```python
if condition1 or condition2:
    # Code executes if condition1 OR condition2 (or both) are True
    statement
```

### Truth Table for or:

| condition1 | condition2 | condition1 or condition2 |
|------------|-----------|--------------------------|
| True       | True      | True                     |
| True       | False     | True                     |
| False      | True      | True                     |
| False      | False     | False                    |

### Example:

```python
age = 70
if age < 18 or age >= 65:
    print("You are not an adult.")
```

In this example:
- First condition: `age < 18` → `70 < 18` → `False`
- Second condition: `age >= 65` → `70 >= 65` → `True`
- Since at least one condition is `True`, the `or` operator returns `True`
- The print statement is executed, outputting: "You are not an adult."

### More Examples:

```python
# Example 1: One condition is true
day = "Saturday"
if day == "Saturday" or day == "Sunday":
    print("It's the weekend!")  # This will execute

# Example 2: Both conditions are false
temperature = 60
if temperature > 30 or temperature < 0:
    print("Extreme temperature!")  # This will NOT execute
```

---

### The not Operator

The **not** operator is used to reverse or negate a condition. It returns `True` if the condition is `False`, and `False` if the condition is `True`. The `not` operator is a unary operator (it works with only one operand).

### Syntax:

```python
if not condition:
    # Code executes if condition is False
    statement
```

### Truth Table for not:

| condition | not condition |
|-----------|---------------|
| True      | False         |
| False     | True          |

### Example:

```python
age = 15
if not age >= 18:
    print("You are a minor.")
```

In this example:
- The condition is `age >= 18` → `15 >= 18` → `False`
- The `not` operator reverses this: `not False` → `True`
- The print statement is executed, outputting: "You are a minor."

This is equivalent to writing:
```python
age = 15
if age < 18:
    print("You are a minor.")
```

### More Examples:

```python
# Example 1: Using not with a variable
is_raining = False
if not is_raining:
    print("Let's go outside!")  # This will execute

# Example 2: Using not with a condition
score = 50
if not score >= 70:
    print("You did not pass the test.")  # This will execute
```

---

## Combining Multiple Logical Operators

You can combine multiple logical operators in a single statement to create more complex conditions.

### Example:

```python
age = 35
income = 50000

if (age >= 30 and age <= 60) or income > 100000:
    print("You qualify for the loan.")
```

In this example:
- First part: `(age >= 30 and age <= 60)` → `(35 >= 30 and 35 <= 60)` → `(True and True)` → `True`
- Second part: `income > 100000` → `50000 > 100000` → `False`
- Combined with `or`: `True or False` → `True`
- The print statement is executed

### Order of Operations:

When combining logical operators, Python evaluates them in this order:
1. `not` (highest priority)
2. `and`
3. `or` (lowest priority)

You can use parentheses to override the default order and make your conditions clearer.

---

## Key Takeaways

- **Control flow** allows you to make decisions and change the order of execution in your programs
- **if statements** execute code only when a condition is true
- **if-else statements** provide an alternative path when the condition is false
- **if-elif-else statements** allow you to check multiple conditions in sequence
- **Logical operators** (`and`, `or`, `not`) let you combine and negate conditions
- **Proper indentation** is crucial for defining code blocks in Python
- **Conditions are evaluated** as either `True` or `False`
- **Use parentheses** to make complex conditions clear and readable
