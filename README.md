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

## Table of Contents

- [Project Overview](#project-overview)
- [Prerequisites](#prerequisites)
- [Installation and Setup](#installation-and-setup)
  - [Setting Up the Hardware](#setting-up-the-hardware)
  - [Setting Up the Software](#setting-up-the-software)
- [Projects](#projects)
  - [1. Hardware Joystick Control](#1-hardware-joystick-control)
  - [2. Software and Hardware Joystick Control](#2-software-and-hardware-joystick-control)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

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

## Prerequisites

### Hardware

- **Arduino Mega 2560**
- **Joystick Module**
  - X-axis (VRX)
  - Y-axis (VRY)
  - Push Button (SW) - optional
- **USB Cable** for connecting the Arduino to the computer
- **Connecting Wires**

### Software

- **Arduino IDE**
- **Python 3.7** or higher
- **Conda** (optional, for managing Python environments)
- **Python Packages**:
  - `pyserial`
  - `tkinter` (comes with standard Python installation)
- **Git** (for cloning the repository)

---

## Installation and Setup

### Setting Up the Hardware

#### Joystick Connections

- **X-axis (VRX)**: Connect to analog pin `A0` on the Arduino.
- **Y-axis (VRY)**: Connect to analog pin `A1` on the Arduino.
- **Push Button (SW)**: Connect to digital pin `2` on the Arduino (optional).
- **GND**: Connect to GND on the Arduino.
- **VCC**: Connect to 5V on the Arduino.

#### Diagram

Joystick Module Arduino Mega

lua
Copy code
  VRX     -------->    A0
  VRY     -------->    A1
  SW      -------->    D2 (optional)
  GND     -------->    GND
  VCC     -------->    5V
bash
Copy code

### Setting Up the Software

#### Cloning the Repository

```bash
git clone https://github.com/Junayed/Arduino-Joystick-Control.git
cd Arduino-Joystick-Control
Setting Up a Conda Environment (Optional)
It's recommended to use a Conda environment to manage dependencies.

bash
Copy code
conda create -n joystick_env python=3.9
conda activate joystick_env
Installing Required Python Packages
bash
Copy code
# Install pyserial for serial communication
conda install -c conda-forge pyserial

# Install tkinter (should be included with Python, but can be installed via conda if necessary)
conda install -c anaconda tk
Projects
1. Hardware Joystick Control
Folder: Hardware-Joystick-Control

Arduino Setup
Open the Arduino IDE.
Navigate to Hardware-Joystick-Control/joystick_control/joystick_control.ino.
Connect your Arduino Mega to your computer via USB.
Select Tools > Board > Arduino Mega 2560.
Select the correct Port under Tools > Port.
Upload the code to the Arduino.
Python Script
Navigate to Hardware-Joystick-Control/joystick_reader.py.

Open the script in a text editor.

Update the arduino_port variable to match your Arduino's serial port.

python
Copy code
arduino_port = 'COM3'  # For Windows
# arduino_port = '/dev/ttyACM0'  # For Linux/macOS
Run the script:

bash
Copy code
python joystick_reader.py
Usage
Move the joystick and observe the output in the terminal.
Press Ctrl+C to terminate the script.
2. Software and Hardware Joystick Control
Folder: Software-Hardware-Joystick-Control

Arduino Setup
Open the Arduino IDE.
Navigate to Software-Hardware-Joystick-Control/joystick_control/joystick_control.ino.
Connect your Arduino Mega to your computer via USB.
Select Tools > Board > Arduino Mega 2560.
Select the correct Port under Tools > Port.
Upload the code to the Arduino.
Python Script
Navigate to Software-Hardware-Joystick-Control/virtual_joystick.py.

Open the script in a text editor.

Update the arduino_port variable to match your Arduino's serial port.

python
Copy code
arduino_port = 'COM3'  # For Windows
# arduino_port = '/dev/ttyACM0'  # For Linux/macOS
Run the script:

bash
Copy code
python virtual_joystick.py
Usage
The GUI window will appear with options to select the control mode.
Hardware Joystick:
Select "Hardware Joystick" mode.
Use the physical joystick to control.
Software Control:
Select "Software Control" mode.
Use the buttons in the GUI to simulate joystick movements.
Observe the output in the terminal.
Close the GUI window or press Ctrl+C in the terminal to terminate the script.
Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
Special thanks to all contributors and the open-source community.
This project was connected with an Unreal Engine virtual twin simulator for testing purposes.
Note: Remember to replace 'COM3' with the correct serial port for your Arduino in the Python scripts. You can find the serial port in the Arduino IDE under Tools > Port.

Git Repository Details
Repository Name
Arduino-Joystick-Control

Folder Structure
Hardware-Joystick-Control
joystick_control/
joystick_control.ino - Arduino code for hardware joystick control.
joystick_reader.py - Python script for reading joystick data.
Software-Hardware-Joystick-Control
joystick_control/
joystick_control.ino - Arduino code for hardware and software joystick control.
virtual_joystick.py - Python script with GUI for virtual joystick control.
README.md - This README file.
LICENSE - The MIT License file.
demo.gif - GIF demonstrating the final test case.
Pushing to GitHub
Initialize Git in Your Project Directory

bash
Copy code
git init
Add Files to the Repository

bash
Copy code
git add .
Commit Changes

bash
Copy code
git commit -m "Initial commit"
Create a New Repository on GitHub

Go to GitHub and create a new repository named Arduino-Joystick-Control.
Add Remote Origin

bash
Copy code
git remote add origin https://github.com/Junayed/Arduino-Joystick-Control.git
Push to GitHub

bash
Copy code
git branch -M main
git push -u origin main
Additional Notes
Serial Port Conflicts: Ensure the Arduino IDE's Serial Monitor is closed when running the Python scripts to avoid conflicts.
Joystick Calibration: If the joystick does not center at 512, adjust the joystickCenter and deadZone constants in the Arduino code.
Unreal Engine Integration: Although the code was connected to an Unreal Engine simulator, the integration steps are not included in this repository.
