weather = "raining"
season = "raining"
print(id(weather))
print(id(season))

if weather == season:
    print("Weather = Season")
else:
    print("It is not raining")