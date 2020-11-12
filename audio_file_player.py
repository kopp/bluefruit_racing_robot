from board import SPEAKER, SPEAKER_ENABLE
from audiocore import WaveFile
from audiopwmio import PWMAudioOut as AudioOut
from digitalio import DigitalInOut


class AudioFilePlayer:
    def __init__(self, filename):
        self.filename = filename
        self.wave = None
        self.audio = None
        # speaker needs to be enabled by pin
        speaker_enable = DigitalInOut(SPEAKER_ENABLE)
        speaker_enable.switch_to_output(value=True)

    def play(self):
        if self.wave is None:
            wave_file = open(self.filename, "rb")
            self.wave = WaveFile(wave_file)
        if self.audio is None:
            self.audio = AudioOut(SPEAKER)
        self.audio.play(self.wave, loop=True)

    def stop(self):
        if self.audio is not None:
            self.audio.stop()
