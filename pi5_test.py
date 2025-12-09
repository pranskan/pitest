import RPi.GPIO as GPIO
import time

# Pin configuration
LED_PIN = 18  # Change this to the GPIO pin number where your LED is connected

# GPIO setup
GPIO.setmode(GPIO.BCM)  # Use BCM pin numbering
GPIO.setup(LED_PIN, GPIO.OUT)

print("Testing GPIO pins. Press Ctrl+C to stop.")

try:
    while True:
        GPIO.output(LED_PIN, GPIO.HIGH)  # Turn LED on
        time.sleep(1)  # Wait for 1 second
        GPIO.output(LED_PIN, GPIO.LOW)  # Turn LED off
        time.sleep(1)  # Wait for 1 second
except KeyboardInterrupt:
    print("\nTest stopped by user.")
finally:
    GPIO.cleanup()  # Reset GPIO settings
    print("GPIO cleanup done.")
