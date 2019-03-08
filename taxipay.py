line = input().split(" ")
taxies = int(line[0])
long = int(line[1])
taxipays = [[]]

for num in range(taxies):
    taxipays.append(input().split(" "))

min = 0
max = 0

for num in range(taxies):
    cost = 0
    pay = taxipays[num]
    firstL = int(pay[0])
    firstP = int(pay[1])
    addL = int(pay[2])
    addP = int(pay[3])

    if long < firstL:
        cost = firstP
    else:
        count = 0
        while True:
            if long < firstL + addL * count:
                cost = firstP + addP * count
                break
            else:
                count

    if min == 0 or min > cost:
        min = cost
    if max < cost:
        max = cost

print(min + " " + max)