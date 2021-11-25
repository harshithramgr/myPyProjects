def primechecker(x):
 for i in range(2,x-1):
     if (x%i==0):
         isprime=False
         return isprime
 isprime=True
 return isprime
start=input("The_number_to_start_at:")
end=input("The_number_to_end_at:")
for i in range(int(start),int(end)):
    if (primechecker(i)):
        bigprime=i
print(bigprime)
