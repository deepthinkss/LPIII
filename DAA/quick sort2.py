import random
import time

# Deterministic Quick Sort
def deterministic_partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def deterministic_quick_sort(arr, low, high):
    if low < high:
        pi = deterministic_partition(arr, low, high)
        deterministic_quick_sort(arr, low, pi - 1)
        deterministic_quick_sort(arr, pi + 1, high)

# Randomized Quick Sort
def randomized_partition(arr, low, high):
    rand_index = random.randint(low, high)
    arr[high], arr[rand_index] = arr[rand_index], arr[high]
    return deterministic_partition(arr, low, high)

def randomized_quick_sort(arr, low, high):
    if low < high:
        pi = randomized_partition(arr, low, high)
        randomized_quick_sort(arr, low, pi - 1)
        randomized_quick_sort(arr, pi + 1, high)

# Utility function to analyze both algorithms
def analyze_quick_sorts(arr):
    arr_copy = arr.copy()

    # Deterministic Quick Sort
    start = time.time()
    deterministic_quick_sort(arr, 0, len(arr) - 1)
    end = time.time()
    print(f"Deterministic Quick Sort Time: {end - start} seconds")

    # Randomized Quick Sort
    start = time.time()
    randomized_quick_sort(arr_copy, 0, len(arr_copy) - 1)
    end = time.time()
    print(f"Randomized Quick Sort Time: {end - start} seconds")

# Sample array for sorting
arr = [12, 4, 56, 17, 8, 99, 34, 23, 75, 3, 15]
analyze_quick_sorts(arr)
print("Sorted array (Deterministic):",arr)