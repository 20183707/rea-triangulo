// Daniel Portillo Madrid
// 20183707
//  6 "A"
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    base = 4
    altura = 5
    // Mostrar la base del triángulo
    basic.showString("b")
    basic.pause(400)
    basic.showNumber(base)
    basic.pause(800)
    // Mostrar la altura del triángulo
    basic.showString("a")
    basic.pause(400)
    basic.showNumber(altura)
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    // Fórmula para calcular el área
    let area = base * altura / 2
    basic.clearScreen()
    basic.pause(600)
    basic.showString("x")
    basic.clearScreen()
    basic.showNumber(area)
    basic.pause(600)
    basic.clearScreen()
    basic.showIcon(IconNames.Yes)
    basic.pause(200)
})
let base = 0
let altura = 0
basic.showLeds(`
    * * * * *
        . . * . .
        . * . * .
        . . * . .
        * * * * *
`)
basic.pause(500)
// basic.show_string("Tablas de multiplicar")
basic.clearScreen()
basic.forever(function on_forever() {
    
})
