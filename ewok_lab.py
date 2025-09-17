# Description: Demonstrates list operations and loops with a roster of Ewoks.
#! Part 1
print("=== Ewok Ops: Lists & Loops ===\n")

# A starting roster of Ewoks (a python list)
ewoks = ["Whicket", "Paploo", "Teebo", "Nippet"]

# Indexing: 0 = first, -1 = last
print("First Ewok:", ewoks[0])
print("Last Ewok:", ewoks[-1])

# Slicing: ewoks[start:stop] (stop is exclusive)
print("Middle pair:", ewoks[1:3]) # Paploo, Teebo

# Lenght of list
print("Roster size", len(ewoks))

#! Part 2
print("n\-- Updating the roster --")
ewoks.append("Cheif Chirpa") # add to the end
print("After append:", ewoks)

ewoks.insert(0,"Longray") # add at a specific position (index 0)
print("After insert at front:", ewoks)

ewoks.extend(["Kneesaa", "Latara"]) # add multiple at once
print("After extend:, ewoks")

ewoks.remove("Paploo") # Remove the FIRST match by value
print("After remove Paploo:", ewoks)

removed = ewoks.pop() # pop removes and RETURNS last item
print("Popped off:", removed)
print("After pop", ewoks)

# Sorting: alphabetacal A->Z, then reverse
ewoks.sort()
print("Sorted A->Z:", ewoks)
ewoks.reverse()
print("Reversed Z->A:", ewoks)

#!Part 3
print("\n-- Roll Call --")
for ewok in ewoks:
    print("Present:", ewok)

print("\n-- Numbered Roll Call (enumerate) --")
for i, ewok in enumerate(ewoks, start = 1):
    print(f"{i}. {ewok}")

#! TASK A
ewoks.append("Walda")

ewoks.insert(2, "Tazia")

if "Teebo" in ewoks:
    ewoks.remove("Teebo")

on_scout = ewoks.pop()
print(f"{on_scout} assigned to forest scout duty.")

ewoks.sort()

ewoks.reverse()

#! TASK B
print("\n-- L-only squad --")
for ewok in ewoks:
    if ewok.startswith("L"): #simple condition
        print("L-squad member:", ewok)

#! TASK C
print("\n-- Uppercase call signs --")
call_signs = []
for ewok in ewoks:
    call_signs.append(ewok.upper())
print(call_signs)

#! TASK D
print("\n-- Longest name --")
longest = ""
for ewok in ewoks:
    if len(ewok) > len(longest):
        longest = ewok
print("Longest:", longest)

#! Part 5
print("\n=== Supply Drop ===")
items = ["Berries", "Spears", "Bandages", "Glider Parts"]
counts = [30, 12, 8, 6]

# Samity check: lengths should match
if len(items) != len(counts):
    print("Data Error: items and counts are different lengths!")
else:
    total = 0
    for i in range(len(items)): # index-based loop pairs up lists
        line = f"{items[i]} x {counts[i]}"
        print(line)
        total += counts[i]
    print("Total units:", total)
