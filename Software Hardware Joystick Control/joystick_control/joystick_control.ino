// Arduino Code: joystick_control.ino

// Pin Definitions
const int xPin = A0; // X-axis analog input
const int yPin = A1; // Y-axis analog input
const int swPin = 2; // Push button input (not used in this code)

// Constants for joystick calibration
const int joystickCenter = 512; // Center value for analog readings
const int deadZone = 50;        // Dead zone to prevent noise around center position

// Maximum output values
const float xMaxOutput = 1.6; // Max value for X-axis
const int yMaxOutput = 90;    // Max value for Y-axis

// Variables to hold joystick values
float xValue = 0.0;
float yValue = 0.0;

// Variables to hold software input values
float xSoftwareValue = 0.0;
float ySoftwareValue = 0.0;

// Control mode: 0 = hardware joystick, 1 = software control
int controlMode = 0;

void setup()
{
    Serial.begin(9600);           // Initialize serial communication at 9600 baud
    pinMode(swPin, INPUT_PULLUP); // Configure the push button pin (if needed)
}

void loop()
{
    // Check for serial input
    if (Serial.available() > 0)
    {
        String inputString = Serial.readStringUntil('\n');
        inputString.trim();

        // Process the serial command
        processSerialCommand(inputString);
    }

    // Depending on control mode, update values
    if (controlMode == 0)
    {
        // Hardware joystick control
        int rawX = analogRead(xPin); // Read raw X-axis value
        int rawY = analogRead(yPin); // Read raw Y-axis value

        // Process joystick inputs
        xValue = processJoystickAxis(rawX, xMaxOutput);
        yValue = processJoystickAxis(rawY, yMaxOutput);
    }
    else if (controlMode == 1)
    {
        // Software control
        xValue = xSoftwareValue;
        yValue = ySoftwareValue;
    }

    // Send the values over serial in a formatted string with start and end markers
    Serial.print("<X:");
    Serial.print(xValue, 2); // Limit to 2 decimal places
    Serial.print(",Y:");
    Serial.print(yValue, 2); // Limit to 2 decimal places
    Serial.println(">");

    delay(100); // Delay to control the update rate
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

// Function to process serial commands from Python
void processSerialCommand(String command)
{
    // Example command format: "MODE:1" or "X:1.2,Y:45.0"
    if (command.startsWith("MODE:"))
    {
        // Change control mode
        int mode = command.substring(5).toInt();
        if (mode == 0 || mode == 1)
        {
            controlMode = mode;
        }
    }
    else if (command.startsWith("X:"))
    {
        // Parse X and Y values
        int commaIndex = command.indexOf(',');
        if (commaIndex > 0)
        {
            String xStr = command.substring(2, commaIndex);
            String yStr = command.substring(commaIndex + 3); // Skip ",Y:"

            xSoftwareValue = xStr.toFloat();
            ySoftwareValue = yStr.toFloat();
        }
    }
}
