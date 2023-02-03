line0 = 0
line1 = 0
line2 = 0

def on_forever():
    global line0, line1, line2
    line0 = pins.digital_read_pin(DigitalPin.P2)
    line1 = pins.digital_read_pin(DigitalPin.P8)
    line2 = pins.digital_read_pin(DigitalPin.P1)
    if line0 or (line1 or line2):
        basic.pause(30)
        line0 = pins.digital_read_pin(DigitalPin.P2)
        line1 = pins.digital_read_pin(DigitalPin.P8)
        line2 = pins.digital_read_pin(DigitalPin.P1)
        if not (line2) and (not (line1) and line0):
            music.play_tone(262, music.beat(BeatFraction.HALF))
        if not (line2) and (line1 and not (line0)):
            music.play_tone(294, music.beat(BeatFraction.HALF))
        if not (line2) and (line1 and line0):
            music.play_tone(330, music.beat(BeatFraction.HALF))
        if line2 and (not (line1) and not (line0)):
            music.play_tone(349, music.beat(BeatFraction.HALF))
        if line2 and (not (line1) and line0):
            music.play_tone(392, music.beat(BeatFraction.HALF))
        if line2 and (line1 and not (line0)):
            music.play_tone(440, music.beat(BeatFraction.HALF))
        if line2 and (line1 and line0):
            music.play_tone(494, music.beat(BeatFraction.HALF))
basic.forever(on_forever)
on_forever()