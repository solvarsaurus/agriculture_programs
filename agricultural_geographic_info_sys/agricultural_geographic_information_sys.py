from unittest import TestCase
from copy import deepcopy
from collections import namedtuple
import math
import os

# Define a Point to represent coordinates in Cartesian space
Point = namedtuple('Point', ['x', 'y'])

# Function to check if a factory creates identifier instances
def identifier_1(factory):
    instance_1 = factory()
    instance_2 = factory()
    return instance_1 is instance_2

# A simple Field class representing a field with boundaries in an agricultural context
class Field:
    def __init__(self, field_name, crop_type, boundary_points):
        self.field_name = field_name
        self.crop_type = crop_type
        self.boundary_points = boundary_points

    def __str__(self):
        return f'Field: {self.field_name}, Crop: {self.crop_type}'

    # Method to check if a point is within the field boundaries
    def is_within_boundaries(self, point):
        # Assume a rectangular boundary defined by two diagonal points
        bottom_left, top_right = self.boundary_points
        return (
            bottom_left.x <= point.x <= top_right.x and
            bottom_left.y <= point.y <= top_right.y
        )

    # Method to save the field's boundaries to a text file
    def save_boundaries_to_file(self, file_path):
        with open(file_path, 'w') as f:
            bottom_left, top_right = self.boundary_points
            f.write(f"Field: {self.field_name}\n")
            f.write(f"Crop: {self.crop_type}\n")
            f.write(f"Boundary Bottom-Left: {bottom_left}\n")
            f.write(f"Boundary Top-Right: {top_right}\n")

# Factory functions for creating field instances with boundary definitions
def primary_field_factory():
    if not hasattr(primary_field_factory, 'instance'):
        boundary_points = (Point(0, 0), Point(10, 10))
        primary_field_factory.instance = Field("Main Field", "Corn", boundary_points)
    return primary_field_factory.instance

def secondary_field_factory():
    boundary_points = (Point(0, 0), Point(5, 5))
    return Field("Secondary Field", "Wheat", boundary_points)

# Test case to evaluate singleton behavior and boundary checks
class Evaluate(TestCase):
    def test_primary_field_is_singleton(self):
        self.assertTrue(identifier_1(primary_field_factory))

    def test_secondary_field_is_not_singleton(self):
        self.assertFalse(identifier_1(secondary_field_factory))

    def test_point_within_primary_field_boundaries(self):
        field = primary_field_factory()
        point = Point(3, 4)
        self.assertTrue(field.is_within_boundaries(point))

    def test_point_outside_secondary_field_boundaries(self):
        field = secondary_field_factory()
        point = Point(6, 6)
        self.assertFalse(field.is_within_boundaries(point))

# If run directly, create field instances, check boundaries, and save to text file
if __name__ == '__main__':
    field_1 = primary_field_factory()  # singleton field with specific boundary
    field_2 = secondary_field_factory()  # new field with different boundary

    # Save field boundaries to text files
    field_1.save_boundaries_to_file("field_1_boundaries.txt")
    field_2.save_boundaries_to_file("field_2_boundaries.txt")

    point_1 = Point(3, 4)
    point_2 = Point(6, 6)

    print("Singleton Field:", field_1)
    print("New Field:", field_2)

    print("Point 1 within primary field:", field_1.is_within_boundaries(point_1))
    print("Point 2 within secondary field:", field_2.is_within_boundaries(point_2))