def Sum(string):
    ans = 0
    for i in range(6):
        ans += int(string[i])
    return ans

def Pal(s):
    return True if s == s[::-1] else False
        
def Pop(s):
    sum = 7*Num(s[0]) + 3*Num(s[1]) + Num(s[2]) + 7*int(s[4]) + 3*int(s[5]) + int(s[6]) + 7*int(s[7]) + 3* int(3[8])
    if sum == int(s[3]):
        return True
    else:
        return False

def Num(n):
    return ord(n) - 55

def zad1():
    with open("22_11_10/identyfikator.txt") as file:
        max = 0
        list = []
        for x in file:
            list.append(x.strip())
        for y in list:
            n = y[3:]
            sum = Sum(n)
            if sum > max:
                max = sum
        for z in list:
            if Sum(z[3:]) == max:
                print(z)

def zad2():
    with open("22_11_10/identyfikator.txt") as file:
        list = []
        for x in file:
            list.append(x.strip())
        for y in list:
            if Pal(str(y[:3])) or Pal(str(y[3:])):
                print(y)

def zad3():
    with open("22_11_10/identyfikator.txt") as file:
        list = []
        for x in file:
            list.append(x.strip())

        
# zad1()
# zad2()
