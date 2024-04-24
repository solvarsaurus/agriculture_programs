# Agricultural Scouting System

The Agricultural Scouting System is a Python-based program designed for agricultural applications, including field boundary identification, geographic coordinate management, weather-based analysis, automated alert systems, and distance calculations. This system is adaptable for various agricultural tasks such as crop monitoring, field scouting, and precision agriculture.

## Features

- **Coordinate Systems**: Supports Cartesian, Polar, and Geographic coordinate systems with conversion methods between them.
- **Field Boundaries**: Allows defining field boundaries and checking if a point is within those boundaries.
- **Haversine Distance**: Calculates the distance between two geographic points using the Haversine formula.
- **Weather-Based Analysis**: Analyzes temperature and humidity conditions to determine crop suitability.
- **Automated Alert System**: Sends automated email alerts for specific weather conditions, like high temperature or low humidity.

## Getting Started

To run the program, ensure you have Python installed. Clone or download this repository and navigate to the program directory. Execute the program to see different coordinate systems and boundary checks in action.

## Clone the repository
git clone https://github.com/your-repo/agricultural-scouting-system.git
cd agricultural-scouting-system

## Run the program
python scouting_system.py

## Example Usage:
Creating Coordinates: Create Cartesian, Polar, or Geographic points. For example, the code snippet below creates a geographic point for São Paulo:
```bash
p = Point.new_geographic_point(-23.5505, -46.6333)  # São Paulo (lat, lon)
Field Boundaries: Define a field's boundaries and check if a point is within them:
```
### Define a field with boundaries
```bash
field = Field("Test Field", "Corn", (Point(0, 0), Point(10, 10)))

```

### Check if a point is within the boundaries
```bash
point = Point.new_cartesian_point(3, 4)
is_within = field.is_within_boundaries(point)
```

## Weather-Based Analysis and Alerts: Analyze weather conditions and send automated alerts:

### Weather Analysis
```bash
temperature = 36  # Example high temperature
weather_report = analyze_weather(temperature, 20)  # 20% humidity
print("Weather Analysis:", weather_report)

# Send an alert if the temperature is too high
if temperature > 35:
    send_alert(
        "High Temperature Alert",
        "The temperature is too high for optimal crop growth. Consider irrigation.",
        "farmer@example.com"
    )
```

## Dependencies
Python 3.x
smtplib for email alerts
Ensure you have the required Python packages installed for successful execution.

## Contributing
Contributions are welcome! If you have suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

## License

[MIT](https://choosealicense.com/licenses/mit/)