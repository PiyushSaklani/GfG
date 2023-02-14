#? Feb 7, 2023
list_1 = list(input().split())
#? Can be done by two ways

#? Way 1
for i in range(int(len(list_1)/2)):
    list_1[i], list_1[-(i+1)] = list_1[-(i+1)], list_1[i]
print(list_1)

#? Way 2
print(list_1[::-1])