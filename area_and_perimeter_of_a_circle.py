#!/usr/bin/env python3

# Created by: Mohammad-al-buraiki
# Created on December 2020
# This program calculates the area and perimeter of a circle
# with radius 15 mm

import math


def main():
    # this function calculates the area and the perimeter of a circle

    print("If the circle has the radius")
    print("15 mm")
    print("The area of the circle is {} mm²."
    .format(math.pi*(15**2)))
    print("The perimeter of the circle is {} mm."
    .format(2*math.pi*(15)))


if __name__ == "__main__":
    main()
