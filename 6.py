#? Feb 7, 2023

#? Way 1
# n,m = input().split()
# print(len(set(map(int,input().split())).union(set(map(int,input().split())))))
#? Using .union() function
#* A[] = array
#* B[] = array
#* A.union(B)

#? Way 2
# n,m = input().split()
# print(len(set(list(map(int,input().split()))+list(map(int,input().split())))))

#? Way 3
n, m = input().split()
a = list(map(int,input().split()))
b = list(map(int,input().split()))

for i in b:
    a.append(i)

print(len(set(a)))