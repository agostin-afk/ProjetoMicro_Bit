let Do = 264
let Re = 297
let Mi = 330
let Fa = 352
let Sol = 396
let La = 440
let Si = 495
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    input.onPinPressed(TouchPin.P0, function on_pin_pressed_p0() {
        music.playTone(Re, music.beat(BeatFraction.Whole))
    })
    input.onPinPressed(TouchPin.P1, function on_pin_pressed_p1() {
        music.playTone(Do, music.beat(BeatFraction.Whole))
    })
    input.onPinPressed(TouchPin.P2, function on_pin_pressed_p2() {
        music.playTone(Mi, music.beat(BeatFraction.Whole))
    })
})
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    input.onPinPressed(TouchPin.P1, function on_pin_pressed_p1() {
        music.playTone(Sol, music.beat(BeatFraction.Whole))
    })
    input.onPinPressed(TouchPin.P0, function on_pin_pressed_p0() {
        music.playTone(Fa, music.beat(BeatFraction.Whole))
    })
    input.onPinPressed(TouchPin.P2, function on_pin_pressed_p2() {
        music.playTone(La, music.beat(BeatFraction.Whole))
    })
})
