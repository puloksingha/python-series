# Day 05 - Loops

## What are Loops?

A **loop** is a programming construct that allows you to execute a block of code repeatedly without having to write the same code multiple times. Loops are essential for automating repetitive tasks and processing collections of data.

Loops help you:
- Execute code multiple times with minimal effort
- Process items in sequences like lists, tuples, or strings
- Repeat actions a specific number of times
- Reduce code duplication

---

## Types of Loops in Python

### 1. for Loop

The **for loop** is used to iterate over a sequence (like a list, tuple, string, or range of numbers). It executes the indented code block once for each item in the sequence.

#### Syntax:

```python
for variable in sequence:
    # Code to execute for each item
    statement
```

#### Key Points:
- The `variable` takes the value of each item in the sequence one at a time
- The loop continues until all items in the sequence have been processed
- Indentation is crucial and defines the code block to execute in each iteration

#### Example with range():

```python
for i in range(5):
    print(i)  # Output: 0, 1, 2, 3, 4
```

In this example:
- `range(5)` generates numbers from 0 to 4 (5 is exclusive)
- The variable `i` takes each value one by one
- The print statement is executed 5 times

#### Example with a list:

```python
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(fruit)
```

---

### 2. while Loop

The **while loop** is used to execute a block of code as long as a specified condition is true. It keeps repeating until the condition becomes false.

#### Syntax:

```python
while condition:
    # Code to execute while condition is True
    statement
    # Don't forget to modify the condition variable
```

#### Key Points:
- The condition is checked before each iteration
- If the condition is true, the block executes
- If the condition is false, the loop stops
- You must update the condition variable to avoid infinite loops
- Indentation defines the code block to execute in each iteration

#### Example:

```python
i = 0
while i < 5:
    print(i)
    i += 1  # Incrementing i by 1 (same as i = i + 1)
# Output: 0, 1, 2, 3, 4
```

In this example:
- We start with `i = 0`
- We check if `i < 5` (is i less than 5?)
- If true, we print `i` and increment it by 1
- This repeats until `i` becomes 5

#### Example with a user condition:

```python
password = ""
while password != "secret":
    password = input("Enter password: ")
print("Access granted!")
```

---

### 3. Nested Loops

A **nested loop** is a loop inside another loop. The inner loop executes completely for each iteration of the outer loop. This is useful for working with multi-dimensional data or creating patterns.

#### Syntax:

```python
for outer_variable in outer_sequence:
    for inner_variable in inner_sequence:
        # Code to execute in the nested loop
        statement
```

#### Example:

```python
for i in range(3):
    for j in range(2):
        print(f'i: {i}, j: {j}')
```

Output:
```
i: 0, j: 0
i: 0, j: 1
i: 1, j: 0
i: 1, j: 1
i: 2, j: 0
i: 2, j: 1
```

In this example:
- For each value of `i` (0, 1, 2), the inner loop runs completely for each value of `j` (0, 1)
- The inner loop runs 2 times for each iteration of the outer loop
- Total iterations: 3 × 2 = 6

#### Practical Example - Creating a multiplication table:

```python
for i in range(1, 4):
    for j in range(1, 4):
        print(f'{i} × {j} = {i * j}', end='  ')
    print()  # New line after each row
```

---

## Loop Control Statements

Loop control statements allow you to change how loops execute by skipping iterations or exiting early.

### 1. break Statement

The **break statement** exits the loop immediately, even if the condition is still true. All remaining iterations are skipped.

#### Syntax:

```python
for/while condition:
    if another_condition:
        break  # Exit the loop
    statement
```

#### Example:

```python
for i in range(5):
    if i == 3:
        break  # Exit the loop when i is 3
    print(i)
# Output: 0, 1, 2
```

In this example:
- When `i` equals 3, the break statement is executed
- The loop stops immediately
- Values 3 and 4 are not printed

#### Practical Example - Searching for a value:

```python
fruits = ["apple", "banana", "orange", "grape"]
for fruit in fruits:
    if fruit == "orange":
        print(f"Found {fruit}!")
        break
    print(f"Checking {fruit}...")
```

---

### 2. continue Statement

The **continue statement** skips the remaining code in the current iteration and moves to the next iteration of the loop.

#### Syntax:

```python
for/while condition:
    if another_condition:
        continue  # Skip to the next iteration
    statement
```

#### Example:

```python
for i in range(5):
    if i == 3:
        continue  # Skip the rest of the loop when i is 3
    print(i)
# Output: 0, 1, 2, 4
```

In this example:
- When `i` equals 3, the continue statement is executed
- The print statement is skipped for i = 3
- The loop continues with i = 4

#### Practical Example - Skipping even numbers:

```python
for i in range(10):
    if i % 2 == 0:
        continue  # Skip even numbers
    print(i)  # Print only odd numbers
# Output: 1, 3, 5, 7, 9
```

---

## Special Loop Features

### 1. Loop with else Statement

Python allows you to attach an **else block** to loops. The else block executes when the loop completes normally (without hitting a break statement).

#### Syntax:

```python
for variable in sequence:
    if condition:
        break
    statement
else:
    # Code to execute if the loop completes without break
    statement
```

#### Example with for loop:

```python
for i in range(5):
    print(i)
else:
    print("Loop completed successfully without break")
```

Output:
```
0
1
2
3
4
Loop completed successfully without break
```

#### Example with while loop:

```python
i = 0
while i < 5:
    print(i)
    i += 1
else:
    print("Loop completed successfully without break")
```

#### Key Point:
- If the loop encounters a `break` statement, the else block is **skipped**
- If the loop completes normally, the else block **executes**

#### Example demonstrating the difference:

```python
# Loop with break - else block is skipped
for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("This won't print!")  # Not executed

# Loop without break - else block executes
for i in range(5):
    print(i)
else:
    print("This will print!")  # Executed
```

---

### 2. Simulating do-while Loop

Python does not have a built-in **do-while loop** (which executes the code block at least once before checking the condition). However, you can simulate it using a `while True` loop with a `break` statement.

#### Syntax:

```python
while True:
    # Code to execute
    statement
    if condition:
        break  # Exit the loop
```

#### Example:

```python
i = 0
while True:
    print(i)
    i += 1
    if i >= 5:
        break  # exit the loop when i is 5 or greater
# Output: 0, 1, 2, 3, 4
```

In this example:
- The code block executes at least once
- We check the condition at the end
- This mimics the behavior of a do-while loop in other languages

---

### 3. Nested Loop with else Statement

The else block works with nested loops as well. It executes when the nested loop completes without a break.

#### Example:

```python
for i in range(3):
    for j in range(2):
        print(f'i: {i}, j: {j}')
else:
    print("Nested loop completed successfully without break")
```

---

## Range Function

The **range()** function generates a sequence of numbers and is commonly used with for loops.

#### Syntax:

```python
range(start, stop, step)
```

#### Parameters:
- `start`: The starting value (inclusive) - default is 0
- `stop`: The ending value (exclusive) - required
- `step`: The increment between numbers - default is 1

#### Examples:

```python
# range(5) - from 0 to 4
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

# range(2, 7) - from 2 to 6
for i in range(2, 7):
    print(i)  # 2, 3, 4, 5, 6

# range(0, 10, 2) - from 0 to 9, incrementing by 2
for i in range(0, 10, 2):
    print(i)  # 0, 2, 4, 6, 8

# range(10, 0, -1) - from 10 to 1, decrementing by 1
for i in range(10, 0, -1):
    print(i)  # 10, 9, 8, 7, 6, 5, 4, 3, 2, 1
```

---

## Summary of Loops

| Loop Type | Use Case | Condition Check |
|-----------|----------|-----------------|
| **for loop** | Iterating over a sequence or a known number of times | Before each iteration |
| **while loop** | Repeating as long as a condition is true | Before each iteration |
| **do-while** | Executing at least once, then repeating based on a condition | After each iteration |
| **nested loop** | Iterating through multiple dimensions | Varies based on inner/outer loops |

---

## Best Practices for Writing Loops

1. **Keep loops simple** - Complex nested loops are hard to understand
2. **Avoid infinite loops** - Always ensure the loop condition becomes false
3. **Use meaningful variable names** - Instead of `i`, use `num` or `item`
4. **Use for loops for known iterations** - When you know how many times to iterate
5. **Use while loops for conditional iterations** - When the number of iterations depends on a condition
6. **Avoid modifying loop variables inside the loop** - Can lead to unexpected behavior
7. **Use break and continue sparingly** - They can make loops harder to understand
8. **Comment complex loops** - Help others (and your future self) understand the logic

---

## Common Loop Patterns

### Pattern 1: Counting occurrences

```python
count = 0
numbers = [1, 2, 3, 4, 3, 5, 3]
for num in numbers:
    if num == 3:
        count += 1
print(f"Number 3 appears {count} times")
```

### Pattern 2: Finding an element

```python
items = ["apple", "banana", "orange"]
search = "banana"
found = False
for item in items:
    if item == search:
        found = True
        break
if found:
    print(f"{search} found!")
else:
    print(f"{search} not found!")
```

### Pattern 3: Transforming a list

```python
numbers = [1, 2, 3, 4, 5]
squared = []
for num in numbers:
    squared.append(num ** 2)
print(squared)  # [1, 4, 9, 16, 25]
```

---

## Key Takeaways from Day 05

✓ Loops allow you to execute code repeatedly without duplication  
✓ **for loops** are ideal for iterating over sequences  
✓ **while loops** are useful for condition-based repetition  
✓ **break** exits the loop immediately  
✓ **continue** skips to the next iteration  
✓ **else with loops** executes when the loop completes without break  
✓ Nested loops repeat loops within loops for multi-dimensional iteration  
✓ **range()** generates number sequences for iteration  
✓ Proper loop usage prevents infinite loops and makes code more readable
