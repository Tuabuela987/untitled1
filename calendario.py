agenda = dict()
salir = False

while not salir:

    accion = input("Que quieres hacer, añadir un nuevo amigo[A], consultar un amigo[C]  o salir [S]: ")

    if accion == "A":
        print("Vamos a añadir un amigo: ")
        print("---------------------------")
        nombre = input("Dime el nombre de tu nuevo amigo: ")
        fecha = input("Cuando es su cumpleaños: ")
        agenda [nombre] = fecha

    elif accion == "C":
        print("vamos a consultar una fecha")
        print("---------------------------")
        nombre = input("Que amigo queires saber: ")
        print(agenda[nombre])
    elif accion == "S":
        salir = True