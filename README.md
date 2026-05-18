# The Ultimate hobbyist 3D Scanner!

An automated 3D scanning rig that rotates an object and tilts a camera to capture perfectly spaced photos for 3D modeling.

## About the Project
I wanted to get into 3D photogrammetry, but taking consistent photos by hand is tedious and inaccurate. To solve this, I built a completely automated, desktop scanning dome.

## How It Works
* **Brain:** A Raspberry Pi 3B+ controls the entire system.
* **Movement:** Dual NEMA 17 stepper motors turn the object on a turntable and tilt the camera arm up using a custom gear assembly.
* **Brain to Muscle:** High-torque TB6600 controllers drive the motors smoothly.
* **Capture:** A Raspberry Pi Camera Module 3 snaps crisp photos automatically right after the motors stop moving to avoid any blur.



A local Python script handles the timing: it rotates the object, stops, takes a photo, logs the position data, and automatically tilts upward by 10 degrees after every full rotation. The final image dataset is then transferred to a laptop for processing into a 3D mesh.

<img width="1920" height="813" alt="Main_2026-May-17_09-35-31PM-000_CustomizedView7972073945" src="https://github.com/user-attachments/assets/45495c2e-a5fe-482f-88ef-36d4cd3e3950" />
<img width="939" height="1109" alt="Main_2026-May-17_10-34-03PM-000_CustomizedView39547607428" src="https://github.com/user-attachments/assets/42e799c2-dcc1-4a1f-b6a6-0aea04cfe321" />
<img width="1225" height="1152" alt="Wiring" src="https://github.com/user-attachments/assets/fff88a7e-a2a5-43f0-b776-09bfcb4f21ef" />
<img width="637" height="387" alt="Screenshot 2026-05-18 142915" src="https://github.com/user-attachments/assets/e5c830ea-6330-4879-abbc-a9e20085e5e8" />


