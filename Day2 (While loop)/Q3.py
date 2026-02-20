# Q3: Find single digit sum of a number (repeat sum until single digit)
num = int(input("Enter Number: "))

while num > 9:
    s = 0
    while num > 0:
        s += num % 10
        num = num // 10
    num = s  
print("Single Digit Sum:", num)
