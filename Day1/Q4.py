# To check starting character of string

str2=input("enter your string")
first=str2[0:1]
last=str2[-1:]
if(first.isupper()):
    print("starts with Uppercase")
elif(last.islower()):
    print("Ends with lowercase")
else:
    print("Other case")

