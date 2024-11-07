import numpy as np
from ctypesexample.summing import csort, nsort
import time
import random

orig = [random.random() for _ in range(1000000)]

a = orig
start = time.time()
a.sort()
end = time.time()
print("Python sort:\n\t" + str(end - start))

b = np.array(orig)
start = time.time()
b = np.sort(b)
end = time.time()
assert(a == b.tolist())
print("Numpy sort:\n\t" + str(end - start))

c = orig
start = time.time()
csort(c)
end = time.time()
assert(b.tolist() == c)
print("C++ sort (array):\n\t" + str(end - start))

d = np.array(orig)
start = time.time()
nsort(d)
end = time.time()
assert(c == d.tolist())
print("C++ sort (numpy array):\n\t" + str(end - start))
