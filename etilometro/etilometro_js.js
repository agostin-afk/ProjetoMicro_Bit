let Gas = 0
let base = 770
/** def on_forever():
    Gas = pins.analog_read_pin(AnalogPin.P0)
    basic.show_number(Gas)
basic.forever(on_forever)

 */
basic.forever(function on_forever() {
    
    Gas = pins.analogReadPin(AnalogPin.P0)
    if (Gas - base <= 0) {
        Gas = 0
    }
    
    if (Gas == 0) {
        basic.showIcon(IconNames.Happy)
    } else {
        music.playTone(554, music.beat(BeatFraction.Double))
        // basic.show_number(Gas)
        basic.showIcon(IconNames.Sad)
    }
    
})
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    Gas = pins.analogReadPin(AnalogPin.P0)
    base = Gas + 2
})
