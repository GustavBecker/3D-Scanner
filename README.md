# The ultimate hobbyist 3D Scanner!

An automated 3D scanning rig that rotates an object and tilts a camera to capture perfectly spaced photos for 3D modeling.

## About the Project
I wanted to get into 3D photogrammetry, but taking consistent photos by hand is tedious and inaccurate. To solve this, I built a completely automated, desktop scanning dome.

## How It Works
* **Brain:** A Raspberry Pi 3B+ controls the entire system.
* **Movement:** Dual NEMA 17 stepper motors turn the object on a turntable and tilt the camera arm up using a custom gear assembly.
* **Brain to Muscle:** High-torque TB6600 controllers drive the motors smoothly.
* **Capture:** A Raspberry Pi Camera Module 3 snaps crisp photos automatically right after the motors stop moving to avoid any blur.



A local Python script handles the timing: it rotates the object, stops, takes a photo, logs the position data, and automatically tilts upward by 10 degrees after every full rotation. The final image dataset is then transferred to a laptop for processing into a 3D mesh.


