# args 

def all_sum(*numbers):
    print(numbers)
    sum = 0
    for num in numbers:
        print(num)
        sum += num
    return sum

total = all_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print("Sum: ", total)  # Output: 55