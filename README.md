# \# airsoft-bomb-prop

# 

# An airsoft bomb prop in the style of CS:GO plant and defuse, built with an ESP32-C6 and MicroPython. It is a prop only: lights, sounds and a timer. Nothing explodes or heats up.

# 

# \## How it plays

# 

# 1\. The LED is blue while the bomb waits. Press the button to arm it.

# 2\. The countdown starts. The light blinks, and the blinking speeds up as time runs out.

# 3\. Hold the button for 10 seconds to defuse. If you let go, the 10 seconds start over.

# 4\. If the timer reaches zero, the bomb "explodes" (solid red light).

# 5\. After 3 seconds the bomb resets and waits to be armed again.

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

# | defuse.py | Countdown plus hold-to-defuse |

# | game.py | Complete game: press to arm, countdown, defuse or explode, then reset |

# 

# \## How to run

# 

# Flash MicroPython to the board, then run a file from your computer:

# 

# &#x20;   py -3.13 -m mpremote connect COM14 run game.py

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

# \- \[x] Reset after win or lose

# \- \[ ] Buzzer beeps

# \- \[ ] Wiring picture and photos

# \- \[ ] Keypad or display

# \- \[ ] Siren and enclosure

# \- \[ ] Wire-cutting defuse (version 2)

