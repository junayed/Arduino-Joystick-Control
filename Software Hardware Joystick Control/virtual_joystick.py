# Python Code: virtual_joystick.py

import serial
import time
import threading
import tkinter as tk
from tkinter import ttk

def parse_arduino_data(line):
    try:
        # Remove start and end markers
        if line.startswith('<') and line.endswith('>'):
            line = line[1:-1]  # Remove '<' and '>'
        else:
            return None  # Discard lines without proper markers

        # Split the line into key-value pairs
        parts = line.split(',')
        data = {}
        for part in parts:
            if ':' in part:
                key, value = part.split(':')
                key = key.strip()
                value = value.strip()
                if key == 'X':
                    data['X'] = float(value)
                elif key == 'Y':
                    data['Y'] = float(value)
        return data
    except ValueError as e:
        # If parsing fails, print the error and return None
        print(f"Parsing error: {e}")
        return None

# Replace 'COM6' with your Arduino's serial port
arduino_port = 'COM6'  # For Windows
# arduino_port = '/dev/ttyACM0'  # For Linux/macOS

baud_rate = 9600  # Must match the baud rate in the Arduino code

# Initialize serial connection to the Arduino
ser = serial.Serial(arduino_port, baud_rate, timeout=1)

# Allow time for the serial connection to initialize
time.sleep(2)

# Global variables for software joystick values
software_x = 0.0
software_y = 0.0

# Function to send control mode to Arduino
def set_control_mode(mode):
    command = f"MODE:{mode}\n"
    ser.write(command.encode('utf-8'))

# Function to send software joystick values to Arduino
def send_software_values(x, y):
    command = f"X:{x},Y:{y}\n"
    ser.write(command.encode('utf-8'))

# Function to read data from Arduino
def read_from_arduino():
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').strip()
            # Print the raw line for debugging
            print(f"Received line: {line}")
            # Parse the line into data
            data = parse_arduino_data(line)
            if data:
                x_value = data['X']
                y_value = data['Y']
                # Display the values
                print(f"X-axis: {x_value:.2f} | Y-axis: {y_value:.2f}")
            else:
                # If parsing failed, print a message
                print("Parsing failed or incomplete data received.")
        else:
            time.sleep(0.01)

# Start the Arduino reading thread
threading.Thread(target=read_from_arduino, daemon=True).start()

# Create the GUI
root = tk.Tk()
root.title("Virtual Joystick Control")

# Control Mode Frame
mode_frame = ttk.LabelFrame(root, text="Control Mode")
mode_frame.pack(fill="x", padx=10, pady=5)

def on_mode_change():
    mode = mode_var.get()
    set_control_mode(mode)

mode_var = tk.IntVar(value=0)
hardware_radio = ttk.Radiobutton(mode_frame, text="Hardware Joystick", variable=mode_var, value=0, command=on_mode_change)
software_radio = ttk.Radiobutton(mode_frame, text="Software Control", variable=mode_var, value=1, command=on_mode_change)
hardware_radio.pack(side="left", padx=5, pady=5)
software_radio.pack(side="left", padx=5, pady=5)

# Software Control Frame
control_frame = ttk.LabelFrame(root, text="Software Joystick")
control_frame.pack(fill="both", expand=True, padx=10, pady=5)

# Functions for button presses
def move_up():
    global software_x
    software_x = x_max
    send_software_values(software_x, software_y)

def move_down():
    global software_x
    software_x = 0.0
    send_software_values(software_x, software_y)

def move_left():
    global software_y
    software_y = y_max
    send_software_values(software_x, software_y)

def move_right():
    global software_y
    software_y = 0.0
    send_software_values(software_x, software_y)

def center():
    global software_x, software_y
    software_x = 0.0
    software_y = 0.0
    send_software_values(software_x, software_y)

# Maximum values (should match Arduino code)
x_max = 1.6
y_max = 90.0

# Buttons for directions
up_button = ttk.Button(control_frame, text="Up", command=move_up)
down_button = ttk.Button(control_frame, text="Down", command=move_down)
left_button = ttk.Button(control_frame, text="Left", command=move_left)
right_button = ttk.Button(control_frame, text="Right", command=move_right)
center_button = ttk.Button(control_frame, text="Center", command=center)

# Arrange buttons in a grid
up_button.grid(row=0, column=1, padx=5, pady=5)
left_button.grid(row=1, column=0, padx=5, pady=5)
center_button.grid(row=1, column=1, padx=5, pady=5)
right_button.grid(row=1, column=2, padx=5, pady=5)
down_button.grid(row=2, column=1, padx=5, pady=5)

# Start the GUI main loop
try:
    root.mainloop()
except KeyboardInterrupt:
    print("Exiting...")
finally:
    ser.close()
