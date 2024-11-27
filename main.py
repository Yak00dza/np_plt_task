import numpy as np
import matplotlib.pyplot as plt

def make_parabola(a, b, c):
    return lambda x: a*(x**2) + b*x + c

a, b, c = map(int, input('Enter values for a b and c ').split())


f = make_parabola(a, b, c)
x = np.linspace(-8, 8, 10000)
y1 = np.array(list(map(f, x)))
y2 = np.log2(x)

plt.plot(x, y1, label='parabola')
plt.plot(x, y2, label='log2')

plt.xlabel('x')
plt.ylabel('y')

plt.legend()
plt.grid(True)
plt.savefig('plot.png')
plt.show()

