# -------------------- Timer Utility --------------------

import time
class Timer:
    def __init__(self):
        self._start_time = 0
        self._elapsed_time = 0

    def start(self):
        self._start_time = time.perf_counter()

    def stop(self):
        self._elapsed_time = time.perf_counter() - self._start_time

    def elapsed(self):
        return self._elapsed_time


# Test Timer on a dummy task
t = Timer()
t.start()

for i in range(1000000):
    _ = i ** 2

t.stop()
print(f"Elapsed time: {t.elapsed()} seconds")


# Compare Prime Functions
import math
def primes(n):
    if n <= 1:
        return False
    result, i = True, 2
    while result and i <= math.sqrt(n):
        if n % i == 0:
            result = False
        i += 1
    return result

t = Timer()
t.start()
print(primes(1000009))
t.stop()
print("Time taken:", t.elapsed(), "seconds")


def primes(n):
    if n <= 1:
        return False
    result = True
    for i in range(2, n):
        if n % i == 0:
            result = False
    return result

t = Timer()
t.start()
print(primes(1000009))
t.stop()
print("Time taken:", t.elapsed(), "seconds")

