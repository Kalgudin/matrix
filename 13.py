from random import randint

I = 2 #Строчки(i)
J = 3 #Столбцы(j)
A = 0

m = []
b = []

for i in range(I):
    s = []
    for j in range(J):
        s.append(randint(0,2))
    m.append(s)
    print(s)

for j in range(J):
    res = 0
    for i in range(I-1):
        if m[i][j] < m[i+1][j]:
            res = 1
        else:
            res = 0
            break
    b.append(res)

print('====================')
print(b)
