def on_button_pressed_b():
    global pontos
    while True:
        if input.button_is_pressed(Button.A):
            inicio2 = False
            break
        pontos = input.compass_heading()
        if pontos < 22 or pontos > 337:
            pins.digital_write_pin(DigitalPin.P1, 1)
            pins.digital_write_pin(DigitalPin.P2, 0)
            pins.digital_write_pin(DigitalPin.P3, 0)
            pins.digital_write_pin(DigitalPin.P4, 0)
            pins.digital_write_pin(DigitalPin.P5, 0)
            pins.digital_write_pin(DigitalPin.P6, 0)
            pins.digital_write_pin(DigitalPin.P7, 0)
            pins.digital_write_pin(DigitalPin.P8, 0)
            basic.show_string("N")
        else:
            basic.clear_screen()
            if pontos > 67 or pontos < 23:
                basic.clear_screen()
            else:
                pins.digital_write_pin(DigitalPin.P1, 0)
                pins.digital_write_pin(DigitalPin.P2, 1)
                pins.digital_write_pin(DigitalPin.P3, 0)
                pins.digital_write_pin(DigitalPin.P4, 0)
                pins.digital_write_pin(DigitalPin.P5, 0)
                pins.digital_write_pin(DigitalPin.P6, 0)
                pins.digital_write_pin(DigitalPin.P7, 0)
                pins.digital_write_pin(DigitalPin.P8, 0)
                basic.show_string("NE")
        if pontos < 113 or pontos > 157:
            basic.clear_screen()
        else:
            pins.digital_write_pin(DigitalPin.P1, 0)
            pins.digital_write_pin(DigitalPin.P2, 0)
            pins.digital_write_pin(DigitalPin.P3, 1)
            pins.digital_write_pin(DigitalPin.P4, 0)
            pins.digital_write_pin(DigitalPin.P5, 0)
            pins.digital_write_pin(DigitalPin.P6, 0)
            pins.digital_write_pin(DigitalPin.P7, 0)
            pins.digital_write_pin(DigitalPin.P8, 0)
            basic.show_string("SE")
        if pontos < 68 or pontos > 112:
            basic.clear_screen()
        else:
            pins.digital_write_pin(DigitalPin.P1, 0)
            pins.digital_write_pin(DigitalPin.P2, 0)
            pins.digital_write_pin(DigitalPin.P3, 0)
            pins.digital_write_pin(DigitalPin.P4, 1)
            pins.digital_write_pin(DigitalPin.P5, 0)
            pins.digital_write_pin(DigitalPin.P6, 0)
            pins.digital_write_pin(DigitalPin.P7, 0)
            pins.digital_write_pin(DigitalPin.P8, 0)
            basic.show_string("L")
            pins.digital_write_pin(DigitalPin.P0, 0)
        if pontos < 158 or pontos > 202:
            basic.clear_screen()
        else:
            pins.digital_write_pin(DigitalPin.P1, 0)
            pins.digital_write_pin(DigitalPin.P2, 0)
            pins.digital_write_pin(DigitalPin.P3, 0)
            pins.digital_write_pin(DigitalPin.P4, 0)
            pins.digital_write_pin(DigitalPin.P5, 1)
            pins.digital_write_pin(DigitalPin.P6, 0)
            pins.digital_write_pin(DigitalPin.P7, 0)
            pins.digital_write_pin(DigitalPin.P8, 0)
            basic.show_string("S")
        pins.digital_write_pin(DigitalPin.P0, 0)
        if pontos < 203 or pontos > 247:
            basic.clear_screen()
        else:
            pins.digital_write_pin(DigitalPin.P1, 0)
            pins.digital_write_pin(DigitalPin.P2, 0)
            pins.digital_write_pin(DigitalPin.P3, 0)
            pins.digital_write_pin(DigitalPin.P4, 0)
            pins.digital_write_pin(DigitalPin.P5, 0)
            pins.digital_write_pin(DigitalPin.P6, 1)
            pins.digital_write_pin(DigitalPin.P7, 0)
            pins.digital_write_pin(DigitalPin.P8, 0)
            basic.show_string("SO")
            pins.digital_write_pin(DigitalPin.P0, 0)
        if pontos < 248 or pontos > 292:
            basic.clear_screen()
        else:
            pins.digital_write_pin(DigitalPin.P1, 0)
            pins.digital_write_pin(DigitalPin.P2, 0)
            pins.digital_write_pin(DigitalPin.P3, 0)
            pins.digital_write_pin(DigitalPin.P4, 0)
            pins.digital_write_pin(DigitalPin.P5, 0)
            pins.digital_write_pin(DigitalPin.P6, 0)
            pins.digital_write_pin(DigitalPin.P7, 1)
            pins.digital_write_pin(DigitalPin.P8, 0)
            basic.show_string("O")
            pins.digital_write_pin(DigitalPin.P0, 0)
        if pontos < 293 or pontos > 336:
            basic.clear_screen()
        else:
            pins.digital_write_pin(DigitalPin.P1, 0)
            pins.digital_write_pin(DigitalPin.P2, 0)
            pins.digital_write_pin(DigitalPin.P3, 0)
            pins.digital_write_pin(DigitalPin.P4, 0)
            pins.digital_write_pin(DigitalPin.P5, 0)
            pins.digital_write_pin(DigitalPin.P6, 0)
            pins.digital_write_pin(DigitalPin.P7, 0)
            pins.digital_write_pin(DigitalPin.P8, 1)
            basic.show_string("NO")
            pins.digital_write_pin(DigitalPin.P0, 0)
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
