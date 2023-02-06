let pin01 = 0
let pin02 = 0
let pin00 = 0
function notas() {
    while (true) {
        basic.pause(0)
        pin00 = pins.digitalReadPin(DigitalPin.P0)
        pin01 = pins.digitalReadPin(DigitalPin.P1)
        pin02 = pins.digitalReadPin(DigitalPin.P2)
        if (pin00 && (!pin02 && !pin01)) {
            music.playTone(264, music.beat(BeatFraction.Half))
            //  Do
            notas()
        }
        
        if (!pin02 && (pin01 && !pin00)) {
            music.playTone(297, music.beat(BeatFraction.Half))
            //  Ré
            notas()
        }
        
        if (pin02 && (!pin01 && !pin00)) {
            music.playTone(330, music.beat(BeatFraction.Half))
            //  Mí
            notas()
        }
        
        if (!pin02 && (pin01 && pin00)) {
            music.playTone(352, music.beat(BeatFraction.Half))
            //  Fá
            notas()
        }
        
        if (pin01 && (pin02 && !pin00)) {
            music.playTone(396, music.beat(BeatFraction.Half))
            //  Sol
            notas()
        }
        
        if (pin02 && (pin00 && !pin01)) {
            music.playTone(440, music.beat(BeatFraction.Half))
            //  Lá
            notas()
        }
        
        if (pin01 && (pin02 && pin00)) {
            music.playTone(495, music.beat(BeatFraction.Half))
            //  Si
            notas()
        }
        
        music.playTone(0, music.beat(BeatFraction.Half))
    }
}

basic.forever(function on_forever() {
    
    pin01 = pins.digitalReadPin(DigitalPin.P1)
    pin02 = pins.digitalReadPin(DigitalPin.P2)
    pin00 = pins.digitalReadPin(DigitalPin.P0)
    if (input.buttonIsPressed(Button.AB)) {
        notas()
        music.playTone(0, music.beat(BeatFraction.Half))
    }
    
})
