# https://github.com/adafruit/Adafruit_CircuitPython_HCSR04
# https://learn.adafruit.com/jack-o-theremin/circuit-python-code

from time import sleep
from board import A4, A5
from adafruit_hcsr04 import HCSR04


sonar = HCSR04(
        trigger_pin=A5,
        echo_pin=A4,  # NOTE: NEEDS VOLTAGE DIVIDER
        )


def get_sonar_distance_cm():
    return sonar.distance


if __name__ == "__main__":
    while True:
        try:
            print(get_sonar_distance_cm())
        except RuntimeError:
            print("Retrying!")
        sleep(1)
