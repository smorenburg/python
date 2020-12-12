#!/usr/bin/env python3.8

# BMI = (Weight in kilograms / Height in meters squared)
# Imperial version: BMI * 703

def gather_info():
    height = float(input(
        "What is your height? (inches or meters) "
    ))
    weight = float(input(
        "What is your weight? (pounds or kilograms) "
    ))
    system = input(
        "Are you measurements in metric or imperial units? "
    ).lower().strip()
    return (height, weight, system)


def calculate_bmi(weight, height, system='metric'):
    """
    Return the Body Mass Index (BIM) for the
    given weight, height, and measurement system.
    """
    if system == 'metric':
        bmi = (weight / (height ** 2))
    else:
        bmi = 703 * (weight / (height ** 2))
    return bmi


while True:
    height, weight, system = gather_info()
    if system.startswith('i'):
        bmi = calculate_bmi(
            weight=weight,
            system=system,
            height=height
        )
        print(
            f"Your BMI is {bmi}."
        )
        break
    elif system.startswith('m'):
        bmi = calculate_bmi(weight, height)
        print(
            f"Your BMI is {bmi}."
        )
        break
    else:
        print(
            "Error: Unknown measurement system. "
            "Please use imperial or metric."
        )
