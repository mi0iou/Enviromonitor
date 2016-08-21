from sense_hat import SenseHat
sense = SenseHat()

# Set rotation of text
sense.set_rotation(180)

# Define colours
red = (255, 0, 0)
blue = (0, 255, 0)
green = (0, 0, 255)
yellow = (255, 255, 0)
magenta = (255, 0, 255)
cyan = (0, 255, 255)
white = (255, 255, 255)

# create colour array
colour = [red, blue, green, yellow, magenta, cyan, white]

# Initialize index to 0
n = 0

#Main Loop
while True:

    # increment index if there has been a joystick event
    if sense.stick.get_events():
        n = n + 1
        if n > 6:
            n = 0

    # get temperature and display on LED array
    temperature = sense.get_temperature()
    sense.show_message ("%.1fC" % temperature, text_colour = colour[n])

    # increment index if there has been a joystick event
    if sense.stick.get_events():
        n = n + 1
        if n > 6:
            n = 0

    # get humidity and display on LED array
    humidity = sense.get_humidity()
    sense.show_message ("%d%%RH" % humidity, text_colour = colour[n])

    # increment index if there has been a joystick event
    if sense.stick.get_events():
        n = n + 1
        if n > 6:
            n = 0

    # get pressure and display on LED array
    pressure = sense.get_pressure()
    sense.show_message ("%dmBar" % pressure, text_colour = colour[n])
