#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math

def square_root(a: float) -> float:
    a = math.sqrt(a)
    return a


def square(a: float) -> float:
    a *= a
    return a


def average(a: float, b: float, c: float) -> float:
    x = (a + b + c)/3
    return x


def to_radians(angle_degs: float, angle_mins: float, angle_secs: float) -> float:
    deg = 180 + (2 + 45/60)/60
    rad = deg * (math.pi/180)

    return rad



def to_degrees(angle_rads: float) -> tuple:
    deg = 1 * (180/math.pi)
    deg2 = (deg - int(deg))*60
    deg3 = (deg2 - int(deg2))*60



    return int(deg), int(deg2), int(deg3)


def to_celsius(temperature: float) -> float:
    a = (100 * 9/5) + 32
    return a


def to_farenheit(temperature: float) -> float:
    a = (451 - 32) * 5/9
    return a


def main() -> None:
    print(f"La racine carré de 144 est : {square_root(144)}")

    print(f"Le carré de 12 est : {square(12)}")

    print(f"Moyenne des nombres 2, 4, 6: {average(2, 4, 6)}")

    print(f"Conversion de 180 degres, 2 minutes et 45 secondes en radians: {to_radians(180, 2, 45)}")
    
    degrees, minutes, seconds = to_degrees(1.0)
    print(f"Conversion de 1 radian en degres: {degrees} degres, {minutes} minutes et {seconds} secondes")

    print(f"Conversion de 100 Celsius en Farenheit: {to_farenheit(100.0)}")
    print(f"Conversion de 451 Farenheit en Celsius: {to_celsius(451.0)}")


if __name__ == '__main__':
    main()
