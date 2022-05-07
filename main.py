#Daniel Portillo Madrid
#20183707
# 6 "A"

def on_button_pressed_a():
    global base, altura
    
    base = 4
    altura = 5  
        
    #Mostrar la base del triángulo
    basic.show_string("b")
    basic.pause(400)
    basic.show_number(base)
    basic.pause(800)


    #Mostrar la altura del triángulo
    basic.show_string("a")
    basic.pause(400)
    basic.show_number(altura)

input.on_button_pressed(Button.A, on_button_pressed_a)


def on_button_pressed_b():

    #Fórmula para calcular el área
    area = (base * altura) / 2
    
    basic.clear_screen()
    basic.pause(600)
    basic.show_string("x")
    basic.clear_screen()
    basic.show_number(area)
    basic.pause(600)
    basic.clear_screen()
    basic.show_icon(IconNames.YES)
    basic.pause(200)
input.on_button_pressed(Button.B, on_button_pressed_b)

base = 0
altura = 0
basic.show_leds("""
    * * * * *
        . . * . .
        . * . * .
        . . * . .
        * * * * *
""")
basic.pause(500)
#basic.show_string("Tablas de multiplicar")
basic.clear_screen()

def on_forever():
    pass
basic.forever(on_forever)
