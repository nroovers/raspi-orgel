import math  # import needed modules


# Sound Generation — python
# https://medium.com/py-bits/sound-generation-python-904e54f5398d
def sinWave(bitrate=44100, freq=440, length=1):
    # bitrate = 44100  # number of frames per second/frameset
    # freq = 261.63  # Hz, waves per second
    # length = 1  # seconds to play sound

    if freq > bitrate:
        bitrate = freq+100
    numberOfFrames = int(bitrate * length)
    restFrames = numberOfFrames % bitrate
    waveData = ''

    # generating waves
    for x in range(numberOfFrames):
        waveData = waveData + \
            chr(int(math.sin(x/((bitrate/freq)/math.pi))*127+128))

    for x in range(restFrames):
        waveData = waveData+chr(128)

    return waveData



# add delay
# http://andrewslotnick.com/posts/audio-delay-with-python.html
