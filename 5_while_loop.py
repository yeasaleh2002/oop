num = 1

# break statement
# while num < 10: 
#     print(f"The current number is {num}")
#     num += 1
#     if num == 5:
#         break
  

num1 = 1

# continue- it is working as skipping the current iteration and moving to the next iteration
while num1 <= 10:
    num1 += 1
    if num1 % 2 == 1:
        continue
    print(f"The current number is {num1}")
