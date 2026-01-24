#find the minimum element in an array

numbers = [12,3,45,2]
min_element = min(numbers)

for num in numbers:
    if num < min_element:
        min_element = num

print("The minimum element is:", min_element)
# Q2: Find the Minimum Element in an Array