from enum import Enum
from math import sin, cos, sqrt, atan2, radians, degrees
from datetime import datetime
import smtplib
from email.mime.text import MIMEText


class CoordinateSystem(Enum):
    CARTESIAN = 1
    POLAR = 2
    GEOGRAPHIC = 3


class Point:
    def __str__(self):
        return f'x: {self.x}, y: {self.y}'

    def __init__(self, a, b, system=CoordinateSystem.CARTESIAN):
        if system == CoordinateSystem.CARTESIAN:
            self.x = a
            self.y = b
        elif system == CoordinateSystem.POLAR:
            self.x = a * cos(b)
            self.y = a * sin(b)
        elif system == CoordinateSystem.GEOGRAPHIC:
            # Interpret 'a' as latitude and 'b' as longitude in degrees
            self.x = a
            self.y = b

    # Factory methods for creating various types of coordinates
    @staticmethod
    def new_cartesian_point(x, y):
        return Point(x, y)

    @staticmethod
    def new_polar_point(rho, theta):
        return Point(rho * cos(theta), rho * sin(theta))

    @staticmethod
    def new_geographic_point(lat, lon):
        return Point(lat, lon, CoordinateSystem.GEOGRAPHIC)

    # Calculate distance between two points (Haversine formula for geographic coordinates)
    @staticmethod
    def haversine_distance(p1, p2):
        R = 6371  # Earth's radius in kilometers
        lat1, lon1 = radians(p1.x), radians(p2.y)
        lat2, lon2 = radians(p2.x), radians(p2.y)

        dlat = lat2 - lat1
        dlon = lon2 - lon1
        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))

        distance = R * c
        return distance


# Function to analyze weather data
def analyze_weather(temperature, humidity):
    if temperature > 35:
        return "Too hot for crops. Ensure irrigation."
    elif humidity < 20:
        return "Low humidity. Consider watering."
    else:
        return "Weather conditions are optimal."


# Function to send automated email alerts
def send_alert(subject, message, recipient_email):
    sender_email = "agriculture_alerts@example.com"
    smtp_server = "smtp.example.com"  # Replace with your SMTP server
    smtp_port = 587  # Or another port if needed
    smtp_user = "your_username"  # Your SMTP server username
    smtp_password = "your_password"  # Your SMTP server password

    # Compose the email
    msg = MIMEText(message)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = recipient_email

    # Send the email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_user, smtp_password)
        server.sendmail(sender_email, recipient_email, msg.as_string())


if __name__ == '__main__':
    # Example usage of different coordinate types
    p1 = Point.new_cartesian_point(3, 4)
    p2 = Point.new_polar_point(5, 0.785)  # 0.785 radians is approximately 45 degrees
    p3 = Point.new_geographic_point(-23.5505, -46.6333)  # São Paulo (lat, lon)
    p4 = Point.new_geographic_point(-25.4297, -49.2719)  # Curitiba (lat, lon)

    print("Cartesian:", p1)
    print("Polar:", p2)
    print("Geographic (São Paulo):", p3)
    print("Geographic (Curitiba):", p4)

    # Calculate distance between geographic points (São Paulo to Curitiba)
    distance = Point.haversine_distance(p3, p4)
    print("Distance between São Paulo and Curitiba:", distance, "km")

    # Weather-based analysis
    temperature = 30  # Example temperature
    humidity = 40  # Example humidity
    weather_report = analyze_weather(temperature, humidity)
    print("Weather Analysis:", weather_report)

    # Automated alert system
    if temperature > 35:
        send_alert(
            "High Temperature Alert",
            "The temperature is too high for optimal crop growth. Consider irrigation.",
            "farmer@example.com"
        )