import random

maxWidth=80
maxHeight=25

minFlakes=0
maxFlakes=5
flake=["☼","❄","❅","❆","✡"]
flakeOptions=4

rows=[]
for _ in range(maxHeight):
    actualFlakes=random.randint(minFlakes,maxFlakes)

    actRows=" "*maxWidth

    Flakes=random.sample

    actualFlakes=random.randint(minFlakes,maxFlakes)
    actRow=" "*maxWidth

    Flakes=random.sample(range(0,maxWidth),actualFlakes)

    for i in Flakes:
        usedFlake=random.randint(0,flakeOptions)
        actRow=actRow[:i]+flake[usedFlake]+actRow[i+1:]
    rows.append(actRow)
print("\n".join(rows))



