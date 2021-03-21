import song
import lightController
import audioController


# leds = lightController.constructLedController()
# audio = audioController.AudioController()

leds = lightController.LightController([])
audio = audioController.AudioController()


def loadSong(songLocation):
    return song.openSong(songLocation)


def playNote(note, length, tempo):
    print('play note:', note)
    leds.getNoteLight(note[0:-1]).on()
    audio.playNote(note, length, tempo)
    leds.getNoteLight(note[0:-1]).off()


def playSong(s):
    audio.open()
    for note in song.getNotes(s):
        playNote(note[0],
                 note[1],
                 song.getTempo(s))
    audio.close()
    # p.terminate()


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
