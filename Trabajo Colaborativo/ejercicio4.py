print("\tEscape Room - La Bóveda ")

energia = 100 
tiempo = 12 
cerraduras_abiertas = 0 
alarma = False 
codigo_parcial = "" 
consecutiva = 0
bloqueado = False

while True:
    apellido = input("\nIngresar apellido: ")
    if apellido.isalpha():
        apellido = apellido.capitalize()
        break
    else:
        print("\nIngresar un apellido que contenga solo letras(no debe contener espacios en blanco)")

while True:
    nombre = input("\nIngresar nombre: ")
    if nombre.isalpha():
        nombre = nombre.capitalize()
        break
    else:
        print("\nIngresar un nombre que contenga solo letras(no debe contener espacios en blanco)")

nombre_completo = apellido + " " + nombre
print (f"\nNombre registrado: {nombre_completo}")

while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and not bloqueado:
    print("\n\tMenu De Opciones")       
    print("\n1. Forzar cerradura")
    print("2. Hackear panel ")
    print("3. Descansar")

    op = input("\nIngresar una opcion: ")
    if  not op.isdigit():
        print("\n***Debe ingresar un numero. ")
        continue

    if int(op) not in (1,2,3):
        print("\n* Debe seleccionar alguna de las 3 opciones ")
        continue

    if op == "1":

        if alarma:
            print("\n*** Cerradura trabada, la alarma esta activa!")
            continue

        consecutiva +=1

        if consecutiva == 3:
            alarma = True
            print("\n*** Cerradura trabada, se activo la alarma!")
            continue

        if energia >= 20 and tiempo >= 2 :
            energia -= 20
            tiempo -= 2
        else:
            print("\nEnergia o tiempo insuficiente para realizar esta operacion")
            continue
            
        if energia < 40:
            print("Riesgo de alarma")
            numero = int(input("\nIngresar un numero entre (1-3): "))
            if numero == 3:
                alarma = True
            else:
                cerraduras_abiertas +=1
                print("\n*** Se abrio una cerradura ***")
                print(f"Cerraduras abiertas {cerraduras_abiertas}")

    elif op == "2":
        
        if energia >= 10 and tiempo >= 3:
            consecutiva = 0
            energia -= 10
            tiempo -= 3
            for i in range(1,5):
                while True:
                    letra = input("\nIngresar una sola letra: ")
                    if len(letra) != 1 or not letra.isalpha():
                        print("\nDebe ingresar un solo caracter y no debe ser un numero")
                    else:
                        codigo_parcial += letra
                        break
        else:
            print("\nEnergia o tiempo insuficiente para realizar esta operacion")
            continue
            
            
        print(f"\n-Codigo: {codigo_parcial}")
        if len(codigo_parcial) >=8:
            cerraduras_abiertas +=1
            print("\n*** Se abrrio una cerradura ***")
            print(f"-Cerraduras abiertas: {cerraduras_abiertas}")
            
    elif op == "3":
        consecutiva = 0
        tiempo -= 1
        
        if energia <= 85:
            energia += 15
            print("\n+ 15 de energia")
        else:
            energia = 100
            print("\nEnergia al 100")
        
        if alarma:
            energia -= 10
            print("\n -10 de energia extra por alarma activada")
    
    print(f"\n-Energia: {energia}")
    print(f"-Tiempo:  {tiempo}")


    if cerraduras_abiertas == 3:
        print("\nVictoria")
        break
    if energia <=0 or tiempo <=0:
        print("\nDerrota, se te termino el tiempo")
        break
    if energia <= 0:
        print("\nDerrota, se te termino la energia")
        break

    if alarma and tiempo <= 3:
        print("\nSistema bloqueado")
        bloqueado = True





