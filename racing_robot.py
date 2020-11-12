from adafruit_motor import servo
from pulseio import PWMOut
from board import A1, A3
from time import sleep, monotonic
from random import random, choice

from ultrasonic import get_sonar_distance_cm
from surprise_on_dawn import is_surprise_appropriate, surprise


MIN_FREE_SPACE_AHEAD_CM = 30
MAX_SPEED = 0.5


rotate_duration_for_turnaround_s = 1.4

pwm_left_wheel = PWMOut(A1, frequency=50)
pwm_right_wheel = PWMOut(A3, frequency=50)

left_wheel = servo.ContinuousServo(pwm_left_wheel)
right_wheel = servo.ContinuousServo(pwm_right_wheel)


def _debug(msg):
    # print(msg)
    pass


def is_sufficient_free_space():
    freespace_cm = get_sonar_distance_cm()
    # freespace_cm = MIN_FREE_SPACE_AHEAD_CM + 1  # fake sonar
    sufficient = freespace_cm > MIN_FREE_SPACE_AHEAD_CM
    _debug("Freespace: {}cm ({}sufficient)".format(
        freespace_cm,
        "" if sufficient else "NOT ",
        ))
    return sufficient


def stop():
    left_wheel.throttle = 0
    right_wheel.throttle = 0


def straight():
    left_wheel.throttle = MAX_SPEED
    right_wheel.throttle = -MAX_SPEED


def rotate(direction: str):
    if direction == "left":
        throttle_delta = -MAX_SPEED
    elif direction == "right":
        throttle_delta = +MAX_SPEED
    else:
        stop()
    left_wheel.throttle = throttle_delta
    right_wheel.throttle = throttle_delta


def turn_around_and(command):
    """
    Turn the robot around about 180 degrees, then execute the given command.
    Use this like e.g. `turn_around_and(straight)`.
    """
    rorate("left")
    sleep(rotate_duration_for_turnaround_s)
    command()


def wait_while_free_for(duration_s):
    """
    Return when either the freespace ahead is not sufficient or the time has
    elapsed.
    """
    straight_begin_timestamp = monotonic()
    time_elapsed_s = 0
    while True:
        if not is_sufficient_free_space():
            print("obstacle ahead, abort straight after {}s".format(time_elapsed_s))
            return
        time_elapsed_s = monotonic() - straight_begin_timestamp
        _debug("currently elapsed: {}s".format(time_elapsed_s))
        if time_elapsed_s > duration_s:
            _debug("time ran out: {}s elapsed (more than {}s)".format(
                time_elapsed_s, duration_s))
            return


def random_swim_and_tumble_movement(
        straight_max_duration_s=3,
        rotate_max_duration_s=2,
        maximal_number_of_loops=None):
    """
    This is a simple model for the movement of bacteria or flying insects:
    Rotate randomly, then run straight for some time, then rotate, then run
    straight again etc.
    If something is in front of you
    """
    if maximal_number_of_loops is None:
        maximal_number_of_loops = float('inf')
    loop_count = 0
    while loop_count < maximal_number_of_loops:
        loop_count += 1
        if is_surprise_appropriate():
            stop()
            surprise()

        straight_duration_s = random() * straight_max_duration_s
        rotate_duration_s = random() * rotate_max_duration_s
        rotation_diretion = choice(["left", "right"])
        print("turn {:.4}s {} then {:.4}s straight".format(rotate_duration_s, rotation_diretion, straight_duration_s))

        rotate(rotation_diretion)
        sleep(rotate_duration_s)

        straight()
        wait_while_free_for(straight_duration_s)


if __name__ == "__main__":
    print("waiting...")
    sleep(15)
    print("go!")
    random_swim_and_tumble_movement()
