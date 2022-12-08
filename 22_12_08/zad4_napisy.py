def zad1():    
    with open("22_12_08/napisy.txt") as file:
        list = []
        for e in file:
            list.append(e.strip())
        counter = 0
        for x in list:
            for i in range(len(x)):
                if x[i].isnumeric() :
                    counter +=1

        print(counter)

def zad2():
    with open("22_12_08/napisy.txt") as file:
        list = []
        for e in file:
            list.append(e.strip())
        index = 0
        haslo = []
        for i in range(19,1001,20):
            haslo.append(list[i][index])
            index += 1

        print("".join(haslo))
    
def zad3():
    with open("22_12_08/napisy.txt") as file:
        list = []
        for e in file:
            list.append(e.strip())
        tekst = []
        for x in list:
            p1 = "".join([x,x[0]])
            p2 = "".join([x[-1],x])
            if p1[0:25:] == p1[-1:25:-1]:
                tekst.append(p1[25])
            elif p2[0:25:] == p2[-1:25:-1]:
                tekst.append(p2[25])
        
        print("".join(tekst))

def zad4():
    with open("22_12_08/napisy.txt") as file:
        list = []
        for e in file:
            list.append(e.strip())
        haslo = []
        for x in list:
            nums = []
            for i in range(50):
                if x[i].isnumeric():
                    nums.append(x[i])
            if len(nums) == 0 or len(nums)==1:
                continue
            if len(nums)%2 != 0:
                nums.pop
            pary = []
            for y in range(0,len(nums)-1,2):
                pary.append(int("".join([nums[y],nums[y+1]])))
            for z in pary:
                if z>= 65 and z <= 90:
                    haslo.append(chr(z))
            if len(haslo)>=3 and haslo[-3::] == ["X","X","X"]:
                break
        
        print("".join(haslo))

