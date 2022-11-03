def Div(n):
    for i in range(2,n):
        if n%i == 0:
            return True
    return False 
        
def Prime(number):
    list = [2]
    for i in range(2,number):
        if not Div(i):
            list.append(i)
    return list

def zad1():
    with open("11_03_22/pary.txt") as file:
        list = []
        for x in file:
            list.append(x.split())
        for e in list:
            n = int(e[0])
            if n%2 == 0:
                p = Prime(n)
                l = []
                for x in p:
                    t = False
                    for y in p:
                        if y >= x and y + x == n:
                            l.append(y)
                            l.append(x)
                            t = True
                    if t:
                        break
                print(e[0],*l)

def zad2():
    with open("11_03_22/pary.txt") as file:
        list = []
        for x in file:
            list.append(x.split())
        for e in list:
            word = e[1]
            max = ["",0]
            streak = 0
            letter = ""
            for i in range(len(word)) :
                if i == 0:
                    letter = word[i]
                    streak += 1
                elif word[i] == letter:
                    streak += 1
                elif word[i] != letter:
                    if streak > max[1]:
                        max[1]  = streak
                        max[0] = letter
                    streak = 1
                    letter = word[i]
            print(max[0]*max[1],max[1])


def zad3(): #TODO
    with open("11_03_22/przyklad.txt") as file:
        list1 = []
        for x in file:
            list1.append(x.split())       
        list = []
        for y in list1:
            if int(y[0]) == len(y[1]):
                list.append(y)
        min = [0,""]
        for e in list:
            n = "".join(sorted(e[1]))
            if min[0] == 0 and min[1] == "":
                min[0] = e[0]
                min[1] = e[1]
            elif n < e[1]:
                min[0] = e[0]
                min[1] = e[1]
        print(*min)
            
           
#zad1()
#zad2()
zad3()