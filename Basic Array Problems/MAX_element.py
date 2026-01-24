# Q2: Find the Maximum Element in an Array
'''
input = 5 8 3 9 1 4
'''

numbers = [5, 8, 3, 9, 1, 4]
max_element = numbers[0]

for num in numbers:
    if num > max_element:
        max_element = num
print("The maximum element in the array is:", max_element)
