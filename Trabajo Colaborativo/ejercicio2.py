usuario = "alumno"
clave = "python123"
intento = 0
while intento < 3:
            print("\nACCESO CAMPUS ")
            usuario = input("\nIngresar usuario: ")
            clave2 = input("Ingresar clave: ")       
            if usuario == "alumno" and clave == clave2:
                op = ""
                while op != "4":
                    print("\n      MENU DE OPCIONES")
                    print("\n1. Ver estado de inscripción")
                    print("2. Cambiar clave ")
                    print("3. Mostrar mensaje motivacional")
                    print("4. Salir")

                    op = input("\nIngresar una opcion: ")

                    if op == "1":
                        print("\nCondicion - Inscripto")
                        input("\nPresione una tecla para volver al menu de opciones") 
                    elif op == "2":
                        print("\nCambio de clave")
                        clave = "  "
                        clave2 = ""
                        while clave != clave2 or len(clave) < 6:
                                clave = input("\nIngresar Clave nueva (minimo 6 caracteres): ")
                                if len(clave) >= 6 :
                                    clave2 = input("Confirmar clave: ")
                                    if clave == clave2:
                                        print("\nClave generada")
                                        input("\nPresione una tecla para volver al menu de opciones") 
                                    else:
                                        print("\n*** Las claves no coinciden")
                                else:
                                    print ("\n*** La clave debe tener minimo 6 caracteres.")
                    elif op == "3":
                        print("\n- Se constante, la practica hace al maestro, con cada nuevo aprendizaje " \
                        "ya estas en ventaja con alguien que no lo ah hecho")   
                        input("\nPresione una tecla para volver al menu de opciones")             

                    elif op == "4":
                        print("\nHasta luego.")
                        intento = 0  
                    
                    if not op.isdigit():
                        print("\n*** No esta permitido caracteres ")
                    if op not in ("1","2","3","4"):
                        print("\n*** Debe ingresar un numero entre 1-4")
            else:
                print("\n*** Usuario y clave no coinciden")
                intento += 1 

            if intento == 3:
                print("\nCuenta Bloqueada.") 
                break

print("\nPrograma finalizado.")                     

