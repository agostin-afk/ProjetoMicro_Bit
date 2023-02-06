pin01 = 0
pin02 = 0
pin00 = 0
def notas():
    while True:
        basic.pause(0)
        pin00 = pins.digital_read_pin(DigitalPin.P0)
        pin01 = pins.digital_read_pin(DigitalPin.P1)
        pin02 = pins.digital_read_pin(DigitalPin.P2)
        if (pin00) and (not (pin02) and  not (pin01)):
            music.play_tone(264, music.beat(BeatFraction.HALF))
            # Do
            notas()
        if not (pin02) and (pin01 and not (pin00)):
            music.play_tone(297, music.beat(BeatFraction.HALF))
            # Ré
            notas()
        if pin02 and (not (pin01) and not (pin00)):
            music.play_tone(330, music.beat(BeatFraction.HALF))
            # Mí
            notas()
        if not (pin02) and (pin01 and pin00):
            music.play_tone(352, music.beat(BeatFraction.HALF))
            # Fá
            notas()
        if pin01 and ((pin02) and not (pin00)):
            music.play_tone(396, music.beat(BeatFraction.HALF))
            # Sol
            notas()
        if pin02 and (pin00 and not (pin01)):
            music.play_tone(440, music.beat(BeatFraction.HALF))
            # Lá
            notas()
        if pin01 and (pin02 and pin00):
            music.play_tone(495, music.beat(BeatFraction.HALF))
            # Si
            notas()
        music.play_tone(0, music.beat(BeatFraction.HALF))

def on_forever():
    global pin01, pin02, pin00
    pin01 = pins.digital_read_pin(DigitalPin.P1)
    pin02 = pins.digital_read_pin(DigitalPin.P2)
    pin00 = pins.digital_read_pin(DigitalPin.P0)
    if input.button_is_pressed(Button.AB):
        notas()
        music.play_tone(0, music.beat(BeatFraction.HALF))
basic.forever(on_forever)
