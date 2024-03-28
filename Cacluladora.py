from pyfiglet import Figlet


def menu():
  f = Figlet(font='slant')
  print(f.renderText("Calculadora de física."))


'''
Esta va a ser una calculadora para lo de fisica 
'''
print("""Esta es una Calculadora cientifica de fisica
por favot de teclear el numero de tu problema
porfavor de poner 0 y no dejar en blanco en los espacions que quieras resolver
1 es para MRU""")

print("[+] Por favor elige un numero:")
PP = int(input("[-] Numero="))
'''
el def te pregunta cual es son los datos que tienes disponibles y envase al faltante que es igual a 0 empieza a resolver el problema
'''
def MRU():
    f = Figlet(font='slant')
    print(f.renderText("Calculadora de MRU."))
    v = float(input("Dime la velocidad: "))
    t = float(input("Dime tu tiempo: "))
    d = float(input("Dime tu distancia: "))
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
        print("el tiempo debe ser ", t)
    elif t == t:
      print("Este es el tiempo que ya tenias", t)
    else:
      print("el tiempo es:", t)
    #esta es la distancia
    if t <= 0:
      if t >= 0 and v >= 0:
        d = t * v
        print("La distancia debe ser ", d)
    elif t == t:
      print("Esta es  la distancia que ya tenias es:", d)
    else:
      print("La distancia es:", d)

if __name__ == "__main__":
  if PP == 1:
    print("Has elegido MRU")
    MRU()
  if PP == 3:
    menu()

