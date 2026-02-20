# To check valid AZ string 

str5=input("enter your string")
start=str5[:1]
end=str5[-1:]
if(start=='A'):
    if(end=='Z'):
        print("valid AZ string")
    else:
        print("Starts with A but invalid end")
else:
    print("Invalid string")