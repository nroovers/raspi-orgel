import pyaudio
import noteUtils
import sound


class AudioController(object):

    channels = 2
    rate = 44100

    def __init__(self):
        self.p = pyaudio.PyAudio()

    def open(self):
        self.stream = self.p.open(format=self.p.get_format_from_width(1),
                                  # format=pyaudio.paUInt8,
                                  # frames_per_buffer=4096,
                                  channels=AudioController.channels,
                                  rate=AudioController.rate,
                                  output=True)

    def playNote(self, note, length, tempo):
        self.playFreq(noteUtils.getFrequency(note),
                      length,
                      tempo)

    def playFreq(self, freq, length, tempo):
        # print('play note', note)
        if(self.stream.is_stopped()):
            self.stream.start_stream()
        self.stream.write(
            sound.sinWave(AudioController.rate,
                          freq,
                          length*tempo))
        self.stream.stop_stream()

    def close(self):
        self.stream.close()

    def __del__(self):
        self.p.terminate()
