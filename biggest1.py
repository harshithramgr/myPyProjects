numbers=[9,6,30,3]
bn=numbers[0]
if numbers[0]<numbers[1]:
    bn=numbers[1]
if numbers[1]<numbers[2]:
    bn=numbers[2]
if numbers[2]<numbers[3]:
    bn=numbers[3]
print (bn)
numbers.remove(bn)

bn=numbers[0]
if numbers[0]<numbers[1]:
    bn=numbers[1]
if numbers[1]<numbers[2]:
    bn=numbers[2]
print (bn)
numbers.remove(bn)

bn=numbers[0]
if numbers[0]<numbers[1]:
    bn=numbers[1]
print (bn)
numbers.remove(bn)

print(numbers[0])
