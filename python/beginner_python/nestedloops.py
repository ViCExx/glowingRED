
for i in range(6):
    print("Multiplying by:", i)
    for j in range(6):
        print(i,"*",j, "=", j * i, end=" This is the result after you multiply \n")
    print()
# example 
for i in range(11):
    for j in range(11):
        print(j, end=" ")
    print()
# example
i = 0
while i < 10:
    
    j = 0 
    while j < 10:
        print(j, end=" ")
        j += 1
    print()
    
    i += 1