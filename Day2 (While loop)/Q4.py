# Q4: Count even and odd digits in a number
num4=eval(input())
even=0
odd=0
while(num4>0):
    digit=num4%10
    if(digit%2==0):
        even+=1
    else:
        odd+=1
    num4=num4//10
print(even,odd)
