from board import LIGHT, NEOPIXEL
from neopixel import NeoPixel
from analogio import AnalogIn

from time import sleep
from random import randint, randrange, random

from audio_file_player import AudioFilePlayer


# parameters

# activate, once light sensor reading is above this
dawn_threshold = 150

# filename of the wav file to play
audio_file_name = "fanfare.wav"


# setup

pixels = NeoPixel(NEOPIXEL, 10, brightness=.05, auto_write=False)
pixels.fill((0, 0, 0))
pixels.show()

light_sensor = AnalogIn(LIGHT)


audio_player = AudioFilePlayer(audio_file_name)


def _random_color(probability_to_get_primary_colors=0.5):
    if random() > probability_to_get_primary_colors:
        return (randint(0, 255), randint(0, 255), randint(0, 255))
    else:
        color = [0, 0, 0]
        channel_to_set = randrange(3)
        color[channel_to_set] = randint(0, 255)
        return tuple(color)


def surprise():
    print("surprise")
    for pixel in range(10):
        pixels[pixel] = _random_color(1)
    pixels.show()
    audio_player.play()
    while True:
        pixel_no = randrange(10)
        color = _random_color()
        pixels[pixel_no] = color
        pixels.show()
        sleep(0.02)


def stop_surprise():
    audio_player.stop()
    for pixel in range(10):
        pixels[pixel] = (0, 0, 0)
    pixels.show()


def is_surprise_appropriate():
    return light_sensor.value > dawn_threshold


if __name__ == "__main__":

    while True:
        print("Waiting...")

        if is_surprise_appropriate():
            surprise()

        sleep(0.5)
