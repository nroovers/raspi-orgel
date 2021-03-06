from gpiozero import LED
# from gpiozero import TonalBuzzer
from gpiozero.tones import Tone

import pyaudio
# import simpleaudio as sa # other option instead of PyAudio

from time import sleep

import noteUtils
import sound
import song


def loadSong(songLocation):
    return song.openSong(songLocation)


def initLEDs():
    leds = {}
    leds['C'] = LED(23)
    leds['D'] = LED(24)
    leds['E'] = LED(25)
    leds['F'] = LED(12)
    leds['G'] = LED(16)
    leds['A'] = LED(20)
    leds['B'] = LED(21)
    return leds


def playNote(stream, leds, note, tempo):
    n=note[0]
    leds[n[0:1]].on()
    print('play note', note)
    if(stream.is_stopped()):
        stream.start_stream()
    stream.write(
        sound.sinWave(44100,
                      noteUtils.getFrequency(n),
                      note[1]*tempo))
    stream.stop_stream()
    leds[n[0:1]].off()
    # sleep(0.01)


def playSong(s):
    p = pyaudio.PyAudio()
    leds = initLEDs()
    stream = p.open(format=p.get_format_from_width(1),
                    # format=pyaudio.paUInt8,
                    # frames_per_buffer=4096,
                    channels=2, 
                    rate=44100, 
                    output=True)
    for note in song.getNotes(s):
        playNote(stream,
                 leds,
                 note,
                 song.getTempo(s))
    stream.close()
    p.terminate()


# for i in range(p.get_device_count()):
#     device = p.get_device_info_by_index(i)
#     if device['maxOutputChannels'] == 2:
#         print(p.get_device_info_by_index(i))
#         print()
#         # stream = p.open(format=p.get_format_from_width(
#         #     1), channels=2, rate=BITRATE, output=True, output_device_index=device['index'])
#         stream = p.open(format=p.get_format_from_width(
#             1), channels=2, rate=int(device['defaultSampleRate']), output=True, output_device_index=device['index'])
#         stream.write(genSound(int(device['defaultSampleRate']), 261.63, 1))
#         stream.stop_stream()
#         stream.close()

#         sleep(2)
