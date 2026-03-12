import random

N = 3
m = []  # исходная матрица
m2 = []  # итоговая матрица
for i in range(N * 2):
    s = []
    s2 = []
    for j in range(N):
        s.append(random.randint(0,10))
        s2.append(None)  # создаем пустую матрицу 2N*N
    print(s)

    m.append(s)
    m2.append(s2)
print('- - - - - - - - - - ')  # просто пропускаю строчку, чтобы удобно было смотреть результат
# ------------- 16 -----------------
# задача слепить матрицу из столбцов в кторых чередуются элементы(последний-средний-предпоследний-средний-1....)
for i in range(N):

    for j in range(N):
        m2[j * 2][i] = m[N * 2 - 1 - j][i]
        m2[j * 2 + 1][i] = m[N - 1 - j][i]

for i in range(N * 2):
    print(m2[i])