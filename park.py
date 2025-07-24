# Flowers
# Author: Áron Domonkos
# Year: 2024

offers = []

with open('offers.txt', 'r') as file:
    bed_count = int(file.readline())
    for line in file:
        line = line.strip().split()
        offers.append([int(line[0]), int(line[1]), line[2]])

print('\nFunction 2')
print(f'Number of offers: {len(offers)}')

print('\nFunction 3')

both_sides = []
index = 1

for offer in offers:
    if offer[0] > offer[1]:
        both_sides.append(index)
    index += 1

print(f"Offers planting on both entrance sides: {' '.join(list(map(str, both_sides)))}")

print('\nFunction 4')

def relevant_offers(bed_number):
    matches = []
    idx = 1
    for offer in offers:
        if offer[0] <= bed_number <= offer[1]:
            matches.append([offer[2], idx])
        if offer[0] > offer[1] >= bed_number:
            matches.append([offer[2], idx])
        if bed_number >= offer[0] > offer[1]:
            matches.append([offer[2], idx])
        idx += 1
    return matches

selected_bed = int(input('Enter flower bed number: '))

matched = relevant_offers(selected_bed)
colors = []

if len(matched) > 0:
    print(f'Number of matching offers: {len(matched)}')
    print(f'Color if only the first offer is executed: {matched[0][0]}')
    for item in matched:
        if item[0][0] not in colors:
            colors.append(item[0][0])
    print(f"Possible colors: {', '.join(colors)}")
else:
    print('This flower bed will not be planted.')

print('\nFunction 5')

bed_number = 1
while len(relevant_offers(bed_number)) > 0:
    bed_number += 1

if bed_number == bed_count:
    print("All beds will be planted.")

else:
    total = 0
    for offer in offers:
        if offer[0] <= offer[1]:
            total += offer[1] - offer[0] + 1
        else:
            total += bed_count + offer[1] - offer[0] + 1

    if total >= bed_count:
        print("Reorganizing allows complete planting.")
    else:
        print("Complete planting is not possible.")

#Function 6

plantings = []

for i in range(1, bed_count + 1):
    matched = relevant_offers(i)
    if len(matched) > 0:
        plantings.append([matched[0][0], matched[0][1]])
    else:
        plantings.append(["#", 0])

with open("colors.txt", "w") as file:
    for row in plantings:
        file.write(f"{row[0]} {row[1]}\n")