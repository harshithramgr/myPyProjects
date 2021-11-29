import math


def add(n):
    sum = n * (n + 1) / 2
    return sum


def facto(n):
    return math.factorial(n)


def average(n):
    return float(add(n)) / n


# print('The average is ' + str(average(10)))

def median(n):
    nums = []
    for i in range(1, n + 1):
        nums.append(i)
    x = (len(nums) - 1) / 2
    print(nums[x])


median(8)
