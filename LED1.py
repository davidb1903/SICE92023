from gpiozero import LED, Button

#Declarar los 3 leds. Verde - 17, Ambar - 18, Rojo - 19
ledVerde = LED(17)
ledAmbar = LED(27)
ledRojo = LED(22)

#Declarar el boton en la entrada 20
boton = Button(4)

#Iniciar el programa con el Led verde prendido
ledVerde.on()

def cambiarLED():
    if ledVerde.is_active:
        ledVerde.off()
        ledAmbar.on()
    elif ledAmbar.is_active:
        ledAmbar.off()
        ledRojo.on()
    elif ledRojo.is_active:
        ledRojo.off()
        ledVerde.on()


if __name__  == "__main__":
    while True:
        boton.when_pressed = cambiarLED
