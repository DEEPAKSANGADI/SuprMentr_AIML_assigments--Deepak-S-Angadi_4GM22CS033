import time
import numpy as np

n = 1_000_000

print("=" * 60)
print("COMPARISON: Python Lists vs NumPy Arrays (1M numbers)")
print("=" * 60)

start = time.time()
python_list = list(range(n))
list_creation_time = time.time() - start

start = time.time()
numpy_array = np.arange(n)
array_creation_time = time.time() - start

print(f"\n1. Creation Time:")
print(f"   Python List: {list_creation_time:.6f} seconds")
print(f"   NumPy Array: {array_creation_time:.6f} seconds")

start = time.time()
list_result = [x * 2 for x in python_list]
list_multiply_time = time.time() - start

start = time.time()
array_result = numpy_array * 2
array_multiply_time = time.time() - start

print(f"\n2. Multiplication Time:")
print(f"   Python List: {list_multiply_time:.6f} seconds")
print(f"   NumPy Array: {array_multiply_time:.6f} seconds")


start = time.time()
list_sum = sum(python_list)
list_sum_time = time.time() - start

start = time.time()
array_sum = np.sum(numpy_array)
array_sum_time = time.time() - start

print(f"\n3. Sum Operation Time:")
print(f"   Python List: {list_sum_time:.6f} seconds")
print(f"   NumPy Array: {array_sum_time:.6f} seconds")

print("\n" + "=" * 60)
print("=" * 60)
#3 KEY observations from the above comparison:
# 1. SPEED: NumPy arrays are significantly faster (~10-100x) for 
#     mathematical operations due to vectorization and C-level 
#     implementation vs Python's interpreted loops.

# 2. MEMORY: NumPy arrays consume less memory as they store 
#     homogeneous data types efficiently, while Python lists 
#     store pointers to objects causing overhead.

# 3. CONVENIENCE: NumPy provides built-in mathematical functions 
#     (sum, mean, std) optimized for large datasets, making complex 
#     computations simpler and faster than list comprehensions.
