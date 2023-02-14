#? Feb 7, 2023
#? Way 1
# list_1 = list(map(int,input().split()))
# print([list_1[-1]] + list_1[:-1])

#? Way 2
list_1 = list(map(int,input().split()))
new_list = [list_1[-1]]
for i in range(len(list_1)-1):
    new_list.append(list_1[i])
print(new_list)