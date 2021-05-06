#If the bill was $150.00, split between 5 people, with 12% tip.
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python
bill = float(input("What is the bill total? "))
tip = int(input("How much do you want to tip? 10, 12, 15? "))
people = int(input("How many people split the bill? "))

# bi: bill, t: tip, p: people f= final

tip_perc = (tip/100)
bi = (bill * tip_perc)
bit= (bi+bill)
bp = (bit/people)
f = round(bp, 2)

print(f"Each person pays ${f}")