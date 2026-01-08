# Swanson, John

squad = []

num = int(input("How many Rebel squads are participating in the mission?: "))
if num < 1:
    print("Amount of squads has to be higher than 0")
else:
    if num == 1:
        squad.append(input("What are the name of this squad?: "))
    elif num == 2:
        squad.append(input("What are the names of these squads?: "))
    elif num == 3:
        squad.append(input("What are the names of these squads?: "))
    elif num == 4:
        squad.append(input("What are the names of these squads?: "))
    elif num == 5:
        squad.append(input("What are the names of these squads?: "))
    else:
        pass

def scores():
    sec1 = int(input("How many imperial targets were nutrilized in sector 1?: "))
    if sec1 < 0:
        print("It needs to be between 0 and 100!")
        return
    else:
        pass
    if sec1 > 100:
        print("It needs to be between 0 and 100!")
        return
    else:
        pass
    sec2 = int(input("How many imperial targets were nutrilized in sector 2?: "))
    if sec2 < 0:
        print("It needs to be between 0 and 100!")
        return
    else:
        pass
    if sec2 > 100:
        print("It needs to be between 0 and 100!")
        return
    else:
        pass
    sec3 = int(input("How many imperial targets were nutrilized in sector 3?: "))
    if sec3 < 0:
        print("It needs to be between 0 and 100!")
        return
    else:
        pass
    if sec3 > 100:
        print("It needs to be between 0 and 100!")
        return
    else:
        pass
    sec4 = int(input("How many imperial targets were nutrilized in sector 4?: "))
    if sec4 < 0:
        print("It needs to be between 0 and 100!")
        return
    else:
        pass
    if sec4 > 100:
        print("It needs to be between 0 and 100!")
        return
    else:
        pass
    sec5 = int(input("How many imperial targets were nutrilized in sector 5?: "))
    if sec5 < 0:
        print("It needs to be between 0 and 100!")
        return
    else:
        pass
    if sec5 > 100:
        print("It needs to be between 0 and 100!")
        return
    else:
        pass
    
for squad in squad:
    tot_score = scores()
high_squad = squad
percision = tot_score
top_percision = squad
most_dang = "sec1"

print(f"The highest scoring squad was {high_squad}")
print(f"The squad with the best percision is {top_percision}")

import datetime as time

with open(mission_report.txt, "w") as file:
    file.write("OFFICIAL REBEL ALLIANCE MISSION DEBRIEF")
    file.write("=" * 35 + "\n")
    file.write(f"current date and time: {time}")
    file.write(f"{squad}")
    file.write(f"{tot_score}")
    file.write(f"{percision}")
    file.write(f"The top squad is {squad}")
    file.write(f"The most dangerous sector is {most_dang}")