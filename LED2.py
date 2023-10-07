from gpiozero import LED

#Se declaran los LEDs
ledVerde = LED(17)
ledAmbar = LED(27)
ledRojo = LED(22)

def Semaforo(instruccion):
    #Se apagan todos los LEDS
    ledVerde.off()
    ledAmbar.off()
    ledRojo.off()

    #Se recibe la instruccion y se prende el LED correspondiente
    if instruccion == 'siga':
        ledVerde.on()
    elif instruccion == 'precaucion':
        ledAmbar.on()
    elif instruccion == 'alto':
        ledRojo.on()
    else:
        print('Opcion no valida, use solo "siga", "precaucion" y "alto"')

if __name__ == "__main__":
    #Se recibe la instruccion en la terminal y se llama a la funcion Semaforo de manera indefinida
    while True:
        instruccion = input("Escriba la instruccion del semaforo 'siga', 'precaucion' o 'alto'")
        Semaforo(instruccion)