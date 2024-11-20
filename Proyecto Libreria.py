'''
╔═════════════════════════╗ 
║       VARIABLES         ║ 
╚═════════════════════════╝ 
'''

#ESTOS SON LOS DICCIONARIOS CON LA INFORMACIÓN DE LOS LIBROS DISPONIBLES
L1={"Título":"Juego de tronos","Autor":"George R.R. Martin","Disponibilidad":True,"Reseña":""}
L2={"Título":"El principe","Autor":"Nicolás Maquiavelo","Disponibilidad":True,"Reseña":""}
L3={"Título":"El cantar del profeta","Autor":"Paul Lynch","Disponibilidad":True,"Reseña":""}
L4={"Título":"Detrás del cielo","Autor":"Manuel Rivas","Disponibilidad":True,"Reseña":""}
L5={"Título":"Intermezzo","Autor":"Sally Rooney","Disponibilidad":True,"Reseña":""}


#AQUÍ JUNTO TODOS LOS DICCIONARIOS EN UNO SOLO PARA LUEGO IMPRIMIR LA INFORMACIÓN FÁCILMENTE
BDD_Libros = {1:L1,
            2:L2,
            3:L3,
            4:L4,
            5:L5}

'''
╔═════════════════════════╗ 
║       FUNCIONES         ║ 
╚═════════════════════════╝ 
'''

#ESTA FUNCIÓN ES UN COMPLEMENTO A LA FUNCIÓN #DEVOLVER_LIBRO QUE PERMITE ESCRIBIR UNA RESEÑA AL DEVOLVER
def escribir_reseña(i):
    pregunta_reseña = input("Desea escribir una reseña? (Si/No)\n").upper()
    if pregunta_reseña == "SI":
        Reseña = input("Escriba su reseña:\n")
        BDD_Libros[i]["Reseña"] = Reseña
        print("Muchas gracias, su reseña ha sido guardada\n")
    elif pregunta_reseña == "NO":
        print("De acuerdo, muchas gracias")
        return
    else:
        return

#ESTA FUNCIÓN COMPARA EL INPUT CON LA INFORMACIÓN EN LA BASE DE DATOS PARA DEVOLVER LOS LIBROS QUE TENGAN LA DISPONIBILIDAD EN FALSE
def devolver_libro():
    print("\nPuede devolver un libro escribiendo el título o puede volver atrás pulsando (X)")
    libro_devuelto = input("Qué libro desea devolver?\n").upper()
    for i in BDD_Libros:
        if libro_devuelto == BDD_Libros[i]["Título"].upper(): 
            if BDD_Libros[i]["Disponibilidad"] == False:
                print("Muchas gracias por devolver el libro")
                BDD_Libros[i]["Disponibilidad"] = True
                escribir_reseña(i)
                continuar = input("Pulsa Enter para continuar...")
            else:
                print("El libro ya había sido devuelto")
                continuar = input("Pulsa Enter para continuar...")
            return
        elif libro_devuelto == "X":
            print("Volviendo atrás...")
            return
    print("La opción que ha introducido no es válida")

#ESTA FUNCIÓN ES UN COMPLEMENTO A LA FUNCIÓN #VER_CATALOGO, PERMITE VER LA RESEÑA DEL LIBRO SELECCIONADO EN EL INPUT "OPCION"
def ver_reseña():
    opcion = input("De qué libro desea ver la reseña?\n").upper()
    for i in BDD_Libros:
        if opcion == BDD_Libros[i]["Título"].upper():
            if BDD_Libros[i]["Reseña"] == "":
                print("Este libro no tiene reseña por el momento")
                continuar = input("Pulsa Enter para continuar")
                return
            else:
                print(f"El libro dispone de esta reseña:\n {BDD_Libros[i]["Reseña"]}")
                continuar = input("Pulsa Enter para continuar...")
                return
    print("No hemos encontrado el libro seleccionado")
    continuar = input("Pulsa Enter para continuar...")
    return

#ESTA FUNCIÓN PERMITE VER EL CATALOGO DE LIBROS AL COMPLETO, ESTÉN DISPONIBLES O NO
def ver_catalogo():
    print("\nEstos son los libros disponibles\n")
    for i in BDD_Libros:
        print(f"Título: {BDD_Libros[i]["Título"]} | Autor: {BDD_Libros[i]["Autor"]}")
    reseña = input("\nDesea ver la reseña de alguno de estos libros? (Si/No)\n").upper()
    if reseña == "SI":
        ver_reseña()
    elif reseña == "NO":
        print("De acuerdo, volviendo al menú...")
        return
    else:
        return

#ESTA FUNCIÓN ES UN COMPLEMENTO A LA FUNCIÓN #CONSULTAR_DISPONIBILIDAD, PERMITE RESERVAR EL LIBRO SI DE MANERA MAS ÁGIL
def reserva_rapida(i):
    reserva = input("Desea reservar este libro? (Si/No)\n").upper()
    if reserva == "SI":
        BDD_Libros[i]["Disponibilidad"] = False
        print("Has reservado el libro")
        continuar = input("Pulsa Enter para continuar...")
        return
    elif reserva == "NO":
        print("De acuerdo, volviendo al menú...")
        return
    else:
        return

#ESTA FUNCIÓN PERMITE CONSULTAR LA DISPONIBILIDAD DE UN LIBRO SELECCIONADO EN EL INPUT "LIBRO_CONSULTADO"
def consultar_disponibilidad():
    print("\nPuede consultar la disponibilidad de un libro escribiendo el título o puede volver atrás pulsando (X)")
    libro_consultado = input("De qué libro desea consultar la disponibilidad?\n").upper()
    for i in BDD_Libros:
        if libro_consultado == BDD_Libros[i]["Título"].upper(): 
            if BDD_Libros[i]["Disponibilidad"] == True:
                print("El libro seleccionado está disponible.")
                reserva_rapida(i)
            else:
                print("El libro seleccionado no está disponible")
                continuar = input("Pulsa Enter para continuar...")
            return
        elif libro_consultado == "X":
            print("Volviendo atrás...")
            return
    print("La opción que ha introducido no es válida") 

#ESTA FUNCIÓN PERMITE RESERVAR UN LIBRO PONIENDO EL NOMBRE DEL MISMO EN EL INPUT "LIBRO_RESERVADO" Y CAMBIA LA DISPONIBILIDAD
def reservar_libro():
    print("\nPuede consultar la disponibilidad de un libro escribiendo el título o puede volver atrás pulsando (X)")
    libro_reservado = input("Qué libro desea reservar?\n").upper()
    for i in BDD_Libros:
        if libro_reservado == BDD_Libros[i]["Título"].upper(): 
            if BDD_Libros[i]["Disponibilidad"] == True:
                print("Ha reservado el libro seleccionado.")
                BDD_Libros[i]["Disponibilidad"] = False
                continuar = input("Pulsa Enter para continuar...")
            else:
                print("El libro seleccionado no está disponible")
                continuar = input("Pulsa Enter para continuar...")
            return
        elif libro_reservado == "X":
            print("Volviendo atrás...")
            return
    print("La opción que ha introducido no es válida") 

'''
╔═════════════════════════╗ 
║    PROGRAMA PRINCIPAL   ║ 
╚═════════════════════════╝ 
'''
#ESTA FUNCIÓN ES EL MENÚ PRINCIPAL DONDE SE TENDRÁ QUE AÑADIR LAS NUEVAS FUNCIONALIDADES QUE SE CREEN PARA LA LIBRERÍA
def menu():
    while True:
        print("\nMenu de opciones\n")
        print("(V) Ver catálogo de libros")
        print("(C) Consultar disponibilidad de un libro")
        print("(R) Reservar un libro")
        print("(D) Devolver un libro")
        print("(S) Salir de la aplicación")
        match(input("Elige una opción: ")).upper():
            case "S":
                print("Saliendo de la aplicación...")
                break
            case "V":
                ver_catalogo()
            case "C":
                consultar_disponibilidad()
            case "R":
                reservar_libro()
            case "D":
                devolver_libro()
            case _:
                print("Esta opción no es correcta, prueba con una de las mencionadas")
                continuar = input("Pulsa Enter para continuar...")

menu()