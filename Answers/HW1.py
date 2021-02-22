import  random

# sayac=0
ekle= [[91, 29, 9],
    [95, 85, 37],
    [9, 87, 93]]

# while sayac != 9:
#     num = random.randint(1,100)
#
#     for i in range(2, num):
#         if (num % i) == 0:
#             print(num, "is not a prime number")
#             break
#         else:
#             print(num, "is a prime number")
#             sayac += 1
#             break
#
# print(list)

n = 3
a = [[0] * n for i in range(n)]
for i in range(n):
    for j in range(0, i):
        a[i][j] = ekle[i][j]
    a[i][i] = ekle[i][i]
    for j in range(i + 1, n):
        a[i][j] = ekle[i][j]
for row in a:
    print(' '.join([str(elem) for elem in row]))






