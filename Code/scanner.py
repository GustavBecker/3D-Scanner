import RPi.GPIO as GPIO
import time
import subprocess
import os

# Pin assignments
TURN_STEP_PIN = 24
TURN_DIR_PIN = 23

TILT_STEP_PIN = 17
TILT_DIR_PIN = 27

# Adjusted based on the TB6600 DIP switch settings
STEPS_PER_ROTATION_TURN = 1600  
STEPS_PER_DEGREE_TILT = 4.44  # (Total steps for a full 360 tilt circle / 360)

# SCANNING SETTINGS
NUM_PHOTOS_PER_ROTATION = 36  # Takes a photo every 10 degrees of rotation
TILT_INCREMENT_DEGREE = 10    # Amount to tilt up after a full rotation
MAX_TILT_STEPS = 5            # Number of rows to scan upwards

# SETUP GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup([TURN_STEP_PIN, TURN_DIR_PIN, TILT_STEP_PIN, TILT_DIR_PIN], GPIO.OUT)

# Ensure output directory exists
output_dir = "/home/pi/3d_scan_images"
os.makedirs(output_dir, exist_ok=True)

def pulse_motor(step_pin, steps, delay=0.001):
    """Sends PWM-like pulses to move the stepper motor."""
    for _ in range(steps):
        GPIO.output(step_pin, GPIO.HIGH)
        time.sleep(delay)
        GPIO.output(step_pin, GPIO.LOW)
        time.sleep(delay)

def capture_photo(filename):
    """Triggers the Pi Camera Module 3 to capture an image."""
    print(f"Capturing: {filename}")
    # Uses the official Libcamera command line tool to snap a quick high-res photo
    cmd = f"libcamera-still -o {output_dir}/{filename} --immediate --nopreview"
    subprocess.run(cmd, shell=True)
    time.sleep(0.5) # Settling time after photo

try:
    print("Starting 3D Scan Sequence...")
    
    # Set initial directions (HIGH/LOW depends on mechanical mounting)
    GPIO.output(TURN_DIR_PIN, GPIO.HIGH) 
    GPIO.output(TILT_DIR_PIN, GPIO.HIGH)

    steps_per_photo_turn = int(STEPS_PER_ROTATION_TURN / NUM_PHOTOS_PER_ROTATION)
    steps_per_tilt_increment = int(TILT_INCREMENT_DEGREE * STEPS_PER_DEGREE_TILT)

    for tilt_row in range(MAX_TILT_STEPS):
        current_tilt_angle = tilt_row * TILT_INCREMENT_DEGREE
        print(f"\n--- Scanning Row {tilt_row + 1} at Tilt Angle: {current_tilt_angle}° ---")

        for photo_num in range(NUM_PHOTOS_PER_ROTATION):
            current_turn_angle = photo_num * (360 / NUM_PHOTOS_PER_ROTATION)
            
            # 1. Take a picture at current position
            filename = f"row_{tilt_row}_angle_{int(current_turn_angle)}.jpg"
            capture_photo(filename)
            
            # 2. Turn the turntable to the next slice
            if photo_num < (NUM_PHOTOS_PER_ROTATION - 1): # Don't turn after the last photo
                pulse_motor(TURN_STEP_PIN, steps_per_photo_turn)
                time.sleep(0.2) # Allow vibration to settle before next loop

        # One full turntable rotation complete! Now tilt up.
        if tilt_row < (MAX_TILT_STEPS - 1):
            print(f"Rotation complete. Tilting up {TILT_INCREMENT_DEGREE} degrees...")
            pulse_motor(TILT_STEP_PIN, steps_per_tilt_increment)
            time.sleep(0.5) # Wait for tilt arm settling

    print("\nScan complete! All images saved to /home/pi/3d_scan_images")

except KeyboardInterrupt:
    print("\nScan aborted by user.")

finally:
    GPIO.cleanup()