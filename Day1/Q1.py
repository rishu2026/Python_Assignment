# To Identify Valid and Invalid Slice
lst=[1,2,3,1,2]
if(lst[:2]==lst[len(lst)-2:len(lst)]):
    print("Valid slice")
else:
    print("Invalid slice")