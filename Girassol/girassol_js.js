let angulo = 0
basic.forever(function on_forever() {
    
    angulo = input.lightLevel()
    servos.P0.setAngle(angulo - 70)
})