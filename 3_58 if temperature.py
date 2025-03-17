
raining = False
haveUmbrella = False
temperature = 11

if temperature >= 40 or temperature <= 0:
    print("stay home")
elif temperature > 0 and temperature < 10 and haveUmbrella and raining:
    print("You may go with umbrella")
elif temperature >= 10 and not raining:
    print("You may go without umbrella")
else:
    print("Just stay home!")



