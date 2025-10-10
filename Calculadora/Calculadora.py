from Suma.Suma import Suma
from Resta.Resta import Resta

def main():
    print ("Bienvenido a la calculadora EMAG")

    numero1 = float (input ("Digite el numero uno: "))
    numero2 = float (input ("Digite el numero dos: "))

    suma_obj = Suma(numero1, numero2)
    resta_obj = Resta(numero1, numero2)

    suma_obj.sumar()    
    resta_obj.restar()

if __name__ == "__main__":
    main()