# Sensor Data Processing

readings = [10, 25, -60, 5, 55, 3, 8, -10, 60, 4]

# Identify valid readings
valid_readings = [
    value for value in readings
    if -50 <= value <= 50
]

# Identify invalid readings
invalid_readings = [
    value for value in readings
    if value < -50 or value > 50
]

# Convert Celsius to Fahrenheit
fahrenheit = [
    (value * 9 / 5) + 32
    for value in valid_readings
]

# Find minutes when temperature is outside 2°C to 8°C
alarm_minutes = [
    minute for minute, temperature in enumerate(valid_readings)
    if temperature < 2 or temperature > 8
]

print("Valid Readings:", valid_readings)
print("Invalid Readings:", invalid_readings)
print("Fahrenheit Values:", fahrenheit)
print("Alarm Minutes:", alarm_minutes)
