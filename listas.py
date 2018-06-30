l1 = list(input('Dame una lista: '))
l2 = list(input ('Dame una lista: '))

result = []

i, j=  0, 0
while i < len (l1) and j < len (l2):
    for i in range ( len (l1)):
        if l1[i] == l2[j] and l1[i] not in result:
            result.append(l1[i])
    j +=1
print (result)