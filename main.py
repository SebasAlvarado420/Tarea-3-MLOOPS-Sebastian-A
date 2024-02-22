def sumar(a, b):
    return a + b

def main():
    numero1 = float(input("Ingrese un numero: "))
    numero2 = float(input("Ingrese el segundo número: "))
    resultado = sumar(numero1, numero2)
    print(f"El resultado de la suma es: {resultado}")

if __name__ == "__main__":
    main()
