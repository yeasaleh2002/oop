# python operators
# 1. Arithmetic operators
# 2. Assignment operators
# 3. Comparison operators
# 4. Logical operators
# 5. Identity operators
# 6. Membership operators
# 7. Bitwise operators

# 1. Arithmetic operators
# +	Addition	x + y
# -	Subtraction	x - y
# *	Multiplication	x * y
# /	Division	x / y

x = 10
y = 3
print(x + y)  # Output: 13
print(x - y)  # Output: 7
print(x * y)  # Output: 30

# 2. Assignment operators
# =	x = 5	x = 5
# +=	x += 3	x = x + 3
# -=	x -= 3	x = x - 3
# *=	x *= 3	x = x * 3
# /=	x /= 3	x = x / 3
# %=	x %= 3	x = x % 3
# //=	x //= 3	x = x // 3

x = 10
x += 5
print(x)  # Output: 15

# 3. Comparison operators
# ==	Equal	x == y
# !=	Not equal	x != y
# >	Greater than	x > y
# <	Less than	x < y
# >=	Greater than or equal to	x >= y
# <=	Less than or equal to	x <= y

x = 10
y = 5
print(x == y)  # Output: False
print(x != y)  # Output: True
print(x > y)  # Output: True

# 4. Logical operators
# and 	Returns True if both statements are true	x < 5 and  x < 10

x = 5
y = 10
print(x < 5 and y < 10)  # Output: True

# or    Returns True if one of the statements is true    x < 5 or x < 2
print(x < 5 or y < 2)  # Output: False

# not   Reverse the result, returns False if the result is true    not (x < 5 and x < 10)

print(not (x < 5 and y < 10))  # Output: False

# 5. Identity operators
# is 	Returns True if both variables are the same object	x is y
# is not	Returns True if both variables are not the same object	x is not y

x = 5
y = 5
print(x is y)  # Output: True

# 6. Membership operators

# in 	Returns True if a sequence with the specified value is present in the object	x in y
# not in	Returns True if a sequence with the specified value is not present in the object	x not in y

x = [1, 2, 3]
y = 2
print(y in x)  # Output: True

# 7. Bitwise operators
# & 	AND	Sets each bit to 1 if both bits are 1
# |	OR	Sets each bit to 1 if one of two bits is 1
# ^	XOR	Sets each bit to 1 if only one of two bits is 1
# ~ 	NOT	Inverts all the bits
# <<	Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off

x = 10
y = 4
print(x & y)  # Output: 4
print(x | y)  # Output: 14
print(x ^ y)  # Output: 6

print(~x)  # Output: -11
print(x << 2)  # Output: 40
print(x >> 2)  # Output: 2

# Bitwise operator precedence:
# 1. ~
# 2. <<, >>

# 3. &
# 4. ^
# 5. |

# 6. Comparison operators
# 7. Logical operators
# 8. Assignment operators
# 9. Arithmetic operators
# 10. Membership operators
# 11. Identity operators

# 12. **  Exponentiation

x = 2
y = 3
print(x ** y)  # Output: 8

# 13. Floor division operator

x = 10
y = 3
print(x // y)  # Output: 3

# 14. Modulo operator

x = 10
y = 3
print(x % y)  # Output: 1

# 15. Ternary operator

x = 10
y = 20
print("x is greater than y" if x > y else "x is less than or equal to y")  # Output: x is less than or equal to y

# 16. Elif statement

x = 10
y = 20
if x > y:
    print("x is greater than y")
elif x < y:
    print("x is less than y")
    print("This is inside elif block")
else:
    print("x is equal to y")
    print("This is inside else block")
    print("This is also inside else block")

    # 17. Nested if statement
    if x > 5:
        if x < 10:
            print("x is greater than 5 and less than 10")
        else:
            print("x is greater than 5 but not less than 10")
    else:
        print("x is not greater than 5")
        if x < 10:
            print("x is less than 10")
            if x == 5:
                print("x is equal to 5")
                print("This is nested if block")
            else:
                print("x is not equal to 5")
                print("This is nested else block")
        else:

            print("x is not less than 10")
            print("This is else block")
            print("This is also else block")
            print("This is the last else block")
# 18. Pass statement

x = 10
if x > 5:
    pass  # This is a placeholder statement, it doesn't do anything

# 19. Break statement

x = 1
while x <= 5:
    print(x)
    if x == 3:
        break  # This will exit the loop when x becomes 3
    x += 1
    print("This is inside while loop")
print("This is outside while loop")

# 20. Continue statement

x = 1
while x <= 5:
    if x == 3:
        x += 1
        continue  # This will skip the current iteration and move to the next iteration 
    print(x)
    x += 1
    print("This is inside while loop")
    print("This is also inside while loop")
    print("This is the last line of inside while loop") 
    print("This is the last line of the while loop")
print("This is outside while loop")

# 21. Global keyword

x = 10
def change_value():
    global x
    x = 20
    print(x)
change_value()
print(x)

# 22. Local keyword

def change_value_local():
    x = 30
    print(x)
change_value_local()
print(x)  # This will raise an error because x is not defined in the global scope

# 23. Nonlocal keyword

def outer_function():
    x = 10
    def inner_function():
        nonlocal x
        x = 20
        print(x)
    inner_function()
    print(x)
outer_function()

# 24. Lambda function   
# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.
# Syntax: lambda arguments : expression

x = lambda a, b : a * b
print(x(5, 6))  # Output: 30
