from random import random
import matplotlib.pyplot as plt
import random

# n = random.randint(1, 9999999999999)
n = 91
jumlah = 0
x = []
y = []
print(n)


def collatz(n):
    if n % 2 == 0:
        return n / 2
    else:
        return n*3+1


while True:
    n = collatz(n)
    jumlah += 1
    x.append(jumlah)
    y.append(n)
    # print(int(jumlah))
    if n == 1:
        break


plt.plot(x, y)
plt.show()
