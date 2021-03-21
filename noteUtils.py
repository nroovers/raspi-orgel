# Code based on
# https://gist.github.com/stuartmemo/3766449

# Takes string of Note + Octave
# Example:
# var frequency = getFrequency('C3');

notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']

def getNotes():
    return notes

def getFrequency(note):
    # print('getFrequency', note)
    octave = 0
    keyNumber = 0

    octave = int(note[-1:])
    keyNumber = int(notes.index(note[0: -1]))

    if keyNumber < 3:
        kn = keyNumber + 12 + ((octave - 1) * 12) + 1
    else:
        kn = keyNumber + ((octave - 1) * 12) + 1

    return 440 * 2**((kn - 49) / 12)


if __name__ == 'main':
    print(getFrequency('C4'))
    print(getFrequency('D4'))
    print(getFrequency('E4'))
    print(getFrequency('F4'))
    print(getFrequency('G4'))
    print(getFrequency('A4'))
    print(getFrequency('B4'))
