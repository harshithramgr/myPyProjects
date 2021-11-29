n = 8
list1 = []
for i in range(n):
    print("i is" + str(i))
    templist = []
    for j in range(i + 1):
        print("j is" + str(j))
        if j == 0 or j == 1:
            templist.append(1)
            print(templist)
        else:
            templist.append(list1[i - 1][j - 1] + list1[i - 1][j])
    list1.append(templist)
