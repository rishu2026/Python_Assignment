lst=[1,2,3,4]
ls=[6,7,8,9]
merge=[]
i=j=0

while(i<len(lst) and j<len(ls)):
    if(lst[i]<ls[j]):
        merge.append(lst[i])
        i+=1
    else:
        merge.append(ls[j])
        j+=1

while(len(lst)>i):
    merge.append(lst[i])
    i+=1

while(len(ls)>j):
    merge.append(ls[j])
    j+=1

print(merge)