# To check slice with same element or slice with different element

lst2=[1,2,3,2,6]
f2=lst2[:2]
l2=lst2[len(lst2)-2:len(lst2)]
if(len(lst2)%2==0):
    if(f2==l2):
        print("slice with same element")
    else:
        print("Slices are different")
else:
    print("Odd Length list")
