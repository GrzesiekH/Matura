import math

def nwd(n):
    list = [1]
    l = n
    i = 2
    while l != 1:
        if l%i == 0:
            l = l/i
            list.append(i)
        else:
            i += 1
    
    return list

def wzglPir(a,b):
    aL = nwd(a)
    bL = nwd(b)
    max = 0
    for x in aL:
        for y in bL:
            if x == y and x > max:
                max = x
    return True if max == 1 else False

a = int(input())
b = int(input())
cL = [a**2 + b**2, -a**2 + b**2,a**2- b**2]
for e in cL:
    s = math.sqrt(e)
    if e > 0 and s == round(s):
        if wzglPir(a) and wzglPir(b) and wzglPir(s):
            print("pierwotne",a,b,s)
        else:
            print(a,b,s) #jjjj
    else:
        print(0)
