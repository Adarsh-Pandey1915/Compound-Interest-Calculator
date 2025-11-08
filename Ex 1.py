# Compound Interest Calculator :

principle = 0
rate = 0
time = 0

while principle <= 0 :
    principle = float(input("Enter the principle amount: "))
    if principle <= 0:
        print ("Principle amount can't be negative or equal to zero !")

while rate <= 0 :
    rate = float(input("Enter the interest rate: "))
    if rate <= 0:
        print ("Rate amount can't be negative or equal to zero !")

while time <= 0 :
    time = int(input("Enter the time in years: "))
    if time <= 0:
        print ("time amount can't be negative or equal to zero !")

amount = principle*pow((1 + rate / 100), time)
print(f"Your total amount after {time} years will be ${amount:.2f}")

CI = amount - principle
print(f"Compound interest charged for {time} year/s is ${CI:.2f}")
