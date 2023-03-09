def zad1(num,base):
    decNum = 0
    m = 1
    while num > 0:
        l = num%10
        decNum += l*m
        m *= base
        num //= 10
    return decNum

def dec2Base(num,base):
    baseNum = 0
    d = 1
    while num > 0:
        l = num%base
        baseNum += l*d
        d *= 10
        num //= base
    return baseNum



def zad2(x,aT):
    sum = 0
    i = 1
    for e in aT:
        sum += e*i
        i *= x
    return sum 

def zad3(x,aT):
    i = len(aT)-1
    y = aT[i]
    while i != 0:
        i -=1
        y = y*x + aT[i]
    return y

def Funkcja(k):
    if k <= 2:
        return 1
    if k%2 == 0:
        k //= 2
        a = Funkcja(k+1)
        b = Funkcja(k-1)
        return a*a - b*b
    else:
        k = (k+1)//2
        a = Funkcja(k)
        b = Funkcja(k-1)
        return a*a + b*b
