def zad1():
    with open("22_12_08/przyklad_neon.txt") as file:
        list = [e.strip() for e in file]
        len = 0
        for x in list:
            X = x.split()
            if X[0] == "USUN":
                len -= 1
            elif X[0] == "DOPISZ":
                len+= 1
        print(len)

def zad2():
    with open("22_12_08/przyklad_neon.txt") as file:
        list = [e.strip() for e in file]
        komendy = [e.split()[0] for e in list]
        maks = [0,""]
        streak = [0,""]
        for x in komendy:
            if streak[0] == 0:
                streak[0] = 1
                streak[1] = x
            else:
                if x == streak[1]:
                    streak[0]+=1
                else:
                    if streak[0] > maks[0]:
                        maks[0] = streak[0]
                        maks[1] = streak[1]
                    streak[0] = 0
                    streak[1] = ""
        
        print(*maks)

def zad3():
    with open("22_12_08/przyklad_neon.txt") as file:
        list = [e.strip() for e in file]
        dop = []
        for e in list:
            if e.split()[0] == "DOPISZ":
                dop.append(e.split()[1])
        maks = [0,""]
        for x in dop:
            c = dop.count(x)
            if c > maks[0]:
                maks[0] = c
                maks[1] = x
        print(*maks)

def d(word,letter):
    return "".join([word,letter])
def z(word, letter):
    l = list(word)
    l.pop()
    l.append(letter)
    return "".join(l)
def u(word):
    l = list(word)
    l.pop()
    return "".join(l)
def p(word, letter):
    l = list(word)
    for i in range(len(l)):
        if l[i] == letter:
            if letter == "Z":
                l[i] = "A"
            else:
                l[i] = chr(ord(letter)+1)
            break
    return "".join(l)



def zad4():
    with open("22_12_08/przyklad_neon.txt") as file:
        list = [e.strip() for e in file]
        word = ""
        for x in list:
            letter = x.split()[1]
            command = x.split()[0]
            if command == "DOPISZ":
                word = d(word,letter)
            elif command == "ZAMIEN":
                word = z(word,letter)
            elif command == "USUN":
                word = u(word)
            elif command == "PRZESUN":
                word = p(word,letter)
        print(word)


zad4()