# General Tips

- Make sure to never accidentally touch any of the contacts on the board with
  one of the cables attached to a pin.
  This may destroy the complete board.
  If you want to leave the wires on the Bluefruit, use one of the cut female
  cables to sheath the cables' outer contacts or plug them into an unused place
  in the Breadboard.
- Prototype with the REPL!
- Keep the terminal open when loading new code to see the exceptions :)
- Use `Ctrl-E` in the REPL to start a "paste" session.
  Paste your code and hit `Ctrl-D` and your code will get executed.
- Use Bluethooth Low Energy together with the Adafruit Bluetooth LE Connect App
  to log what your robot is doing while it is running around.
  See the instructions
  [here](https://learn.adafruit.com/circuitpython-nrf52840)
  to get started.


# Notes on the additional hardware

- You can leave the battery pack plugged in while connecting to USB -- this
  allows you to rapidly prototype code in python, unplug and test, go back to
  coding, because the device does not power off (and your session is lost).
- The display has an SSD1306 chip with I2C and runs with 3.3V directly.
  See
  [here](https://learn.adafruit.com/micropython-hardware-ssd1306-oled-display/circuitpython)
  for how to get it running with CircuitPython.
- Build your own "Lidar" from the Ultrasonic mounted on the Servo.
  Note, that this servo does not rotate continuously, but rather you control
  the angle.
  See
  [here](https://learn.adafruit.com/circuitpython-essentials/circuitpython-servo)
  for how wo use it -- it's under the headline "Standard Servo" (while the
  other servos with wheels are "Continuous Servos").
- For the DC Motor, see
  [these instructions](https://tutorial45.com/arduino-projects-arduino-dc-motor-control/)
  (instead of a 47 kOhm resistor, use 2 times 100 kOhm (brown black black
  orange brown) in parallel.
- Use the small thing labeled "DC-DC XL6009E1" on the back to get a higher
  voltage than the battery normally provides.
  On the front, there is a small screw -- using that, you can regulate the
  voltage.
  This can be useful to e.g. drive motors faster.
