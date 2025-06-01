# Week 1 — Basic Math, Primes, and OOP

# -------------------- GCF / GCD --------------------

def gcf(m, n):
    # GCF using list of common factors
    cf = []
    for i in range(1, min(m, n) + 1):
        if (m % i) == 0 and (n % i) == 0:
            cf.append(i)
    return cf[-1]

print(gcf(8, 12))


def gcf(m, n):
    # GCF using single variable (more memory efficient)
    for i in range(1, min(m, n) + 1):
        if (m % i) == 0 and (n % i) == 0:
            mrff = i
    return mrff

print(gcf(8, 12))


def gcd(m, n):
    # Recursive GCD using modulo-based subtraction
    a, b = max(m, n), min(m, n)
    if a % b == 0:
        return b
    else:
        return gcd(b, a - b)


# -------------------- Prime Numbers --------------------

def factors(k):
    fl = []
    for i in range(1, k + 1):
        if k % i == 0:
            fl.append(i)
    return fl


def prime(k):
    return factors(k) == [1, k]

print(prime(7))


def primes(n):
    # Basic method (no early exit)
    result = True
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            result = False
    return result


def prime(n):
    # Improved version with early exit
    result = True
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            result = False
            break
    return result


def prime(n):
    # While loop version
    if n <= 1:
        return False
    result, i = True, 2
    while result and (i < n):
        if n % i == 0:
            result = False
        i += 1
    return result


import math
def prime(n):
    # Most efficient version using √n
    if n <= 1:
        return False
    result, i = True, 2
    while result and (i <= math.sqrt(n)):
        if n % i == 0:
            result = False
        i += 1
    return result


def primesupto(k):
    # Return list of all primes ≤ k
    j = []
    for i in range(1, k + 1):
        if prime(i):
            j.append(i)
    return j

print(primesupto(26))


def primesumupto(m):
    # Return first m prime numbers
    count, i, pl = 0, 1, []
    while count < m:
        if prime(i):
            pl.append(i)
            count += 1
        i += 1
    return pl

print(primesumupto(100))


def primediffs(n):
    # Returns frequency of prime gaps (difference between consecutive primes)
    lastprime = 2
    pd = {}
    for i in range(3, n + 1):
        if prime(i):
            d = i - lastprime
            lastprime = i
            if d in pd.keys():
                pd[d] += 1
            else:
                pd[d] = 1
    return pd
  
  
  #just a starter of oop take it as bonus

# -------------------- OOP Examples --------------------

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("adding new student in Database..")

s1 = Student("karan", 97)
print(s1.name)

s2 = Student("arjun", 88)
print(s2.name, s2.marks)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}({self.age})"

p1 = Person("John", 36)
p2 = Person("Johrn", 26)

print(p1)
print(p2)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name + " and I am of " + str(self.age))

p1 = Person("John", 36)
p1.myfunc()


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


# Week 2 — Search and Sort

def bsearch(v, L):
    # Recursive binary search
    if L == []:
        return False
    m = len(L) // 2
    if v == L[m]:
        return True
    if v < L[m]:
        return bsearch(v, L[:m])
    else:
        return bsearch(v, L[m+1:])

print(bsearch(7, [0, 1, 2, 4, 5, 9]))


def selection_sort(l):
    # In-place selection sort
    n = len(l)
    if n < 1:
        return l
    for i in range(n):
        mpos = i
        for j in range(i + 1, n):
            if l[j] < l[mpos]:
                mpos = j
        l[i], l[mpos] = l[mpos], l[i]
    return l

print(selection_sort([2, 5, 1, 4, 9, 0]))


def insertionSort(array):
    # Insertion sort algorithm
    for step in range(1, len(array)):
        key = array[step]
        j = step - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array

print(insertionSort([0, 1, 2, 4, 5, 9]))
