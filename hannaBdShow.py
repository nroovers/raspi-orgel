import sys
import player
import lightController
import audioController
import noteUtils
from time import sleep


lc = lightController.constructLedController()
ac = audioController.AudioController()
player.leds = lc


def test():
    print('test')
    lc.allOn()
    ac.open()
    while True:
        ac.playNote('A3',5,1)


def countDown():
    print('count down')
    lc.allOn()
    for i in range(len(lc)):
        sleep(1)
        lc[i].off()
    sleep(1)

def play():
    print('Play happy birthday')
    player.playSong(player.loadSong('songs/bday.json'))


def lighShow():
    print('Ligth show')
    lc.allOff()

    # toggle lights on off
    for i in range(3):
        lc.allOn()
        sleep(0.5)
        lc.allOff()
        sleep(0.5)

    # lights left to right and back
    for i in range(2):
        for i in range(len(lc)):
            lc[i].toggle()
            sleep(0.1)
        for i in range(len(lc)):
            lc[i].toggle()
            sleep(0.1)
        for i in range(len(lc)):
            lc[len(lc)-i-1].toggle()
            sleep(0.1)
        for i in range(len(lc)):
            lc[len(lc)-i-1].toggle()
            sleep(0.1)

    # firework lights
    for x in range(12):
        half = int(len(lc)/2)
        if len(lc) % 2 == 1:
            lc[half].toggle()
            sleep(0.1)
        for i in range(half):
            j = half-i
            lc[j-1].toggle()
            lc[half+i+len(lc) % 2].toggle()
            sleep(0.1)




def main(argv):
    if len(argv) > 0  and argv[0] == '-t':
        test()
    else:
        lc.allOn()
        input('press key to start countdown')
        countDown()
        play()
        lighShow()

if __name__ == "__main__":
   main(sys.argv[1:])
