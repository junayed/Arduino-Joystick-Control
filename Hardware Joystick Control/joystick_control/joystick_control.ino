// Arduino Code: joystick_control.ino

// Pin Definitions
const int xPin = A0;  // X-axis analog input
const int yPin = A1;  // Y-axis analog input
const int swPin = 2;  // Push button input (not used in this code)

// Constants for joystick calibration
const int joystickCenter = 512;  // Center value for analog readings
const int deadZone = 50;         // Dead zone to prevent noise around center position

// Maximum output values
const float xMaxOutput = 1.6;    // Max value for X-axis
const int yMaxOutput = 90;       // Max value for Y-axis

void setup()
{
    Serial.begin(9600);            // Initialize serial communication at 9600 baud
    pinMode(swPin, INPUT_PULLUP);  // Configure the push button pin (if needed)
}

void loop()
{
    int rawX = analogRead(xPin);   // Read raw X-axis value
    int rawY = analogRead(yPin);   // Read raw Y-axis value

    // Process joystick inputs
    float xValue = processJoystickAxis(rawX, xMaxOutput);
    float yValue = processJoystickAxis(rawY, yMaxOutput);

    // Send the values over serial in a formatted string with start and end markers
    Serial.print("<X:");
    Serial.print(xValue, 2);  // Limit to 2 decimal places
    Serial.print(",Y:");
    Serial.print(yValue, 2);  // Limit to 2 decimal places
    Serial.println(">");

    delay(100);  // Delay to control the update rate
}

// Function to process and map joystick axis values
float processJoystickAxis(int rawValue, float maxOutput)
{
    float outputValue = 0.0;

    if (rawValue > (joystickCenter + deadZone))
    {
        // Positive movement
        float percent = (float)(rawValue - (joystickCenter + deadZone)) / (1023 - (joystickCenter + deadZone));
        outputValue = percent * maxOutput;
        outputValue = constrain(outputValue, 0.0, maxOutput);
    }
    else if (rawValue < (joystickCenter - deadZone))
    {
        // Negative movement
        float percent = (float)((joystickCenter - deadZone) - rawValue) / ((joystickCenter - deadZone) - 0);
        outputValue = percent * maxOutput;
        outputValue = constrain(outputValue, 0.0, maxOutput);
    }
    else
    {
        // Within dead zone
        outputValue = 0.0;
    }

    return outputValue;
}
