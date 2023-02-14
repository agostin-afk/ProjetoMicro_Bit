Gas = 0
base = 770
'''def on_forever():
    Gas = pins.analog_read_pin(AnalogPin.P0)
    basic.show_number(Gas)
basic.forever(on_forever)
'''
def on_forever():
    global Gas
    Gas = pins.analog_read_pin(AnalogPin.P0)
    if Gas - base <= 0:
        Gas = 0
    if Gas == 0:
        basic.show_icon(IconNames.HAPPY)
    else:
        music.play_tone(554, music.beat(BeatFraction.DOUBLE))
        #basic.show_number(Gas)
        basic.show_icon(IconNames.SAD)
basic.forever(on_forever)
def on_button_pressed_a():
    global base, Gas
    Gas = pins.analog_read_pin(AnalogPin.P0)
    base = Gas+2
input.on_button_pressed(Button.A, on_button_pressed_a)