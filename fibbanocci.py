n1 = 0
n2 = 1
numbers_to_print = input("Please enter the numbers the print::")
print(n1)
print(n2)
for i in range(int(numbers_to_print) - 2):
    n3 = n1 + n2
    print(n3)
    n1 = n2
    n2 = n3
