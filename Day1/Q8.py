# To check valid invalid format

str6=input("Enter yoour string")
f2=str6[:2]
l2=str6[-1:-3:-1]
if(f2.isdigit()):
    if(l2.isalpha()):
        print("Valid format")
else:
    print("Invalid format")