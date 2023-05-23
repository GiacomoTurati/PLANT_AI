# Python code
#
moisture = 0
x = 0
y = 0

def on_forever():
  global moisture
  global x
  global y
  pins.digital_write_pin(DigitalPin.P1, 1)
  basic.pause(10)
  moisture = Math.map(pins.analog_read_pin(AnalogPin.P2), 0, 813, 0, 100)
  pins.digital_write_pin(DigitalPin.P1, 0)
  if moisture < 50:
    x = randint(0, 4)
    y = 0
    for index in range(9):
      led.plot_brightness(x, y, 255)
      led.plot_brightness(x, (y - 1), 32)
      led.plot_brightness(x, (y - 2), 8)
      led.plot_brightness(x, (y - 3), 2)
      led.plot_brightness(x, (y - 4), 0)
      y += 1
      basic.pause(50)
  else:
    basic.pause(1000)
basic.forever(on_forever)
