import numpy as np

# 1. Reshape
numbers = np.array([1, 2, 3, 4, 5, 6])

reshaped = numbers.reshape(2, 3)

print("Original:", numbers)
print("Reshaped:")
print(reshaped)


# 2. Flatten
flattened = reshaped.flatten()

print("\nFlatten:")
print(flattened)


# 3. Ravel
raveled = reshaped.ravel()

print("\nRavel:")
print(raveled)


# 4. Transpose
transposed = reshaped.transpose()

print("\nTranspose:")
print(transposed)


# 5. Resize
resized = np.array([1, 2, 3, 4, 5, 6])
resized.resize(3, 2)

print("\nResize:")
print(resized)


# 6. Concatenate
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

concatenated = np.concatenate((a, b))

print("\nConcatenate:")
print(concatenated)


# 7. Stack
stacked = np.stack((a, b))

print("\nStack:")
print(stacked)


# 8. Horizontal Stack
horizontal = np.hstack((a, b))

print("\nHorizontal Stack:")
print(horizontal)


# 9. Vertical Stack
vertical = np.vstack((a, b))

print("\nVertical Stack:")
print(vertical)


# 10. Split
values = np.array([1, 2, 3, 4, 5, 6])

split_values = np.split(values, 3)

print("\nSplit:")
print(split_values)


# 11. Horizontal Split
matrix = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8]
])

horizontal_split = np.hsplit(matrix, 2)

print("\nHorizontal Split:")
print(horizontal_split)


# 12. Vertical Split
vertical_split = np.vsplit(matrix, 2)

print("\nVertical Split:")
print(vertical_split)


# 13. Where
numbers = np.array([10, 20, 30, 40, 50])

positions = np.where(numbers > 25)

print("\nPositions greater than 25:")
print(positions)


# 14. Searchsorted
sorted_numbers = np.array([10, 20, 30, 40, 50])

position = np.searchsorted(sorted_numbers, 35)

print("\nPosition for 35:")
print(position)


# 15. Sort
unsorted = np.array([40, 10, 50, 20, 30])

sorted_array = np.sort(unsorted)

print("\nSorted:")
print(sorted_array)


# 16. Argsort
indices = np.argsort(unsorted)

print("\nArgsort:")
print(indices)


# 17. Boolean Indexing
numbers = np.array([10, 20, 30, 40, 50])

result = numbers[numbers > 25]

print("\nNumbers greater than 25:")
print(result)


# 18. Multiple Conditions
result = numbers[(numbers > 20) & (numbers < 50)]

print("\nNumbers between 20 and 50:")
print(result)