with open("symetryczne.txt") as dane:
    T = [e.strip().split() for e in dane]
c = {2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0,13:0,14:0,15:0,16:0}
n = len(T)
for i in range(n):
    number = T[i][1]
    if len(number) >= 2 and number == number[::-1]:
        c[int(T[i][0])] += 1
for x in c:
    print(x,c[x])

c = 0
TDec = []
for e in T:
    TDec.append(int(e[1], base=int(e[0])))
for i in range(len(TDec)):
    iString = str(TDec[i])
    iLen = len(iString)
    for j in range(2,iLen-2):
        A = iString[0:j]
        B = iString[j:iLen]
        if A == A[::-1] and B == B[::-1] and int(A)>=0 and int(B)>=10:
            c += 1
            break

print(c)


def dec2Bin(n):
    nBin = 0
    l = 1
    while n !=0:
        t = n%2
        nBin += l*t
        n //= 2
        l*=10
    return nBin

m = [0,0,0,0]#len,dec, org, bin
for e in T:
    eDec = int(e[1],base=int(e[0]))
    eBin = dec2Bin(eDec)
    if str(eBin) == str(eBin)[::-1]:
        if len(str(eBin)) > m[0]:
            m[0],m[1],m[2],m[3] = len(str(eBin)), eDec, e[1], eBin

print(*m)


def isPrime(n):
    i = 2
    while i <n:
        if n%i == 0:
            return False
        i += 1
    return True

c = 0
for e in TDec:
    x = isPrime(e)
    if isPrime(e) and str(e) == str(e)[::-1]:
        c+= 1
print(c)

