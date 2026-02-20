# Q8: Count how many times digit 2 appears in a number
b=eval(input())
target=2
count=0
while(b>0):
    digit=b%10
    if(target==digit):
        count+=1
    b=b//10
print(count)
