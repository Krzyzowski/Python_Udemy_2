
capital = 5000
rateOfInterest = 0.08
inflationRate = 0.15

oneYearReturn = capital * (1 + rateOfInterest)
print(oneYearReturn)

oneYearinflation = capital * (1 -inflationRate)
print(oneYearinflation)

delta = rateOfInterest - inflationRate
print("delta", delta)
oneYearRate = (capital *( 1 + delta)) - capital
print(oneYearRate)