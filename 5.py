#? Feb 7, 2023
#? Way 1
# print(sorted(list(map(int,input().split()))))
#? Using Sorted() function

#? Way 2
list_1 = list(map(int,input().split()))
l,h = 0,len(list_1)-1
while l <= h:
    if list_1[l] > 0:
        if list_1[h] < 0:
            list_1[l], list_1[h] = list_1[h], list_1[l]
        else:
            h -= 1
    else:
        l += 1
print(list_1)