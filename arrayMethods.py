import numpy as np

# 1. NumPy Array
numbers = np.array([10, 20, 30, 40, 50])
print("Array:", numbers)


# 2. 1D, 2D and 3D Arrays

one_d = np.array([1, 2, 3, 4])
print("1D:", one_d)

two_d = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
print("2D:")
print(two_d)

three_d = np.array([
    [[1, 2, 3], [4, 5, 6]],
    [[7, 8, 9], [10, 11, 12]]
])
print("3D:")
print(three_d)


# 3. Array Properties

print("Dimensions:", two_d.ndim)
print("Shape:", two_d.shape)
print("Size:", two_d.size)
print("Data Type:", two_d.dtype)


# 4. Creating Arrays

zeros = np.zeros(5)
print("Zeros:", zeros)

ones = np.ones(5)
print("Ones:", ones)

full = np.full(5, 7)
print("Full:", full)

empty = np.empty(5)
print("Empty:", empty)

arange = np.arange(1, 6)
print("Arange:", arange)

linspace = np.linspace(0, 10, 5)
print("Linspace:", linspace)

identity = np.eye(3)
print("Identity Matrix:")
print(identity)


# 5. Indexing

numbers = np.array([10, 20, 30, 40, 50])

print("Indexing:", numbers[2])
print("Negative Indexing:", numbers[-1])

two_d = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print("2D Indexing:", two_d[1, 2])


# 6. Slicing

numbers = np.array([10, 20, 30, 40, 50])

print("Slice:", numbers[1:4])
print("From index 2:", numbers[2:])
print("First 3:", numbers[:3])
print("Step:", numbers[0:5:2])
print("Reverse:", numbers[::-1])


# 7. Array Operations

a = np.array([10, 20, 30, 40])
b = np.array([1, 2, 3, 4])

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)
print("Power:", a ** 2)


# 8. Mathematical Functions

numbers = np.array([10, 20, 30, 40, 50])

print("Sum:", np.sum(numbers))
print("Minimum:", np.min(numbers))
print("Maximum:", np.max(numbers))
print("Mean:", np.mean(numbers))
print("Median:", np.median(numbers))
print("Standard Deviation:", np.std(numbers))
print("Variance:", np.var(numbers))
print("Square Root:", np.sqrt(numbers))

values = np.array([-10, -20, 30, -40])
print("Absolute:", np.abs(values))

decimal = np.array([1.234, 2.567, 3.891])
print("Round:", np.round(decimal))


# 9. Axis

numbers = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print("Total:", np.sum(numbers))
print("Axis 0:", np.sum(numbers, axis=0))
print("Axis 1:", np.sum(numbers, axis=1))