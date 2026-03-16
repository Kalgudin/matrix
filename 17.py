from random import randint
M = 3
N = 8
A = 1

m = []
res = []

for i in range(M):
    s = []
    for j in range(N):
        s.append(randint(0,2))
    m.append(s)
    print(s)
for i in range(N):
    counter = 0
    for j in range(M):
        if m[j][i] == A:
            counter += 1
    res.append(counter)
print('====================')
print(res)
# вариант по строчкам
res2 = []
for i in m:
    counter = 0
    for j in i:
        if j == A:
            counter += 1
    res2.append(counter)
print('====================')
print(res2)