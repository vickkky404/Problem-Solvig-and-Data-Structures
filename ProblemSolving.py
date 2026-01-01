# there is a movie which needs to verify the gender and age of the person to allow them for a movie also set specific price for males or certain age and females of certain age , so WAP to verify or write the logic of the code to implement this feature

# if the age is a 18F then the ticket price is 150  , if the age is 19M then the ticket price is 150 , less than 18 of both M and F will have to pay less amount

askage = int(input("Enter your age: "))
askgender = str(input("Enter your gender M/F: "))

if askage >=18 and askgender == 'F':
    print(f"as your age is {askage} so your price is 150, and your gender is  {askgender}")
elif askage <= 18:
    print(f"as your age is {askage} so your price is 50 , and gender is  {askgender}")
elif askage >= 18 and askgender == 'M':
    print(f"as your age is {askage} so your price is 150")
else:
    print("Invalid input")