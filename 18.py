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

for i in range(M):
    for j in range(N):
        if m[i][j] == A:
            res.append(j*i)
print('========================')
print(res)