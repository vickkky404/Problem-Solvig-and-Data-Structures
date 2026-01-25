# array operation

import array as arr

val = arr.array('i' , [1,2,3,4,5,6])
print(val)

print("\n")

print("Reversed Array")

val.reverse()
for i in range(len(val)):
    print(val[i], end=" ")


