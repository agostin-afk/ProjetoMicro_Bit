Do = 264
Re = 297
Mi = 330
Fa = 352
Sol = 396
La = 440
Si =495
def on_button_pressed_b():
    def on_pin_pressed_p0():
        music.play_tone(Re, music.beat(BeatFraction.WHOLE))
    input.on_pin_pressed(TouchPin.P0, on_pin_pressed_p0)

    def on_pin_pressed_p1():
        music.play_tone(Do, music.beat(BeatFraction.WHOLE))
    input.on_pin_pressed(TouchPin.P1, on_pin_pressed_p1)

    def on_pin_pressed_p2():
        music.play_tone(Mi, music.beat(BeatFraction.WHOLE))
    input.on_pin_pressed(TouchPin.P2, on_pin_pressed_p2)
input.on_button_pressed(Button.B, on_button_pressed_b)
def on_button_pressed_a():
    def on_pin_pressed_p1():
        music.play_tone(Sol, music.beat(BeatFraction.WHOLE))
    input.on_pin_pressed(TouchPin.P1, on_pin_pressed_p1)

    def on_pin_pressed_p0():
        music.play_tone(Fa, music.beat(BeatFraction.WHOLE))
    input.on_pin_pressed(TouchPin.P0, on_pin_pressed_p0)

    def on_pin_pressed_p2():
        music.play_tone(La, music.beat(BeatFraction.WHOLE))
    input.on_pin_pressed(TouchPin.P2, on_pin_pressed_p2)
input.on_button_pressed(Button.A, on_button_pressed_a)