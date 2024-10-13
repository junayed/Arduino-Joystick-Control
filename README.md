# Arduino Joystick Control

![Demo GIF](demo.gif)

This repository contains two projects demonstrating how to interface an Arduino Mega with Python to read joystick inputs and control applications. The projects include:

1. **Hardware Joystick Control**
2. **Software and Hardware Joystick Control**

Both projects were connected to an Unreal Engine virtual twin simulator for testing (see the included GIF above for a demonstration).

---

## Repository Structure

Arduino-Joystick-Control/ ├── Hardware-Joystick-Control/ │ ├── joystick_control/ │ │ └── joystick_control.ino │ └── joystick_reader.py ├── Software-Hardware-Joystick-Control/ │ ├── joystick_control/ │ │ └── joystick_control.ino │ └── virtual_joystick.py ├── README.md ├── LICENSE └── demo.gif # GIF demonstrating the final test case

markdown
Copy code




---

## Project Overview

### 1. Hardware Joystick Control

**Folder**: `Hardware-Joystick-Control`

This project demonstrates how to read inputs from a physical joystick connected to an Arduino Mega and display the data using a Python script. It involves:

- Reading analog inputs from the joystick on the Arduino.
- Mapping the joystick values to specified ranges.
- Sending the data over serial communication to a Python script.
- Displaying the joystick values in real-time using Python.

### 2. Software and Hardware Joystick Control

**Folder**: `Software-Hardware-Joystick-Control`

This project extends the hardware joystick control by adding a virtual joystick interface using a Python GUI (`tkinter`). It allows:

- Switching between physical joystick input and virtual joystick input.
- Controlling the Arduino using software inputs from the Python GUI.
- Reading and displaying joystick data in real-time.

---


Additional Notes
Serial Port Conflicts: Ensure the Arduino IDE's Serial Monitor is closed when running the Python scripts to avoid conflicts.
Joystick Calibration: If the joystick does not center at 512, adjust the joystickCenter and deadZone constants in the Arduino code.
Unreal Engine Integration: Although the code was connected to an Unreal Engine simulator, the integration steps are not included in this repository.
