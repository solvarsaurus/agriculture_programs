# Agricultural Geographic Information System (Agricultural GIS)

The Agricultural Geographic Information System (Agricultural GIS) program is designed to manage field mapping, boundaries, and coordinate-based field management in agricultural settings. It allows you to create and test fields with boundary definitions and supports basic GIS operations for agricultural applications.

## Features
* Field Creation: Create field instances with unique names, crop types, and boundary definitions.
* Boundary Checking: Determine if a given point is within the boundaries of a field, allowing for geographic data processing and agricultural machinery compatibility.
* Singleton and Non-Singleton Factories: Includes factory functions that create singleton and non-singleton field instances for flexible field management.
* Automated Testing: A test suite that verifies singleton behavior and boundary checks, ensuring program reliability.
* Report Generating: A .txt file is created to identify the boundries of the fields.

## Usage
To use the Agricultural GIS program, follow these steps:

1. Clone or download the repository containing the program files.
2. Ensure you have Python installed on your system.
3. Run the code to create field instances and test their boundaries.
4. Customize the code to create additional fields or modify existing boundaries.

### Example
Here is an example that creates two fields with different boundary definitions and checks if certain points are within those boundaries:

```bash
from collections import namedtuple
from enum import Enum
from unittest import TestCase 

Point = namedtuple('Point', ['x', 'y'])

### Factory functions for creating field instances


def primary_field_factory():
    boundary_points = (Point(0, 0), Point(10, 10))
    return Field("Main Field", "Corn", boundary_points)

def secondary_field_factory():
    boundary_points = (Point(0, 0), Point(5, 5))
    return Field("Secondary Field", "Wheat", boundary_points)

```

### Create fields
```bash

field_1 = primary_field_factory()  # singleton field with specific boundary
field_2 = secondary_field_factory()  # new field with different boundary

```

### Test points
```bash

point_1 = Point(3, 4)
point_2 = Point(6, 6)

print("Point 1 within primary field:", field_1.is_within_boundaries(point_1))  # True
print("Point 2 within secondary field:", field_2.is_within_boundaries(point_2))  # False

```

### Test Suite
The program includes a test suite to evaluate the following:

* Singleton Behavior: Ensures the primary field factory always returns the same instance.
* Boundary Checks: Tests whether points are within field boundaries.

### To run the test suite, use the unittest module:

```bash

python -m unittest
Contributing
Contributions to the Agricultural GIS program are welcome. If you have ideas for new features, bug fixes, or improvements, feel free to open a pull request or create an issue.

```

## License

[MIT](https://choosealicense.com/licenses/mit/)



