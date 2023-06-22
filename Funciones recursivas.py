# Funciones recursivas

def cuenta_regresiva(num):
    if num>0:
        print(num)
        cuenta_regresiva(num - 1)
    else:
        print("Booooooom !!!")

numero = int(input("Digite un numero -> "))
cuenta_regresiva(numero)

# Carolina EM