#array practice

# reverse an array using slicing
def reverse_array(arr):
    return arr[::-1]
# find the maximum element in an array
def max_in_array(arr):
    return max(arr)
# find the minimum element in an array
def min_in_array(arr):
    return min(arr)
# calculate the sum of all elements in an array
def sum_of_array(arr):
    return sum(arr)
# calculate the average of all elements in an array
def average_of_array(arr):
    return sum(arr) / len(arr) if arr else 0
# find the index of a specific element in an array
def index_of_element(arr, element):
    try:
        return arr.index(element)
    except ValueError:
        return -1