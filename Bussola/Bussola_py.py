letra = ''

def Pins(letra):
    if letra == 'N':
        pins.digital_write_pin(DigitalPin.P1, 1)
        basic.pause(500)
        pins.digital_write_pin(DigitalPin.P1, 0)
    elif letra == 'NE':
        pins.digital_write_pin(DigitalPin.P2, 1)
        basic.pause(500)
        pins.digital_write_pin(DigitalPin.P2, 0)
    elif letra == 'SE':
        pins.digital_write_pin(DigitalPin.P3, 1)
        basic.pause(500)
        pins.digital_write_pin(DigitalPin.P3, 0)
    elif letra == 'L':
        pins.digital_write_pin(DigitalPin.P4, 1)
        basic.pause(500)
        pins.digital_write_pin(DigitalPin.P4, 0)
    elif letra == 'S':
        pins.digital_write_pin(DigitalPin.P5, 1)
        basic.pause(500)
        pins.digital_write_pin(DigitalPin.P5, 0)
    elif letra == 'SO':
        pins.digital_write_pin(DigitalPin.P6, 1)
        basic.pause(500)
        pins.digital_write_pin(DigitalPin.P6, 0)
    elif letra == 'O':
        pins.digital_write_pin(DigitalPin.P7, 1)
        basic.pause(500)
        pins.digital_write_pin(DigitalPin.P7, 0)
    else:
        pins.digital_write_pin(DigitalPin.P8, 1)
        basic.pause(500)
        pins.digital_write_pin(DigitalPin.P8, 0)
        

def on_button_pressed_b():
    global pontos
    while True:
        if input.button_is_pressed(Button.A):
            inicio2 = False
            break
        pontos = input.compass_heading()
        if pontos < 22 or pontos > 337:
            letra = 'N'
            basic.show_string(letra)
            Pins(letra)
        else:
            basic.clear_screen()
            if pontos > 67 or pontos < 23:
                basic.clear_screen()
            else:
                letra = 'NE'
                basic.show_string(letra)
                Pins(letra)
        if pontos < 113 or pontos > 157:
            basic.clear_screen()
        else:
            letra = 'SE'
            basic.show_string(letra)
            Pins(letra)
        if pontos < 68 or pontos > 112:
            basic.clear_screen()
        else:
            letra = 'L'
            basic.show_string(letra)
            Pins(letra)
        if pontos < 158 or pontos > 202:
            basic.clear_screen()
        else:
            letra = 'S'
            basic.show_string(letra)
            Pins(letra)
        if pontos < 203 or pontos > 247:
            basic.clear_screen()
        else:
            letra = 'SO'
            basic.show_string(letra)
            Pins(letra)
        if pontos < 248 or pontos > 292:
            basic.clear_screen()
        else:
            letra = 'O'
            basic.show_string(letra)
            Pins(letra)
        if pontos < 293 or pontos > 336:
            basic.clear_screen()
        else:
            letra = 'NO'
            basic.show_string(letra)
            Pins(letra)
input.on_button_pressed(Button.B, on_button_pressed_b)

passo = 0
pontos = 0
basic.clear_screen()
inicio = True

def on_forever():
    global passo
    if input.button_is_pressed(Button.AB):
        passo += 1
        basic.show_number(passo)
basic.forever(on_forever)
