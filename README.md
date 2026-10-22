# \# airsoft-bomb-prop

# 

# An airsoft bomb prop in the style of CS:GO plant and defuse, built with an ESP32-C6 and MicroPython. It is a prop only: lights, sounds and a timer. Nothing explodes or heats up.

# 

# \## How it plays

# 

# 1\. The bomb is armed and the countdown starts.

# 2\. The light blinks, and the blinking speeds up as time runs out.

# 3\. Hold the button for 10 seconds to defuse. If you let go, the 10 seconds start over.

# 4\. If the timer reaches zero, the bomb "explodes" (solid red light).

# 

# \## Hardware

# 

# \- ESP32-C6 dev board (ESP32-C6-WROOM-1)

# \- On-board RGB LED (GPIO 8)

# \- On-board BOOT button (GPIO 9)

# \- Buzzer and external button: planned

# 

# \## Files

# 

# | File | What it does |

# | --- | --- |

# | blink.py | Blinks the on-board LED |

# | button\_led.py | LED turns green while the button is held |

# | countdown.py | LED blinks faster and faster, then explodes |

# | defuse.py | Full game loop: countdown plus hold-to-defuse |

# 

# \## How to run

# 

# Flash MicroPython to the board, then run a file from your computer:

# 

# &#x20;   py -3.13 -m mpremote connect COM14 run defuse.py

# 

# Change COM14 to the port your board uses.

# 

# \## Progress

# 

# \- \[x] Set up Git, Python, MicroPython

# \- \[x] Blink the LED

# \- \[x] Button input

# \- \[x] Countdown with blinking that speeds up

# \- \[x] Hold-to-defuse game loop

# \- \[ ] Buzzer beeps

# \- \[ ] Wiring picture and photos

# \- \[ ] Keypad or display

# \- \[ ] Siren, reset, enclosure

# \- \[ ] Wire-cutting defuse (version 2)

