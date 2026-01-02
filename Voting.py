#voting system..
# if age greater then or = to 18 then the person is eligible to vote otherwisr not eligible to vote.

age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
elif age < 18:
    print("You are not eligible to vote.")
else:
    print("Invalid input...")