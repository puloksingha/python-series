"""
geometry.py — Geometric calculations
"""

import math

def circle_area(radius):
    """Calculate area of circle."""
    return math.pi * radius ** 2

def circle_circumference(radius):
    """Calculate circumference of circle."""
    return 2 * math.pi * radius

def rectangle_area(width, height):
    """Calculate area of rectangle."""
    return width * height
