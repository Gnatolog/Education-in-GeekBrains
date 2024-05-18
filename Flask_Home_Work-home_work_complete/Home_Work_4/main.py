# Задание №7
# 🐀 Напишите программу на Python, которая будет находить
# сумму элементов массива из 1000000 целых чисел.
# 🐀 Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
# 🐀 Массив должен быть заполнен случайными целыми числами
# от 1 до 100.
# 🐀 При решении задачи нужно использовать многопоточность,
# многопроцессорность и асинхронность.
# 🐀 В каждом решении нужно вывести время выполнения
# вычислений.

# Массив первое генерируес после подаем на
# обработку что бы массив был одинаковый
# Подаём на обработку не весь массив а по частям

from random import randint
import time
import threading
import multiprocessing
import asyncio

arr = [randint(1, 101) for i in range(0, 1_000_001)]

part_arr = len(arr) // 3

arr_1 = arr[:part_arr]
arr_2 = arr[part_arr: part_arr * 2]
arr_3 = arr[part_arr * 2:]
list_array = [arr_1, arr_2, arr_3]

all_sum = 0


def synchro_sum():
    global all_sum
    start_time = time.time()

    for array in list_array:
        for num in array:
            all_sum += num

    time_work = time.time() - start_time
    sum_arr = all_sum
    all_sum = 0
    return f' Synchro sum = {sum_arr} time = {time_work:.2f}'


def multithreading_sum(arr):
    global all_sum
    for i in arr:
        all_sum += i


def multithreading():
    global list_array
    start_time = time.time()
    threads = []
    for i in range(3):
        t = threading.Thread(target=multithreading_sum, args=[list_array[i]])
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
    time_work = time.time() - start_time
    return f' Multhithreding = {all_sum},  time = {time_work:.2f}'


def multiprocessing_sum(arr):
    global all_sum
    for i in arr:
        all_sum += i


def multiprocess():
    global list_array
    start_time = time.time()
    processes = []
    for i in range(3):
        p = multiprocessing.Process(target=multithreading_sum, args=[list_array[i]])
        processes.append(p)
        p.start()

    for p in processes:
        p.join()
    time_work = time.time() - start_time
    return f' Multiprocess = {all_sum},  time = {time_work:.2f}'


async def async_sum(arr):
    all_sum = 0
    for i in arr:
        all_sum += i

    return all_sum

async def main():
    start_time = time.time()
    await asyncio.gather(async_sum(arr_1), async_sum(arr_2), async_sum(arr_3))

    time_work = time.time() - start_time
    return f' Asynchro = {all_sum},  time = {time_work:.2f}'


print(synchro_sum())
print(multithreading())
print(multiprocess())
print(asyncio.run(main()))
