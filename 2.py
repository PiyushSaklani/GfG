#? Feb 7,2023
#? Way 1
# list_1 = list(map(int,input().split()))
# print(max(list_1),min(list_1))
#? Using max() & min() function

#? Way 2
list_1 = list(map(int,input().split()))
max,min = 0,float('inf')
for i in list_1:
    if max < i:
        max = i
    elif min > i:
        min = i
print(max,min)