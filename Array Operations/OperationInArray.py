# array operation program
import array as arr

val = arr.array('i' , [1,2,3,4,5,6,7])
print(val)

# printing using basic for loop and advanced for loop

# basic for loop
for i in range(len(val)):
    print(val[i])

# advanced for loop
print('\n')
print("Advanced for loop output")

for x in val:
    print(x)
