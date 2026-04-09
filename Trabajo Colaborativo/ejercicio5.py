print("\n\tEscape Room:La Arena del Gladiador")

vida_gladiador = 100 
vida_enemigo = 100 
pociones_vida_gladiador = 3
pociones_vida_enemigo = 3
daño_base_gladiador= 15  
daño_base_enemigo = 12
turno_gladiador = True 
daño_critico = 0

while True:
    nombre_gladiador = input("\nNombre del gladiador: ")
    if nombre_gladiador.isalpha():
        break
    else:
        print("\n *** Error: Solo se permiten letras")

while vida_gladiador > 0 and vida_enemigo > 0:

    print(f"\n- Vida de {nombre_gladiador}: {vida_gladiador}")
    print(f"- Posiones de {nombre_gladiador}: {pociones_vida_gladiador}")
    print(f"\n- Vida de enemigo: {vida_enemigo}")
    print(f"- Posiones de enemigo: {pociones_vida_enemigo}")
    
    print("\n\tEligir accion")
    print("\n1. Ataque pesado")
    print("2. Ráfaga veloz") #uso de for 
    print("3. Curar")

    while vida_gladiador > 0 and vida_enemigo > 0:
        op = input("\nIngresar una opcion: ")
        if op.isdigit():
            break
        else:
            print("\n***Debe ingresar un numero")
    
    if op == "1":
        if vida_enemigo < 20:
            daño_critico = daño_base_gladiador * 1.5 
            vida_enemigo -= daño_critico
            print(f"\nDaño critico!")
            print(f"Atacaste al enemigo por {daño_critico} puntos de daño")
        else:
            print("\nAtaque sin efecto! +0 de daño")
        vida_gladiador -= 12
        print("\n¡El enemigo te atacó por 12 puntos de daño!")
    
    elif op == "2":
        print("\n¡Inicias una ráfaga de golpes! ")
        for ataque in range(0,3):
            vida_enemigo -= 5
            print("Golpe conectado por 5 de daño")
        vida_gladiador -= 12
        print("¡El enemigo te atacó por 12 puntos de daño!")

    elif op == "3":
        if pociones_vida_gladiador > 0:
            vida_gladiador += 30
        if posiones > 0:
            pociones_vida_gladiador -=1
            print("\nSe consumio una posion")
        else:
            print("¡No quedan pociones!")
            vida_gladiador -= 12
            print("¡El enemigo te atacó por 12 puntos de daño!")

        print("¡El enemigo contraataca por 12 puntos!  ")
        vida_gladiador -= daño_base_enemigo
    else:
        print("\n*** Debe ingresar un numero (1,2 o 3)")
    
if vida_gladiador > 0:
    print(f"\n¡VICTORIA! {nombre_gladiador} ha ganado la batalla.")
else:
    print("\nDERROTA. Has caído en combate.")
