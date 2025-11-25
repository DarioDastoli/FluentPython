#Example 2-9. Method from an imaginary Robot class

def handle_message(self, message):
    match message:
        case ['BEEPER', frequency, times]:
            self.beep(times, frequency)
        case ['NECK', angle]:
            self.rotate_neck(angle)
        case['LED', ident, intensity]:
            self.leds[ident].set_brightness(ident, intensity)
        case['LED',ident, red, green, blue]:
            self.leds[ident].set_color(red, green, blue)
        case _ :
            raise InvalidCommand(message)
