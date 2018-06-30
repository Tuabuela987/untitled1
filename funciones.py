"""""
def numero_en_rango(x, y, z, ):
    if x > y and x < z:
        return True


print  (numero_en_rango(10, 1, 100))
print  (numero_en_rango(101, 1, 100))
print  (numero_en_rango(0, 1, 100))
"""
"""""
def num_bigger (x, y, z):
    return max((x, y, z))

print (num_bigger(1, 2, 3))
print (num_bigger(100, 1000, 10))
print (num_bigger(1, 0, -1))
"""""
def devolver_pares(lista):
    lista_pares = []
    for i in range (len(lista)):
        if i%2 == 0:
            lista_pares.append(i)
    return lista_pares

print (devolver_pares([1, 2, 3, 4, 5, 6]))
