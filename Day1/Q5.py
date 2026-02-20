# To check which half is greater

lst = [4,3,1,2]

mid = len(lst) // 2
f_half = lst[:mid]
s_half = lst[mid:]

if sum(f_half) > sum(s_half):
    print("First Half Greater")
elif sum(f_half) == sum(s_half):
    print("Equal halves")
else:
    print("Second Half Greater")