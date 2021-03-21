import player
import lightController
from time import sleep


lc = lightController.constructLedController()
player.leds = lc

player.playSong(player.loadSong('songs/twinkle.json'))
