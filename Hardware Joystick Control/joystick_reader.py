# Python Code: joystick_reader.py

import serial
import time

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

# Replace 'COM3' with your Arduino's serial port
arduino_port = 'COM6'  # For Windows
# arduino_port = '/dev/ttyACM0'  # For Linux/macOS

baud_rate = 9600  # Must match the baud rate in the Arduino code

# Initialize serial connection to the Arduino
ser = serial.Serial(arduino_port, baud_rate, timeout=1)

# Allow time for the serial connection to initialize
time.sleep(2)

try:
    while True:
        if ser.in_waiting > 0:
            # Read a line from the serial port
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
            # If no data is available, wait briefly
            time.sleep(0.01)
except KeyboardInterrupt:
    print("Exiting...")
finally:
    # Close the serial connection on exit
    ser.close()
