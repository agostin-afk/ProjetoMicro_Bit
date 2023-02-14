let letra = ""
function Pins(letra: string) {
    if (letra == "N") {
        pins.digitalWritePin(DigitalPin.P1, 1)
        basic.pause(500)
        pins.digitalWritePin(DigitalPin.P1, 0)
    } else if (letra == "NE") {
        pins.digitalWritePin(DigitalPin.P2, 1)
        basic.pause(500)
        pins.digitalWritePin(DigitalPin.P2, 0)
    } else if (letra == "SE") {
        pins.digitalWritePin(DigitalPin.P3, 1)
        basic.pause(500)
        pins.digitalWritePin(DigitalPin.P3, 0)
    } else if (letra == "L") {
        pins.digitalWritePin(DigitalPin.P4, 1)
        basic.pause(500)
        pins.digitalWritePin(DigitalPin.P4, 0)
    } else if (letra == "S") {
        pins.digitalWritePin(DigitalPin.P5, 1)
        basic.pause(500)
        pins.digitalWritePin(DigitalPin.P5, 0)
    } else if (letra == "SO") {
        pins.digitalWritePin(DigitalPin.P6, 1)
        basic.pause(500)
        pins.digitalWritePin(DigitalPin.P6, 0)
    } else if (letra == "O") {
        pins.digitalWritePin(DigitalPin.P7, 1)
        basic.pause(500)
        pins.digitalWritePin(DigitalPin.P7, 0)
    } else {
        pins.digitalWritePin(DigitalPin.P8, 1)
        basic.pause(500)
        pins.digitalWritePin(DigitalPin.P8, 0)
    }
    
}

input.onButtonPressed(Button.B, function on_button_pressed_b() {
    let inicio2: boolean;
    let letra: string;
    
    while (true) {
        if (input.buttonIsPressed(Button.A)) {
            inicio2 = false
            break
        }
        
        pontos = input.compassHeading()
        if (pontos < 22 || pontos > 337) {
            letra = "N"
            basic.showString(letra)
            Pins(letra)
        } else {
            basic.clearScreen()
            if (pontos > 67 || pontos < 23) {
                basic.clearScreen()
            } else {
                letra = "NE"
                basic.showString(letra)
                Pins(letra)
            }
            
        }
        
        if (pontos < 113 || pontos > 157) {
            basic.clearScreen()
        } else {
            letra = "SE"
            basic.showString(letra)
            Pins(letra)
        }
        
        if (pontos < 68 || pontos > 112) {
            basic.clearScreen()
        } else {
            letra = "L"
            basic.showString(letra)
            Pins(letra)
        }
        
        if (pontos < 158 || pontos > 202) {
            basic.clearScreen()
        } else {
            letra = "S"
            basic.showString(letra)
            Pins(letra)
        }
        
        if (pontos < 203 || pontos > 247) {
            basic.clearScreen()
        } else {
            letra = "SO"
            basic.showString(letra)
            Pins(letra)
        }
        
        if (pontos < 248 || pontos > 292) {
            basic.clearScreen()
        } else {
            letra = "O"
            basic.showString(letra)
            Pins(letra)
        }
        
        if (pontos < 293 || pontos > 336) {
            basic.clearScreen()
        } else {
            letra = "NO"
            basic.showString(letra)
            Pins(letra)
        }
        
    }
})
let passo = 0
let pontos = 0
basic.clearScreen()
let inicio = true
basic.forever(function on_forever() {
    
    if (input.buttonIsPressed(Button.AB)) {
        passo += 1
        basic.showNumber(passo)
    }
    
})
