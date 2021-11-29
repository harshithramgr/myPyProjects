word = "it is 0c"
i = word.split()
temp = i[2]

if ("c" in temp):
    temp = temp.replace("c", "")
    f = int(temp) * 1.8 + 32
    print("it is " + str(f) + " farenhiet")

if ("f" in temp):
    temp = temp.replace("f", "")
    f = (int(temp) - 32) / 1.8
    print("it is " + str(f) + " celcius")
