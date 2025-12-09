import time

# Path to the onboard LED brightness file
LED_BRIGHTNESS_PATH = "/sys/class/leds/led0/brightness"

print("Testing onboard LED. Press Ctrl+C to stop.")

try:
    while True:
        # Turn LED on
        with open(LED_BRIGHTNESS_PATH, "w") as led_file:
            led_file.write("1")
        time.sleep(1)  # Wait for 1 second

        # Turn LED off
        with open(LED_BRIGHTNESS_PATH, "w") as led_file:
            led_file.write("0")
        time.sleep(1)  # Wait for 1 second
except KeyboardInterrupt:
    print("\nTest stopped by user.")
finally:
    print("Onboard LED test complete.")

#test