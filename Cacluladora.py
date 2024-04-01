from pyfiglet import Figlet, FigletFont

def menu():
    
    fi = Figlet(font='slant').renderText
    f = format("")
    print("""
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░   ░░░░░░░░░░░░░░░   ░░░░░░░░░░░░░░░░░░   ░░░░░░░░░░░░░░░░░   ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░   ░░░░░░░░░░░░░░░░░░░░░░░   ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
▒▒   ▒▒▒   ▒▒▒▒▒▒▒▒▒▒▒▒   ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒   ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒   ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒   ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒  ▒▒▒▒▒▒  ▒▒▒▒▒▒▒▒▒▒  ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒   ▒▒▒▒▒▒▒▒▒▒▒   ▒▒▒▒▒   ▒▒▒▒    ▒   ▒▒   ▒   ▒▒▒▒   ▒▒▒▒▒▒▒▒▒▒   ▒▒▒▒▒   ▒▒▒▒▒  ▒    ▒▒▒▒   ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒   ▒▒▒▒▒   ▒▒▒▒▒▒▒▒▒▒▒    ▒  ▒▒▒▒▒▒▒     ▒▒▒▒▒▒▒▒▒    ▒▒▒▒   ▒▒▒▒
▓   ▓▓▓▓▓▓▓▓▓   ▓▓   ▓▓   ▓▓   ▓▓▓▓   ▓▓   ▓   ▓▓   ▓▓   ▓▓▓   ▓   ▓▓▓   ▓▓   ▓▓▓   ▓▓▓▓▓   ▓▓   ▓▓▓▓▓▓▓▓▓   ▓   ▓▓▓  ▓▓▓   ▓▓▓▓▓▓▓▓▓▓   ▓▓▓▓   ▓   ▓▓▓▓▓   ▓▓   ▓▓▓▓▓   ▓▓   ▓
▓   ▓▓▓▓▓▓▓▓   ▓▓▓   ▓▓   ▓   ▓▓▓▓▓   ▓▓   ▓   ▓   ▓▓▓   ▓▓  ▓▓▓   ▓▓   ▓▓▓▓   ▓▓   ▓▓▓▓   ▓▓▓   ▓▓▓▓▓▓▓▓  ▓▓▓   ▓▓         ▓▓▓▓▓▓▓▓▓▓   ▓▓▓▓   ▓▓▓    ▓▓   ▓   ▓▓▓▓▓   ▓▓▓   ▓
▓▓   ▓▓▓   ▓   ▓▓▓   ▓▓   ▓▓   ▓▓▓▓   ▓▓   ▓   ▓   ▓▓▓   ▓▓  ▓▓▓   ▓▓▓   ▓▓   ▓▓▓   ▓▓▓▓   ▓▓▓   ▓▓▓▓▓▓▓▓  ▓▓▓   ▓▓  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓   ▓▓▓▓   ▓▓▓▓▓   ▓   ▓▓   ▓▓▓▓   ▓▓▓   ▓
████     █████   █    █   ████    ███      █   ███   █    ██   █   █████   █████    ██████   █    ████████   █   ████     ████████████   ████   █      ██   ████    ███   █    
███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████

    """)


    '''
    Esta va a ser una calculadora para lo de fisica 
    '''
    print("""                  
Esta es una Calculadora cientifica de fisica
por favot de teclear el numero de tu problema
porfavor de poner 0 y no dejar en blanco en los espacions que quieras resolver
1 es para Movimiento rectilineo
2 es para Movimiento en 3 dimenciones
3 es Leyes de Newton

   """)
    
    print("[+] Por favor elige un numero:")
    PP = int(input("[-] Numero="))
    '''
    el def te pregunta cual es son los datos que tienes disponibles y envase al faltante que es igual a 0 empieza a resolver el problema
    '''
    def MRU():
        print(fi("Calculadora de MRU."))
        print("""
Porfavor de elegir el numero de la calculadora que quieres
1-MRU triangulo          ---
                     ---( d )---
                    ( v )   ( t )
                    -------------
2-Despejar la differencia 
                    Δx = x₂ - x₁
                    Δt = t₂ - t₁
                    Δv = Δt / Δt
  """)
        PPMRU = int(input("porfavot elige un numero ="))

        def MRU_triangulo():
            print(fi("Estas en la calculadora de triangulo "))
            v = float(input("Dime la velocidad: "))
            t = float(input("Dime tu tiempo: "))
            d = float(input("Dime tu distancia: "))
            #este es la velocidad
            if v <= 0:
                if t >= 0 and d >= 0:
                    v = d / t
                print("La velocidad debe ser ", v)
            elif v == v:
                print("Esta es la Velocidad que ya tenias ", v)
            else:
                print("La velocidad es:", v)
            #esta es el tiempo
            if t <= 0:
                if v >= 0 and d >= 0:
                    t = d / v

            elif t == t:
                print("Este es el tiempo que ya tenias", t)
            else:
                print("el tiempo es:", t)
            #esta es la distancia
            if t <= 0:
                if t >= 0 and v >= 0:
                    d = v * t
                print("La distancia debe ser ", d)
            elif t == t:
                print("Esta es  la distancia que ya tenias es:", d)
            else:
                print("La distancia es:", d)
        def MRU_differencia():
            def deltaX():
                #es el delta x
                print("estas en delta x")
                x1 = float(input("Por favor dime la distancia 1(x1)="))
                x2 = float(input("Por favor dime la distancia 2(x2)="))
                deltax = x2 - x1
                print("""
Tu distancia 1 fue {0} y distancia 2 fue {1} asi que la diferencia de distancia es {2}m/s
                """.format(x1,x2,deltax))
            def deltaT():
                t1 = float(input("Por favor dime tu tiempo 1(x1)="))
                t2 = float(input("Por favor dime tu tiempo 2(x2)="))
                deltat = t2 - t1
                print("""
Tu tiempo 1 fue {0} y distancia 2 fue {1} asi que la diferencia de distancia es {2}m/s
                """.format(t1,t2,deltat))
            def deltaV():
                x1 = float(input("Por favor dime la distancia 1(x1)="))
                x2 = float(input("Por favor dime la distancia 2(x2)="))
                t1 = float(input("Por favor dime tu tiempo 1(x1)="))
                t2 = float(input("Por favor dime tu tiempo 2(x2)="))
                deltat = t2 - t1
                deltax = x2 - x1
                deltav = deltax/deltat
                print(deltav)
                

            print(fi("""
Calcula los deltas
            """))
            print("""
que delta quieres despejar?
por favor de poner una letra no la palabra
""")
            eleccin = input("x=(distancia),t=(tiempo),v=(Vmed)? =")
            if eleccin == "x":
                deltaX()
            elif eleccin == "t":
                deltaT()
            elif eleccin == "v":
                deltaV()
            elif():
            #es el delta x
                x1 = float(input("Por favor dime la distancia 1(x1)="))
                x2 = float(input("Por favor dime la distancia 2(x2)="))
                deltax = x1 - x2
                print("""
Tu distancia 1 fue {0} y distancia 2 fue {1} asi que la diferencia de distancia es {2}m/s
                """.format(x1,x2,deltax))
            
        if PPMRU == 1:
            MRU_triangulo()
        elif PPMRU == 2:
            MRU_differencia()
        else:
            print("Tu programa esta en otro castillo")
            MRU()

    def M3D():
        print("test 123....")
    def LawNew():
        print("test 123....")
    if PP == 1:
        print("Has elegido MRU")
        MRU()
    elif PP == 2:
        print("Has elegido Movimiento en 3 dimenciones")
        M3D()
    elif PP == 3:
        print("Has elegido Leyes de Newton")
        LawNew()
    else:
        print(""" 
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠶⢛⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡟⠁⢀⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⣾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⠇⠀⠉⢷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠋⠀⠀⠀⠀⣸⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⠁⠀⠀⠀⠀⣰⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡏⠀⠀⣀⡤⠤⣀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠁⣀⠶⠉⠀⠀⠈⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⠋⠉⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡼⠃⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡾⠁⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠃⠀⠀⠀⠀⠀⠀⠀⠀⠨⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⢲⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⢾⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡴⠊⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠳⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡴⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠞⠁⠀⠀⠀⠀⠀⢀⡤⠶⢶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⠁⢀⢀⣀⠀⢀⣠⣾⡿⠿⢿⢾⣻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢦⡀⠀⠀⠀⠀⠀⣀⣀⣀⡠⠴⠶⠶⣶⠶⠶⢦⣀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣾⠃⣿⣿⣾⢻⣿⢳⣾⣿⣯⣶⣦⣞⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠒⠒⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠙⡇⠀⠀⠈⠳⡄⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⢀⡿⢻⣏⡸⣿⣿⠘⠹⣿⣓⣒⡿⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡞⠁⠀⠀⠀⠀⠙⢆⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣧⣄⣻⣿⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣰⠟⣩⣿⣏⢿⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣆⣠⣀⣀⠀⠀⠀⠈⢳⡄⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣧⠉⠛⠂⠀⢻⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⡿⢠⣿⢽⣿⢸⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⣀⡠⠶⠊⠉⠁⠀⠀⠈⠙⠦⣀⠀⠀⠙⢆
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡆⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢷⢸⠸⣼⢿⣾⡾⠃⠀⠀⠀⠀⢀⣠⠶⠊⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⣄⠀⠈
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡄⠀⠀⠸⣿⣷⣶⣶⣶⣶⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠈⠷⠿⠿⠋⠀⠀⠀⠀⢀⡞⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⢄
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢳⡄⠀⠀⠀⠀⠀⠈⠉⠙⣿⣦⣀⠀⠀⠀⠀⠀⠀⢀⡤⠴⠶⢤⣀⠀⠀⠀⠀⠀⣾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣄⠀⠀⠀⠀⠀⠀⠀⠹⠿⣿⣿⣶⡀⠀⠀⣴⠟⠀⠀⠀⣀⡽⠂⠀⠀⠀⣸⠃⠀⠀⠀⠀⠀⠀⠀⣀⣠⠶⢺⠏⢳⡆⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢳⣄⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣷⣶⣶⣿⠿⠃⠀⠀⣿⣿⠆⠀⠀⣠⠇⠀⠀⠀⠀⠀⣠⠴⠚⠁⠀⠀⢸⡁⠀⢳⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠟⠈⠙⠶⣄⡀⠀⠀⠀⠀⠀⠀⠛⠿⣍⠁⠀⠀⢀⣿⠉⠉⠀⠀⡴⠋⠀⠀⠀⣀⡴⠋⠁⠀⠀⠀⠀⠀⢸⡅⠀⢸⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠏⠀⠀⠀⠀⠈⠉⠳⠦⣄⣀⠀⠀⠀⠀⠈⠛⠒⠒⠉⠀⣀⣀⠴⠏⠁⠀⠀⣠⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⢸⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠶⣖⣒⠒⠒⠒⠉⠉⠉⠉⠀⠀⠀⠀⣠⡞⠁⠀⠀⠀⣠⠴⠚⠁⠀⠀⠀⠈⠳⣤⡞⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⠋⠀⠀⠠⠶⣋⣡⠶⠊⠀⠀⠀⢀⣠⠶⠛⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢦⠀⠀⠀⠀⠀⠀⠀⢸⡁⠀⠀⠀⠀⠀⠉⠀⠀⣀⣠⠴⠞⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡼⠀⠀⠀⠀⠀⠀⠀⣤⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠈⢳⡀⠀⠀⠀⠀⠀⠀⠻⡄⠀⠀⢀⣠⠴⠖⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠃⠀⠀⠀⠀⠀⠀⢠⣿⡄⠀⠀⠀⠀⣿⣦⠀⠀⠀⠀⠀⠀⢷⠀⠀⠀⠀⠀⢀⡴⠛⠀⠀⠈⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡏⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⠀⠈⣧⠀⠀⢀⡴⠋⠀⠀⠀⠀⢀⣽⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠁⠀⠀⠀⠀⠀⠀⠀⠈⣿⠿⠀⠀⠀⠀⠘⢿⠆⠀⠀⠀⠀⠀⠀⠸⡄⠀⠈⢧⡀⠀⠀⢶⠞⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢠⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⠀⠀⠀⣹⠆⠀⣸⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣼⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣧⣀⠞⠁⣠⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢤⣤⡤⠤⠤⠤⠴⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠿⣶⡊⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠉⢉⣳⡦⢤⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠑⠶⢦⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣀⣴⣖⣉⣁⣀⣀⠀⢉⣻⡆⠀⠀⠀⠀⣀⡤⠶⣄⣀⠀⠀⠀⠀⠀⣠⠤⣄⣀⣀⠀⠀⠀⠀⠀⢶⠚⠙⠒⠒⣶⠶⠶⠾⠿⠶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠉⢉⡉⠀⠀⡀⣘⠛⠉⠁⣳⣠⠴⠖⠋⡉⣧⣴⠋⠉⠙⠲⠶⠴⡞⠳⣄⣀⡟⠉⠉⠒⠶⠤⣄⣈⣟⠲⠦⠤⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        """)
menu()
