import numpy as np


# 14. Broadcasting

a = np.array([1, 2, 3])
b = 10

print("Broadcasting:")
print(a + b)

numbers = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(numbers + 10)


# 15. Random

print("\nRandom:")

print("rand:", np.random.rand(3))
print("randint:", np.random.randint(1, 10, 5))
print("randn:", np.random.randn(3))
print("choice:", np.random.choice([10, 20, 30, 40], 2))

values = np.array([1, 2, 3, 4, 5])
np.random.shuffle(values)

print("shuffle:", values)


# 16. Linear Algebra

a = np.array([
    [1, 2],
    [3, 4]
])

b = np.array([
    [5, 6],
    [7, 8]
])

print("\nLinear Algebra:")

print("Matrix multiplication:")
print(np.matmul(a, b))

print("Dot product:")
print(np.dot(a, b))

print("@ operator:")
print(a @ b)

print("Determinant:")
print(np.linalg.det(a))

print("Inverse:")
print(np.linalg.inv(a))


# 17. Copy and View

original = np.array([1, 2, 3, 4])

copied = original.copy()
copied[0] = 100

print("\nCopy:")
print("Original:", original)
print("Copy:", copied)

viewed = original.view()
viewed[1] = 200

print("View:")
print("Original:", original)
print("View:", viewed)


# 18. Missing and Special Values

values = np.array([10, np.nan, 30, np.inf, 50])

print("\nMissing and Special Values:")

print("Array:", values)
print("NaN check:", np.isnan(values))
print("Infinity check:", np.isinf(values))


# 19. Performance / Vectorization

numbers = np.array([1, 2, 3, 4, 5])

result = numbers * 10

print("\nVectorization:")
print("Original:", numbers)
print("Multiplied:", result)

result = numbers ** 2

print("Squared:", result)