n = int(input())
A = list(map(int,input().split()))
L = []
for i in range(n):
    L.append(i+1)
counter  = 0
for x in L:
    for y in A:
        if x == y:
            counter -=1
            break 
    counter += 1

print(counter)