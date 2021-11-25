import random
x=1000000
heads=0
tails=0


def flip():
    num=random.randint(1,2)
    if num==1:
        return True
    else:
        return False


for i in range(x):
    if flip():
        heads=heads+1
    else:
        tails=tails+1
print("the number of heads is "+str(heads),"the number of tails is "+str(tails))
