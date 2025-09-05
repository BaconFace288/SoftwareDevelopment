my_int = 42
my_float = 3.14
print("the value of my_int is", my_int)
print("the value of my_float is", my_float)
addition = my_int + my_float
subtraction = my_int - my_float
multiplication = my_int * my_float
division = my_float / my_int
power = my_int ** 2
modulus = my_int % 5
floor_division = my_int // 7

print("Addition result:", addition)
print("Subtraction result:", subtraction)
print("Multiplication result:", multiplication)
print("Division result:", division)
print("Power result:", power)
print("Modulus results:", modulus)
print("Floor Division result:", floor_division)

first_name = "Luke"
Last_name = "Skywalker"
full_name = first_name + " " + Last_name
print("Your Jedi name is:", full_name)

name_lenght = len(full_name)
print("the lenght of your jedi name is:", name_lenght)

message = "May the force be with you, " + full_name + "!"
print(message)

starships = ["Millennium Falcon", "X-Wing", "TIE Fighter"]
print("Initial starships fleet:", starships)
starships.append("Star Destroyer")
print("Updated starships fleet:", starships)
print("The second starship in the fleet is:", starships[1])
print("The first starship in the fleet is:", starships[0])
print("The last starship in formation is:", starships[-1])
