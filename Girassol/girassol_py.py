angulo = 0

def on_forever():
    global angulo
    angulo = input.light_level()
    servos.P0.set_angle(angulo-70)
basic.forever(on_forever)