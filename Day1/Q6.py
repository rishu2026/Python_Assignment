# To check middle charcter is vowel or not

str4=input("enter your string")
mid=(str4[(len(str4)+1)//2])
if(len(str4)>=5):
    if(mid.lower() in "aeiou" ):
        print("Middle character is a vowel")
    else:
        print("Middle chatrcater is not a vowel")
else:
    print("string too short")

