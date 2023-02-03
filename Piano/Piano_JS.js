let pin01 = 0
let pin02 = 0
let pin08 = 0
function notas() {
    while (true) {
        basic.pause(0)
        pin01 = pins.digitalReadPin(DigitalPin.P1)
        pin02 = pins.digitalReadPin(DigitalPin.P2)
        pin08 = pins.digitalReadPin(DigitalPin.P0)
        if (!pin01 && (!pin02 && pin08)) {
            music.playTone(262, music.beat(BeatFraction.Half))
            notas()
        }
        
        if (!pin01 && (pin02 && !pin08)) {
            music.playTone(294, music.beat(BeatFraction.Half))
            notas()
        }
        
        if (!pin01 && (pin02 && pin08)) {
            music.playTone(330, music.beat(BeatFraction.Half))
            notas()
        }
        
        if (pin01 && (!pin02 && !pin08)) {
            music.playTone(349, music.beat(BeatFraction.Half))
            notas()
        }
        
        if (pin01 && (!pin02 && pin08)) {
            music.playTone(392, music.beat(BeatFraction.Half))
            notas()
        }
        
        if (pin01 && (pin02 && !pin08)) {
            music.playTone(440, music.beat(BeatFraction.Half))
            notas()
        }
        
        if (pin01 && (pin02 && pin08)) {
            music.playTone(494, music.beat(BeatFraction.Half))
            notas()
        }
        
        music.playTone(0, music.beat(BeatFraction.Half))
    }
}

basic.forever(function on_forever() {
    
    pin01 = pins.digitalReadPin(DigitalPin.P1)
    pin02 = pins.digitalReadPin(DigitalPin.P2)
    pin08 = pins.digitalReadPin(DigitalPin.P0)
    if (input.buttonIsPressed(Button.AB)) {
        notas()
        music.playTone(0, music.beat(BeatFraction.Half))
    }
    
})
