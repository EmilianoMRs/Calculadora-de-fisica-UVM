#!/usr/bin/python3

# Aqui van librerías que se ocupen
import time


def MRU(v,t,d):
    if v <= 0:
        if t >= 0 and d >= 0:
            v = d / t
            print("\t [+] La velocidad debe ser ", v)
        elif v == v:
            print("[+] Esta es la Velocidad que ya tenias ", v)
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
                d = v * t
            print("La distancia debe ser ", d)
        elif t == t:
            print("Esta es  la distancia que ya tenias es:", d)
        else:
            print("La distancia es:", d)
    

#def MRUA():


if __name__ == "__main__":
    while True:
        print("[+] Favor de Ingresar numero: ")
        valor = input("[1] MRU: ")
        time.sleep(2)
        if valor == 1:
            print("[+] Favor ingresar los valores requeridos")
            v = float(input("[=] Velocidad: "))
            t = float(input("[=] Tiempo: "))
            d = float(input("[=] Distancia: "))
            MRU(v, t, d)
        else:
            print("No es valido")
            break
