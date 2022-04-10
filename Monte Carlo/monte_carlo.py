import random
import time
import numpy as np
import multiprocessing


# обычный Монте-Карло,аналитический метод (не геометрический)
def Monte_Carlo(func, n=10000000, a=0, b=1):
    u_rand = np.zeros(n)
    integral = 0
    for i in range(len(u_rand)):
        u_rand[i] = random.uniform(a, b)
        integral += func(u_rand[i])
    answer = (b - a) / float(n) * integral
    return answer


# пример неберущегося интеграла
def func(x):
    return np.sin(np.pi * x ** 2 / 2)


# каждое ядро считаем сумму и добовляет ее в мультипроцессорную очередь
def integ_sum(func, n, res, a=0, b=1):
    u_rand = np.zeros(n)
    sum = 0
    for i in range(len(u_rand)):
        u_rand[i] = random.uniform(a, b)
        sum += func(u_rand[i])
    res.put(sum)

    return None


def Monte_Carlo_prc(a=0, b=1, n=10000000):
    procs = multiprocessing.cpu_count()
    # procs - количество возможных потоков
    # ↓ мультипроцессорная очередь с суммами
    res = multiprocessing.Queue()
    # количество точек на один поток
    n = n // procs
    processes = []
    for proc in range(procs):
        p = multiprocessing.Process(target=integ_sum, args=(func, n, res))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()
    # восстанавливаем суммарное количество точек
    n = n * procs

    # считаем нашу сумму
    sum = 0
    for _ in range(res.qsize()):
        sum += res.get()
    answer = (b - a) / float(n) * sum
    return answer


if __name__ == "__main__":
    start_1 = time.time()
    integral_1 = Monte_Carlo(func)
    end_1 = time.time()
    print('Монте Карло без оптимизации', integral_1, 'время работы:', end_1 - start_1, sep=' ')

    start_2 = time.time()
    integral_2 = Monte_Carlo_prc()
    end_2 = time.time()
    print('Монте Карло с оптимизацией', integral_2, 'время работы:', end_2 - start_2, sep=' ')

# мои результаты:
# Монте Карло без оптимизации 0.43813751797524175 время работы: 49.72575855255127
# Монте Карло с оптимизацией 0.43834383852364456 время работы: 7.524782180786133
