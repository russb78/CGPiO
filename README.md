#CGPiO
Copyright 2013 Russell Barnes <russell@russellbarnes.co.uk>

###CGPiO is a Raspberry Pi robot I've built from the frindo.org robot platform.
This is all pretty new to me, so if you've got any tips/advice drop me a line!

#########################

THEORY:
Wheel diameter: 42mm
Wheel circumference: (42*3.14) = 131.88mm (13.19cm per revolution).
Motor RPM (50:1 micro motor @6v) = 250rpm
4.16 revolutions per second = 54.87cm per second - approx 1 meter every 2 seconds. 

PRACTICAL:
CGPiO weighs 800g so travels 35cm per second on 4 fresh AA batteries.
That's 1 meter every 2.86 seconds.

#########################

#Simple, functional control
##sensorfuncs.py will expand to include other sensors beyond 4 Sharp SY0A21's.

##Motorfuncs.py holds all the main motor controls with the following functions:

speed(x):
set the speed of both motors together.
0 == off - 100 == full"""

stop():
Stops your robot should you need it to

end():
Stops the robot and cleans up the GPIO pins - use to finish your program

go_forward(x, y): 
Move the robot forward at x speed (0-100) for y seconds

go_back(x, y): 
Move the robot forward at x (0-100) speed for y seconds

spin_right(x):
Turns robot by number of degrees (from original facing direction)
in a range between 0 and 360 degrees to the right

spin_left(x):
Turns robot by number of degrees (from original facing direction)
in a range between 0 and 360 degrees to the left

turn_right(x, y): 
Gradually turn your robot right, where x (0 == sharp turn to 100 == no turn) 
relates to sharpness and y is the time the robot will continue to turn

turn_left(x, y):
Gradually turn your robot right, where x (0 == sharp turn to 100 == no turn) 
relates to sharpness and y is the time the robot will continue to turn

#Next steps:
* Measure at various motor speeds to produce accurate turning circles at any speed
* Alter movement functions to allow for travel distance in meters
* Map sensor readings to turns/spins to create more intelligent behaviour
* 'lock onto' and 'track' functions (for mapping and swarming)

#License
This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
MA 02110-1301, USA.
