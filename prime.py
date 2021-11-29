your_input=input("The_number_to_check please:")
for i in range(2,int(your_input)-1):
    if (int(your_input)%i==0):
        print ("not prime:(")
        exit()
print("prime;)")
