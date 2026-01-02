# WAP to check what is the tempreature in the city and tell what type of weather it is.

# if tempreature is below 19 degree then it is cold
# if tempreature is between 20 to 30 degree then it is normal
# if tempreature is above 30 degree then it is hot

degree = int(input("Enter the tempreature in your area.."))

if degree < 0:
    print("Extreme Cold Weather")
elif degree >= 0 and degree <= 19:
    print("Cold Weather")
elif degree >= 20 and degree <= 30:
    print("Normal Weather")
elif degree > 30 and degree <= 40:
    print("Hot Weather")
elif degree > 40:
    print("Extremely Hot Weather")
else:
    print("Invalid Input...")