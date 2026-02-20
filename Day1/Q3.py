# To Identify last character whether it is digit, alphabet or special symbol
str1 = input("enter your string")
last = str1[-1]

if(last.isdigit()):
    print("Ends with digit")
elif(last.isalpha()):
    print("Ends with character")
elif(not last.isalnum()):
    print("Ends with special symbol")