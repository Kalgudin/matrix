from random import randint

I = 40 #Строчки(i)
J = 30 #Столбцы(j)
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
    counter = 0
    for i in range(I):
        if m[i][j] == A:
            counter += 1

    b.append((counter / I) * 100)
print(b)