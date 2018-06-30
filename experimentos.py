list = input("Dime una frase: ")
nlist = ""
for i in range(len(list)-1):
    if list[i] == "a" or list[i] == "e" or list[i] == "i" or list[i] == "o" or list[i] == "u":
        nlist += str(i)
    else:
        nlist += list[i]
print(nlist)


