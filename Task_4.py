from time import perf_counter
from sys import getsizeof

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

start_1 = perf_counter()
result_1 = [src[i] for i in range(1, len(src)) if src[i] > src[i - 1]]
print(result_1, perf_counter() - start_1, getsizeof(result_1))
# создали список: требуется больше времени, но меньше памяти

start_2 = perf_counter()
result_2 = (src[i] for i in range(1, len(src)) if src[i] > src[i - 1])
print(list(result_2), perf_counter() - start_2, getsizeof(list(result_2)) + getsizeof(result_2))
# создали генератор и из негератора получили список: требуется меньше времени, но больше памяти
