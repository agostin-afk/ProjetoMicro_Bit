pin01 = 0
pin02 = 0
pin08 = 0
def notas():
    while True:
        basic.pause(0)
        pin01 = pins.digital_read_pin(DigitalPin.P1)
        pin02 = pins.digital_read_pin(DigitalPin.P2)
        pin08 = pins.digital_read_pin(DigitalPin.P0)
        if not (pin01) and (not (pin02) and pin08):
            music.play_tone(262, music.beat(BeatFraction.HALF))
            notas()
        if not (pin01) and (pin02 and not (pin08)):
            music.play_tone(294, music.beat(BeatFraction.HALF))
            notas()
        if not (pin01) and (pin02 and pin08):
            music.play_tone(330, music.beat(BeatFraction.HALF))
            notas()
        if pin01 and (not (pin02) and not (pin08)):
            music.play_tone(349, music.beat(BeatFraction.HALF))
            notas()
        if pin01 and (not (pin02) and pin08):
            music.play_tone(392, music.beat(BeatFraction.HALF))
            notas()
        if pin01 and (pin02 and not (pin08)):
            music.play_tone(440, music.beat(BeatFraction.HALF))
            notas()
        if pin01 and (pin02 and pin08):
            music.play_tone(494, music.beat(BeatFraction.HALF))
            notas()
        music.play_tone(0, music.beat(BeatFraction.HALF))
def on_forever():
    global pin01, pin02, pin08
    pin01 = pins.digital_read_pin(DigitalPin.P1)
    pin02 = pins.digital_read_pin(DigitalPin.P2)
    pin08 = pins.digital_read_pin(DigitalPin.P0)
    if input.button_is_pressed(Button.AB):
        notas()
        music.play_tone(0, music.beat(BeatFraction.HALF))
basic.forever(on_forever)