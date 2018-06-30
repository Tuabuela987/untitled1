frase = input("Dime una frase: ")
cuenta = dict()

for i in frase :
    if i not in cuenta:
        cuenta[i] = 1
    else:
        cuenta [i] +=1
print (cuenta)
