# Q2: Reverse a number and compare it with original number
num1=eval(input())
num2=num1
rev=0
while(num1>0):
    ldigit=num1%10
    rev=rev*10+ldigit
    num1=num1//10
print(rev)
if(rev>num2):
    print("Reverse is greater than number")
elif(rev==num2):
    print("Reverse is equal to the number")
else:
    print("Reverse is smaller than number")
