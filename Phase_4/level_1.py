'''
PHASE 4 — BASIC ARRAYS (Iterative Logical Thinking)

Level-1 Fundamental Of Arrays
'''


# 1. Input n and take n integers into an array; print them.
def input_and_print(n, arr=None):
    if arr is None:
        arr = []
    if n == 0:
        print(arr)
        return arr
    x = int(input())
    arr.append(x)
    return input_and_print(n - 1, arr)


# 2. Find the sum of all elements in an array.
def sum_array(arr, i=0):
    if i == len(arr):
        return 0
    return arr[i] + sum_array(arr, i + 1)


# 3. Find the average of array elements.
def average_array(arr):
    return sum_array(arr) / len(arr)


# 4. Find the maximum element in an array.
def max_array(arr, i=0):
    if i == len(arr) - 1:
        return arr[i]
    return max(arr[i], max_array(arr, i + 1))


# 5. Find the minimum element in an array.
def min_array(arr, i=0):
    if i == len(arr) - 1:
        return arr[i]
    return min(arr[i], min_array(arr, i + 1))


# 6. Count how many elements are positive, negative, or zero.
def count_pos_neg_zero(arr, i=0, p=0, n=0, z=0):
    if i == len(arr):
        return p, n, z
    if arr[i] > 0:
        return count_pos_neg_zero(arr, i + 1, p + 1, n, z)
    elif arr[i] < 0:
        return count_pos_neg_zero(arr, i + 1, p, n + 1, z)
    else:
        return count_pos_neg_zero(arr, i + 1, p, n, z + 1)


# 7. Count how many elements are even and odd.
def count_even_odd(arr, i=0, e=0, o=0):
    if i == len(arr):
        return e, o
    if arr[i] % 2 == 0:
        return count_even_odd(arr, i + 1, e + 1, o)
    else:
        return count_even_odd(arr, i + 1, e, o + 1)


# 8. Find the index of the maximum element.
def index_max(arr, i=0, max_i=0):
    if i == len(arr):
        return max_i
    if arr[i] > arr[max_i]:
        return index_max(arr, i + 1, i)
    return index_max(arr, i + 1, max_i)


# 9. Find the index of the minimum element.
def index_min(arr, i=0, min_i=0):
    if i == len(arr):
        return min_i
    if arr[i] < arr[min_i]:
        return index_min(arr, i + 1, i)
    return index_min(arr, i + 1, min_i)


# 10. Take n elements and print only those greater than a given value k.
def greater_than_k(arr, k, i=0):
    if i == len(arr):
        return
    if arr[i] > k:
        print(arr[i], end=" ")
    greater_than_k(arr, k, i + 1)


# Demo
if __name__ == "__main__":
    n = 5
    arr = [1, -2, 3, 0, 5]

    print("1:")
    print(arr)

    print("2:", sum_array(arr))
    print("3:", average_array(arr))
    print("4:", max_array(arr))
    print("5:", min_array(arr))
    print("6:", count_pos_neg_zero(arr))
    print("7:", count_even_odd(arr))
    print("8:", index_max(arr))
    print("9:", index_min(arr))
    print("10:")
    greater_than_k(arr, 2)