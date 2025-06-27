pokemon = []
tipos = ["fuego", "agua", "hierba", "veneno", "psiquico", "luchador", "eléctrico"]

def ingresar():
    id = input("ID: ")
    nombre = input("Nombre: ")

    repetido = False
    for p in pokemon:
        if p[1] == nombre:
            repetido = True
    if repetido:
        print("Ya existe ese nombre.")
        return

    codigo = input("Código: ")

    contador = 0
    for c in codigo:
        contador = contador + 1
    if contador < 8:
        print("Código demasiado corto.")
        return

    espacio = False
    for c in codigo:
        if c == " ":
            espacio = True
    if espacio:
        print("Código no puede tener espacios.")
        return

    tiene_letra = False
    tiene_numero = False
    for c in codigo:
        if (c >= "a" and c <= "z") or (c >= "A" and c <= "Z"):
            tiene_letra = True
        if c >= "0" and c <= "9":
            tiene_numero = True
    if not tiene_letra or not tiene_numero:
        print("Código debe tener letra y número.")
        return

    tipo = input("Tipo: ")
    valido = False
    for t in tipos:
        if tipo == t:
            valido = True
    if not valido:
        print("Tipo no válido.")
        return

    pokemon.append([id, nombre, codigo, tipo])
    print("¡Pokémon ingresado!")

def buscar():
    nombre = input("Nombre a buscar: ")
    encontrado = False
    for p in pokemon:
        if p[1] == nombre:
            print("Tipo:", p[3])
            encontrado = True
    if not encontrado:
        print("No encontrado.")

def eliminar():
    nombre = input("Nombre a eliminar: ")
    indice = -1
    posicion = 0
    for p in pokemon:
        if p[1] == nombre:
            indice = posicion
        posicion = posicion + 1
    if indice != -1:
        del pokemon[indice]
        print("Eliminado.")
    else:
        print("No se encontró.")

def ver():
    if pokemon == []:
        print("Sin datos.")
    else:
        for p in pokemon:
            print("ID:", p[0], "| Nombre:", p[1], "| Tipo:", p[3])

def menu():
    while True:
        print("\n1. Ingresar pokemon\n2. Buscar pokemon\n3. Eliminar pokemon\n4. Ver la lista de pokemon\n5. Salir")
        op = input("Opción: ")
        if op == "1": ingresar()
        elif op == "2": buscar()
        elif op == "3": eliminar()
        elif op == "4": ver()
        elif op == "5": break
        else: print("Inválido.")

menu()
