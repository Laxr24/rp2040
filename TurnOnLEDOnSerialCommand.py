# Control on-board NeoPixel LED via Serial Commands ('on' / 'off')

import machine
import neopixel

# GPIO pin connected to the NeoPixel LED (e.g., GP16 on RP2040-Zero)
pixel_pin = 16
pixel = neopixel.NeoPixel(machine.Pin(pixel_pin), 1)

# Color configurations (RGB)
color_val = (20, 30, 20)     # LED ON color (G, R, B or R, G, B depending on LED type)
off_color_val = (0, 0, 0)    # LED OFF color

# Set default LED state to OFF
pixel[0] = off_color_val
pixel.write()

print("RP2040 Serial LED Controller Ready.")
print("Send 'on' to light up LED, 'off' to turn it off.")

while True:
    try:
        # Read command line from serial input (USB CDC / REPL)
        command = input().strip().lower()
        
        if not command:
            continue
        
        if command == "on":
            pixel[0] = color_val
            pixel.write()
            print("LED turned ON")
        elif command == "off":
            pixel[0] = off_color_val
            pixel.write()
            print("LED turned OFF")
        else:
            print(f"Unknown command: '{command}'. Please send 'on' or 'off'.")
            
    except KeyboardInterrupt:
        print("\nProgram stopped.")
        break
