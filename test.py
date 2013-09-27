from motorfuncs import *
from sensorfuncs import *

# speed(x):
"""set the speed of both motors together.
0 == off - 100 == full"""

# stop():
"""Stops your robot should you need it to"""

# end():
"""Stops the robot and cleans up the GPIO pins - use to finish your program"""

# go_forward(x, y): 
"""Move the robot forward at x speed (0-100) for y seconds"""

# go_back(x, y): 
"""Move the robot forward at x (0-100) speed for y seconds"""

# spin_right(x):
"""Turns robot by number of degrees (from original facing direction)
in a range between 0 and 360 degrees to the right"""

# spin_left(x):
"""Turns robot by number of degrees (from original facing direction)
in a range between 0 and 360 degrees to the left"""

# turn_right(x, y): 
"""Gradually turn your robot right, where x (0 == sharp turn to 100 == no turn) 
relates to sharpness and y is the time the robot will continue to turn"""

# turn_left(x, y):
"""Gradually turn your robot right, where x (0 == sharp turn to 100 == no turn) 
relates to sharpness and y is the time the robot will continue to turn"""

def high_react():
    reading = read_sensors()
    if reading[0] > high_trigger:
        print "Left HIGH sensor warning!" 
    elif reading[1] > (high_trigger):
        print "Front HIGH sensor warning!"
        if reading[0] < reading[2]: #if left reading is smaller than right reading...
            print "Turning left"
        else:
            print "Turning right"
        if readadc(3) > high_trigger:
            new_reading = read_sensors()
            if new_reading[0] < new_reading[2]:
                print "Spinning left"
            else:
                print "Spinning right"
    elif reading[2] > high_trigger:
        print "Right HIGH sensor warning!"
    elif reading[3] > high_trigger:
        print "Rear HIGH sensor warning!"

def low_react():
    reading = read_sensors()
    if reading[0] > low_trigger + 10:
        old_L_reading = reading[0]
        print "Left LOW sensor warning!" 
        print "Turning right a bit"
        if readadc(0) > old_L_reading:
            print "Turning right a bit more"
    elif reading[1] > (low_trigger):
        print "Front LOW sensor warning!"
        if reading[0] < reading[2]: #if left reading is smaller than right reading...
            print "Turning left a bit"
        else:
            print "Turning right a bit"
    elif reading[2] > low_trigger:
        old_R_reading = reading[0]
        print "Left LOW sensor warning!" 
        print "Turning left a bit"
        if readadc(2) > old_R_reading:
            print "Turning left a bit more"
    elif reading[3] > low_trigger:
        print "Rear LOW sensor warning!"

def main():
    try:
        while True:
            #your code goes here
            low_react()
            high_react()
            reading = read_sensors()
            print "left:", reading[0], " | front:", reading[1], " | right:", reading[2], " | rear:", reading[3]
            sleep(.1)
    except KeyboardInterrupt:
        end()
        print "GPIO cleaned"

if __name__ == '__main__':
    main()