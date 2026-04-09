print("\tAGENDA DE TURNOS")

lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""
martes1 = ""
martes2 = ""
martes3 = ""

while True:
    tiene_numero = False
    operador = input("\nIngresar nombre del operador: ")
    if operador == "":
        print("\n*** Debe ingresar un nombre")
        continue
    
    for letra in (operador):
        if letra.isdigit():
            print("\n*** EL nombre del operador no debe contener numeros")
            tiene_numero = True
            break
    if tiene_numero:
        continue
    else:
        break   
op = ""
while op != "5":
    print("\n\tMENU DE OPCIONES")
    print("\n1. Reservar turno ")
    print("2. Cancelar turno")
    print("3. Ver agenda del día")
    print("4. Ver resumen general")
    print("5. Cerrar sistema")
    op = input("\nIngresar una opcion: ")
    
    if op == "1":
        
        while True:
            print("\n1. Para reservar dia lunes")
            print("2. Para reservar dia martes")
            dia = input("\nIngresar opcion: ")
            if dia not in ("1", "2"):
                print("\n***Opcion invalida")
                continue
            else:
                break
        while True:
            nombre = input("\n-Ingresar nombre: ").capitalize()
            if nombre.isalpha():
                apellido = input("-Ingresar apellido: ").capitalize()
                if apellido.isalpha():
                    nombre = nombre + " " + apellido
                    break
                else:
                    print("\n*** El apellido no debe contener numeros ni espacios")
                    continue
            else:
                print("\n*** El nombre no debe contener numeros ni espacios")
        if dia == "1":
            if nombre in (lunes1,lunes2,lunes3,lunes4):
                print("\n*** Ya existe una reserva con ese nombre")
                continue
            if lunes1 == "":
                lunes1 = nombre
            elif lunes2 == "":
                lunes2 = nombre
            elif lunes3 == "":
                lunes3 = nombre
            elif lunes4 == "":
                lunes4 = nombre
            else:
                print("\n*** No quedan reservas disponibles para dia lunes.")
        elif dia == "2":
            if nombre in (martes1,martes2,martes3):
                print("\n*** Ya existe una reserva con ese nombre")
                continue
            if martes1 == "":
                martes1 = nombre
            elif martes2 == "":
                martes2 = nombre
            elif martes3 == "":
                martes3 = nombre
            else:
                print("\n*** No quedan reservas disponibles para dia martes.")
    
    elif op == "2":
        while True:
            nombre = input("\n-Ingresar nombre: ").capitalize()
            if nombre.isalpha():
                apellido = input("-Ingresar apellido: ").capitalize()
                if apellido.isalpha():
                    nombre = nombre + " " + apellido
                    break
                else:
                    print("\n*** El apellido no debe contener numeros ni espacios")
                    continue
            else:
                print("\n*** El nombre no debe contener numeros ni espacios")
        
        if lunes1 == nombre:
            lunes1 = ""
            print("\nReserva cancelada.")
        elif lunes2 == nombre:
            lunes2 = ""
            print("\nReserva cancelada.")
        elif lunes3 == nombre:
            lunes3 = ""
            print("\nReserva cancelada.")
        elif lunes4 == nombre:
            lunes4 = ""
            print("\nReserva cancelada.")
        elif martes1 == nombre:
            martes1 = ""
            print("\nReserva cancelada.")
        elif martes2 == nombre:
            martes2 = ""
            print("\nReserva cancelada.")
        elif martes3 == nombre:
            lunes3 = ""
            print("\nReserva cancelada.")
        else:
            print("\n*** No se encontro reserva con ese nombre")
    elif op == "3":
        print("\n1. Para ver agenda del dia lunes")
        print("2. Para ver agenda del dia martes")
        while True:
            dia = input("\nIngresar opcion: ")
            if dia not in ("1", "2"):
                print("\n***Opcion invalida")
                continue
            else:
                break
        if dia == "1":
            print("\nAgenda dia lunes")
            print(f"Turno 1: {lunes1}")
            print(f"Turno 2: {lunes2}")
            print(f"Turno 3: {lunes3}")
            print(f"Turno 4: {lunes4}")
            input("\nPresione una tecla para continuar")
        else:
            print("\nAgenda dia martes")
            print(f"Turno 1: {martes1}")
            print(f"Turno 2: {martes2}")
            print(f"Turno 3: {martes3}")
            input("\nPresione una tecla para continuar")
    
    elif op == "4":
        print("\n\tAGENDA")
        print("\nAgenda dia lunes")
        print(f"Turno 1: {lunes1}")
        print(f"Turno 2: {lunes2}")
        print(f"Turno 3: {lunes3}")
        print(f"Turno 4: {lunes4}")
        print("\nAgenda dia martes")
        print(f"Turno 1: {martes1}")
        print(f"Turno 2: {martes2}")
        print(f"Turno 3: {martes3}")
        input("\nPresione una tecla para continuar")
    elif op == "5":
        pass
    else:
        print("Opcion incorrecta, intentelo de nuevo.")



