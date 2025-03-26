nums = [5, 10, 15, 20, 25, 30, 35, 40]

for num in nums:
    print(num)
    if num % 2 == 0:
        print(f"{num} is an even number")
    else:
        print(f"{num} is an odd number")


# 
text = "python test"

for char in text:
    print(char)
    

# range tests range(inclusive, exclusive)
# range(inclusive, exclusive, step)
for i in range(3, 10):
    print(i)