import random
import time
import numpy as np
from numba import njit


# обычный Монте-Карло,аналитический метод (не геометрический)
@njit
def Monte_Carlo(func, n=10000000, a=0, b=1):
    u_rand = np.zeros(n)
    integral = 0
    for i in range(len(u_rand)):
        u_rand[i] = random.uniform(a, b)
        integral += func(u_rand[i])
    answer = (b - a) / float(n) * integral
    return answer


# пример неберущегося интеграла
@njit
def func(x):
    return np.sin(np.pi * x ** 2 / 2)


if __name__ == "__main__":
    start = time.time()
    integral = Monte_Carlo(func)
    end = time.time()
    print('Монте Карло без multiprocessing', integral, 'время работы:', end - start, sep=' ')

#итог: до numba интеграл считался за ~ 49 секунд, с numba - 1,3
