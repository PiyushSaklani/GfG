#? Feb 7, 2023
#TODO Complete the Question

#? Way 1
# list_1 = list(map(int,input().split()))
# print(sum(list(filter(lambda x:x>=0,list_1)))+sum([sorted(list(filter(lambda x:x<0,list_1)))[-1]]))

#? Expanded version of Way 1
# list_1 = list(map(int,input().split()))
# list_2 = list(filter(lambda x:x>=0,list_1))
# list_3 = sorted(list(filter(lambda x:x<0,list_1)))
# print(sum(list_2)+sum([list_3[-1]]))

#? Way 2
#! -1 2 -3 1 4 -5 6 -4 -1 7 -1
# n = int(input())
# list_1 = list(map(int,input().split()))
# max = float('-inf')
# for i,j in enumerate(list_1):
#     print(max) 

#? Way 3