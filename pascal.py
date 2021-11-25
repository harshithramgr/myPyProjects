numberOfRows=1
oldlist=[1]
print(oldlist)
for x in range(2,numberOfRows+1):
    newlist=[None] * x
    for i in range(0,x):
        if (i==0):
            newlist[0]=1

        elif (i==len(newlist)-1):
            newlist[i]=1

        else:
            newlist[i]=oldlist[i-1]+oldlist[i]
    print(newlist)
    oldlist=newlist
