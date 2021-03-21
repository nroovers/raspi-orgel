from gpiozero import LED
import noteUtils

def constructLedController():
    return LightController([
        LED(23),
        LED(24),
        LED(25),
        LED(12),
        LED(16),
        LED(20),
        LED(21)
    ])

def constructRelayController():
    return LightController([
        # LED(23),
        LED(24),
        LED(25),
        LED(12),
        LED(16),
        LED(20),
        LED(21)
    ])

class LightController(object):

    def __init__(self, lights):
        if type(lights) != list:
            raise TypeError('lights attribute is not a list')
        self.lights = lights

    def __iter__(self):
        self.i=0
        return self

    def __next__(self):    # Returns the next weekday
        if self.i == len(self.lights):
            raise StopIteration # Signal that all weekdays were already iterated over
        else:
            light = self.lights[self.i]
            self.i += 1
            return light

    def __getitem__(self, key):
        return self.lights[key]

    def __len__(self):
        return len(self.lights)

    def getNoteLight(self, note):
        notePosition = noteUtils.notes.index(note) * len(self.lights) // len(noteUtils.notes)
        return self.lights[notePosition]

    def allOn(self):
        for l in self.lights:
            l.on()

    def allOff(self):
        for l in self.lights:
            l.off()
    
    def toggleAll(self):
        for l in self.lights:
            l.toggle()