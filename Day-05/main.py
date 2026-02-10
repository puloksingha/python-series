# loops 
# for loop
for i in range(5):
    print(i)
# while loop
i = 0
while i < 5:
    print(i)
    i += 1  # incrementing the value of i by 1(i = i + 1)

# nested loop
for i in range(3):
    for j in range(2):
        print(f'i: {i}, j: {j}')
# break statement
for i in range(5):
    if i == 3:
        break  # exit the loop when i is 3
    print(i)
# continue statement
for i in range(5):
    if i == 3:
        continue  # skip the rest of the loop when i is 3
    print(i)    
'''type of loops:
1. for loop: used to iterate over a sequence (like a list, tuple, or string) or a range of numbers.
2. while loop: used to execute a block of code as long as a specified condition is true.
3. nested loop: a loop inside another loop, used to perform more complex iterations.    
4. break statement: used to exit a loop prematurely when a certain condition is met.
5. continue statement: used to skip the current iteration of a loop and move to the next iteration when a certain condition is met.'''

# do while loop is not available in python but we can simulate it using while loop
i = 0
while True:
    print(i)
    i += 1
    if i >= 5:
        break  # exit the loop when i is 5 or greater

# for loop with else statement
for i in range(5):
    print(i)    
else:    print("Loop completed successfully without break")  # this will be executed if the loop completes without a break statement
# while loop with else statement
i = 0
while i < 5:
    print(i)
    i += 1  
else:    print("Loop completed successfully without break")  # this will be executed if the loop completes without a break statement

# nested loop with else statement
for i in range(3):
    for j in range(2):
        print(f'i: {i}, j: {j}')
else:    print("Nested loop completed successfully without break")  # this will be executed if the nested loop completes without a break statement  
