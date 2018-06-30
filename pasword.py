cog = input ("Dime tu apellido: ")
num = input ("Dime un numero: ")
c= ""
for i in range(len(cog)):
    if i%2 !=0:
        c +=cog[i]
    else:
        c+=(num)
    c.replace (" ", "")
    print (c)

