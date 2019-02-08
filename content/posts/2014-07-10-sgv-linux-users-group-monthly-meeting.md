Title: Raspberry Pi Retro Camera
Date: 2014-07-09 12:48
event_date: 2014-07-10 19:00
event_location: Burger Continental, 535 S Lake Ave, Pasadena, CA, 91101
event_updated: 1404935279000

James McDuffie gave a presentation on his Raspberry Pi Camera project. He has hollowed out a film camera and put in a Raspberry Pi, camera, and some other electronics to make a retro-looking camera that actually takes digital photos -and- allows ssh access.

He had close-up pictures of the electronic components and detailed explanations of why he chose a particular component, why he modified it, and how it fit into the project. James' particular focus was on energy efficiency, so he went through a lot of trouble to modify the board to use 3.3v power from a cellphone battery.  He also looked for low-power components and ways to save power.  Because there is no leds or lcd, he used beeps to provide feedback from the camera during operation.  He also has a six-position knob that allows him to do things like turn on the system, turn off the camera portion, or to send the halt command to the Raspberry Pi.  There is room for more features.

He has set up a webserver on the Raspberry Pi using nginx and Flask.  This allows access to the photos on the Pi.  Aside from a serial connection and the controls from the camera, the only way to "talk" to the Raspberry Pi is through the webserver or ssh.  The Raspberry Pi is set up to automatically connect to known networks in the wpa supplicants file.  The actual camera operation is handled through a Python library called [picamera](https://picamera.readthedocs.org/en/release-1.5/).
