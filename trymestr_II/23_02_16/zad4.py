with open("trymestr_II/23_02_16/dane4.txt") as file:
    T = [int(e.strip()) for e in file]
max = [0,0]
for i in range(len(T)):
    counter = 0
    for j in range(0,i):
        if T[i]>T[j]:
            counter += 1
    if counter > max[0]:
        max = [counter,i]
print(max[1]+1)

