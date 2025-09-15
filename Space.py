weight = float(input("Enter your weight in pounds: "))

planet = input("Enter which planet you wish to fight on: ")

if planet == "Earth":
    weight = weight * 1 
elif planet == "Mercury":
    weight = weight * 0.90
elif planet == "Venus":
    weight = weight * 0.91
elif planet == "Mars":
    weight = weight * 0.38
elif planet == "Jupiter":
    weight = weight * 2.34
elif planet == "Saturn":
    weight = weight *1.06
elif planet == "Uranus":
    weight = weight * 0.92
elif planet == "Neptune":
    weight = weight * 1.19
elif planet == "Pluto":
    weight = weight * 0.063
else:
    print("Invalid planet name. Error.")

print(f"Your weight on {planet} is {weight} pounds.")