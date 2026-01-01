# take input from the user and check is the number is positive or negative

inputNum = int(input("Enter a number to check id the number is positive or negative: "))

if inputNum > 0:
    print(f"The inputed number {inputNum} is Positive")
elif inputNum < 0:
    print(f"The inputed number {inputNum} is Negative")
else:
    print("The inputed number is Zero")
