# To check Palindrome String
str=input("enter your string")
if(str==str[::-1]):
    print("Given string is a palindrome")
else:
    print("Not a palindrome")