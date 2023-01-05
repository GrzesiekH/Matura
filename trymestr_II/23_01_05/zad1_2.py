n = int(input())
A = list(map(int,input().split()))
L = []
for i in range(n):
    L.append(0)
counter  = 0
for x in range(0,n):
    if A[x] > n:
        counter += 1
    
    elif L[A[x]] == 0:
        L[A[x]] = 1
for e in L:
    if e == 0:
        counter += 1

print(counter)