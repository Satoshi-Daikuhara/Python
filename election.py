line = input().split(" ")
post = int(line[0])
elector = int(line[1])
voice = int(line[2])
postList = []

for num in range(post):
    postList.append(0)

for num in range(voice):
    man = int(input()) - 1
    count = 0

    for i in range(post):
        if i != man and postList[i] > 0:
            postList.insert(i, postList[i] - 1)
            del postList[i + 1]
            count += 1

    if elector > 0:
        elector -= 1
        count += 1

    postList.insert(man, postList[man] + count)
    del postList[man + 1]

topList = []
top = 0

for num in range(post):
    siji = postList[num]
    if siji > top:
        topList = [num]
        top = siji
    elif siji == top:
        topList.append(num)

for num in range(len(topList)):
    print(topList[num] + 1)
