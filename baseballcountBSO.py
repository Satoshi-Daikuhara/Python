pitting = int(input())
fourball = []
threestrike = []

for num in range(pitting):
    ball = input()
    if ball == "ball":
        fourball.append("ball")
        if len(fourball) == 4:
            print("fourball!")
            break
        else:
            print("ball!")
    elif ball == "strike":
        threestrike.append("strike")
        if len(threestrike) == 3:
            print("out!")
            break
        else:
            print("strike!")
    else:
        break
