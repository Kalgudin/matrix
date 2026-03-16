from random import randint

I = 4 #Строчки(i)
J = 3 #Столбцы(j)
A = 0

bm = []
bp = []
m = []
for i in range(I):
    s = []
    for j in range(J):
        s.append(randint(-10,10))
    m.append(s)
    print(s)

for j in range(J):
    pl = 0
    mn = 0
    for i in range(I):
        if m[i][j] > 0:
            pl += 1
        elif m[i][j] < 0:
            mn += 1
        else:
            pass

    bm.append(mn)
    bp.append(pl)

print(f'pluses - {bp}')
print(f"minuses - {bm}")
