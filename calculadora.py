import math, cmath

signos = [  "▛▔A▔▜ \n  % \n▙▃ ▃▟\n",
          "\n▛▔B▔▜ \n  + \n▙▃ ▃▟\n",
          "\n▛▔C▔▜ \n  - \n▙▃ ▃▟\n",
          "\n▛▔D▔▜ \n  / \n▙▃ ▃▟\n",
          "\n▛▔E▔▜ \n  x \n▙▃ ▃▟\n",
          "\n▛▔F▔▜ \n  √ \n▙▃ ▃▟\n",
          "\n▛▔G▔▜ \n  x^ \n▙▃ ▃▟\n"]

while True:
    operacion = input(f"que tipo de operaciones quieres hacer ?\n{signos[0]}{signos[1]}{signos[2]}{signos[3]}{signos[4]}{signos[5]}{signos[6]} \n"
                      "contesta con la letra: ")
    
    if operacion.lower() == "b":
        numero_uno = input(f"haz elegido: {operacion}, Cual es el primer numero: ")
        numero_dos = input(f"ok, elegiste {numero_uno}, Cual es el segundo numero: ")
        ecuacion = float(numero_uno) + float(numero_dos)
        print(f"el resultado de tu operacion Suma es: {ecuacion:.2f}")

        again = input("quieres hacer otra operacion: si o no: ")
        if again == "si":
            continue
        else:
            break
    elif operacion.lower()  == "c":
        numero_uno = input(f"haz elegido: {operacion}, Cual es el primer numero: ")
        numero_dos = input(f"ok, elegiste {numero_uno}, Cual es el segundo numero: ")
        ecuacion = float(numero_uno) - float(numero_dos)
        print(f"el resultado de tu operacion Resta es: {ecuacion:.2f}")

        again = input("quieres hacer otra operacion: si o no: ")
        if again == "si":
            continue
        else:
            break
    elif operacion.lower()  == "d":
        numero_uno = input(f"haz elegido: {operacion}, Cual es el primer numero: ")
        numero_dos = input(f"ok, elegiste {numero_uno}, Cual es el segundo numero: ")
        ecuacion = float(numero_uno) / float(numero_dos)
        print(f"el resultado de tu operacion Division es: {ecuacion:.2f}")

        again = input("quieres hacer otra operacion: si o no: ")
        if again == "si":
            continue
        else:
            break
    elif operacion.lower()  == "e":
        numero_uno = input(f"haz elegido: {operacion}, Cual es el primer numero: ")
        numero_dos = input(f"ok, elegiste {numero_uno}, Cual es el segundo numero: ")
        ecuacion = float(numero_uno) * float(numero_dos)
        print(f"el resultado de tu operacion Multiplicacion es: {ecuacion:.2f}")

        again = input("quieres hacer otra operacion: si o no: ")
        if again == "si":
            continue
        else:
            break
    elif operacion.lower()  == "f":
        try:
            numero_uno = input(f"haz elegido: {operacion}, Cual es el numero: ")
            a = math.sqrt(float(numero_uno))
            print(f"el resultado de tu Raiz Cuadrada es: {a:.2f}")
        except:
            print(f"Los numeros negativos, como {numero_uno} no aplican para raiz cuadrada, ya que son numeros imaginarios")
            b = cmath.sqrt(float(numero_uno))
            print(f"el resultado de tu operacion con Numeros Imaginarios es: {b}")

        again = input("quieres hacer otra operacion: si o no: ")
        if again == "si":
            continue
        else:
            break
    elif operacion.lower()  == "a":
        cantidad = input("cual es la cantidad principal: ")
        porcentaje = input("cual es el porcentaje ")
        ecuacion = (float(cantidad) * float(porcentaje)) / 100

        if float(porcentaje) < 0:
            print(f"ok, entonces quieres saber cual es el resultado de disminuir el {porcentaje}% a ${cantidad}") 
            disminucion = 100*(float(porcentaje) / float(cantidad))
            resultado = 100 + disminucion
            print(f"el resultado de Disminuir el {porcentaje}% a ${cantidad} es: ${resultado:.2f}")

        elif float(cantidad) < 0:
            ecuacion = (float(cantidad) * float(porcentaje)) / 100
            print(f"el resultado de Disminuir del Porcentaje es ${ecuacion:.2f}")

        elif float(cantidad) > 0 or float(porcentaje) > 0: 
            print(f"el resultado de Sacar el Porcentaje es ${ecuacion:.2f}")

        again = input("quieres hacer otra operacion: si o no: ")
        if again == "si":
            continue
        else:
            break
    elif operacion.lower()  == "g":
        pregunta = input("es una raiz cuadrada, si o no ")

        if pregunta == "si":
            numero = input("cual es el numero que quieres potenciar: ")
            ecuacion = pow(float(numero),2)
            print(f"la potenciacion al cuadrado de {numero} es {ecuacion}")
        elif pregunta == "no":
            numero = input("cual es el numero que quieres potenciar: ")
            valor = input("cual es el exponente ")
            ecuacion = pow(float(numero),float(valor))
            print(f"la potenciacion al {valor} de {numero} es {ecuacion}")

        again = input("quieres hacer otra operacion: si o no: ")
        if again == "si":
            continue
        else:
            break
    else:
        print("nesecito que me respondas, si no quieres o fue un error lo que escribiste, solo comenta: no")

        again = input("quieres hacer alguna operacion: si o no: ")
        if again == "si":
            continue
        else:
            break
