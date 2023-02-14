#? Feb 7, 2023

#? Way 1
# print(sorted(list(map(int,input().split()))))
#? Using Sorted() function

#? Way 2
# list_1 = list(map(int,input().split()))
# new_list = list()
# for i in range(len(list_1)):
#     new_list.append(min(list_1))
#     list_1.remove(min(list_1))
# print(new_list)

#? Way 3
list_1 = list(map(int,input().split()))
l,m,h = 0,0,len(list_1)-1

while m <= h:
    if list_1[m] == 0:
        list_1[l], list_1[m] = list_1[m], list_1[l]
        l += 1
        m += 1
    elif list_1[m] == 1:
        m += 1
    elif list_1[m] == 2:
        list_1[h], list_1[m] = list_1[m], list_1[h]
        h -= 1