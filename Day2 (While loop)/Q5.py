# Q5: Check whether a number is palindrome or not
num5=eval(input())
n1=num5
rev=0
while(num5>0):
    digit=num5%10
    rev=rev*10+digit
    num5=num5//10
if(rev==n1):
    print("Palindrome number")
else:
    print("Not a palindrome")
print(rev)
