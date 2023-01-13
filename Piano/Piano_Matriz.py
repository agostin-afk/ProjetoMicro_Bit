# Piano_Matriz
tecla_0 = 0
tecla_1 = 0
tecla_2 = 0


def on_forever():
    global tecla_0, tecla_1, tecla_2
    tecla_0 = pins.digital_read_pin(DigitalPin.P4)
    tecla_1 = pins.digital_read_pin(DigitalPin.P1)
    tecla_2 = pins.digital_read_pin(DigitalPin.P2)
    if tecla_0 and (not (tecla_1) and not (tecla_2)):
        music.set_tempo(120)
        music.play_tone(264, music.beat(BeatFraction.HALF))
    if tecla_1 and (not (tecla_0) and not (tecla_2)):
        music.set_tempo(120)
        music.play_tone(297, music.beat(BeatFraction.HALF))
    if tecla_2 and (not (tecla_0) and not (tecla_1)):
        music.set_tempo(120)
        music.play_tone(330, music.beat(BeatFraction.HALF))
    if not (tecla_2) and (tecla_0 and tecla_1):
        music.set_tempo(120)
        music.play_tone(352, music.beat(BeatFraction.HALF))
    if not (tecla_0) and (tecla_1 and tecla_2):
        music.set_tempo(120)
        music.play_tone(396, music.beat(BeatFraction.HALF))
    if not (tecla_1) and (tecla_0 and tecla_2):
        music.set_tempo(120)
        music.play_tone(440, music.beat(BeatFraction.HALF))
    if tecla_0 and (tecla_1 and tecla_2):
        music.set_tempo(120)
        music.play_tone(495, music.beat(BeatFraction.HALF))


basic.forever(on_forever)
