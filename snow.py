import random

maxWidth=80
maxHeight=25

minFlakes=0
maxFlakes=5

rows=[]
for _ in range(maxHeight):
    actualFlakes=random.randint(minFlakes,maxFlakes)

    actRows=" "+maxWidth

    Flakes=random.sample

actualFlakes=random.randint(minFlakes,maxFlakes)
actRow=" "*maxWidth

Flakes=random.sample(range(0,maxWidth),actualFlakes)

for i in Flakes:
    aactRow=actRow[:i]+"*"+actRow[i+1:]
actRow=actRow[:5]+"*"+actRow[:6]
print(actRow)

