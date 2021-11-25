numbers=[15,30,3,11]
for i in range(4):
    bn=numbers[0]
    for j in range(0,len(numbers)-1):

        if numbers[j]<numbers[j+1]:
            bn=numbers[j+1]
    print(bn)
    numbers.remove(bn)
