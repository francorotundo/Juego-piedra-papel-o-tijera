import random 
random.seed()
l = ["Piedra",'Papel','Tijera']

print('''
BIENVENIDO AL JUEGO DE PIEDRA, PAPEL O TIJERA
PARA JUEGAR ESTAS SON LAS OPCIONES:

1 PIEDRA
2 PAPEL
3 TIJERA
4 SALIR
''')

try:
    c = 0
    p = 0
    while (p <=3 or c <= 3):
        pc = random.randint(1, 3)
        if p==3:
            print(f":'( PERDISTE CONTRA GUIDO {p} a {c}")
            break
        if c==3:
            print(f"xD FELICITACIONES!!!\nLE GANASTE A GUIDO VAN ROSSUM!!! {c} a {p}")
            break

        opc = int(input("¿1 Piedra, 2 papel o 3 tijera? "))
        if opc == pc:
            print(f'Elejiste {l[opc-1]} contra {l[pc-1]}')
            print("Es un empate. Intentalo de nuevo.")
        elif opc != pc:
            if pc == 1 and opc == 3 or pc == 2 and opc == 1 or pc == 3 and opc == 2:
                p+=1
                print(f'Elejiste {l[opc-1]} contra {l[pc-1]}')
                print(f"Perdiste esta ronda, vas {c} a {p}")
            if pc == 3 and opc == 1 or pc == 1 and opc == 2 or pc == 2 and opc == 3:
                c+=1
                print(f'Elejiste {l[opc-1]} contra {l[pc-1]}')
                print(f"Muy bien... Ganaste esta ronda, vas {c} a {p}")
        elif opc==4:
            print("Hasta la proxima.")
            break
        else:
            print(f'La opción {opc} no es valida.')
    
    
except:
    print("No se aceptan letras solo los numeros del 1 al 3 para jugar y 4 para salir")
