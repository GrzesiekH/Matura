def ONP(s):
    s = s.split()
    T = []
    for i in range(len(s)):
        if s[i] == "+":
            b = T.pop()
            a = T.pop()
            T.append(a+b)
        elif s[i] == "-":
            b = T.pop()
            a = T.pop()
            T.append(a-b)
        elif s[i] == "*":
            b = T.pop()
            a = T.pop()
            T.append(a*b)
        elif s[i] == "/":
            b = T.pop()
            a = T.pop()
            T.append(a/b)
        else:
            T.append(int(s[i]))
    return T[0]


print(ONP("3 4 5 + 4 2 - * +"))