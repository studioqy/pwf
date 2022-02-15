'''
Week 1 Assignment Tire Volume
Calculates the volume of tires on a car
Apr 24 2022
'''
import math
from datetime import datetime

# Gathers tire measurements
w = int(input('Enter tire width (mm): '))
a = int(input('Enter tire aspect ration: '))
d = int(input('Enter wheel diameter (in): '))

v = (math.pi * w ** 2 * a * (w * a + 2540 * d)) / 10000000  # v = tire volume

print(f'\nThe approximate volume is {v:.1f} cubic cm.\n')

# Extra: Calculates total volume of all tires on a vehicle
tire_count = int(input('How many tires does your vehicle have? '))
total_v = tire_count * v

print(
    f'The tires on your vehicle have an approximately {total_v:.1f} cubic cm combined volume.')

current_time_and_date = datetime.now(tz=None).date()

with open("volumes.txt", "at") as vol_file:

    print(current_time_and_date, w, a, d, v, file=vol_file)

# Extra- asks user if they would like to buy a tire, if yes then it takes
# their phone number and stores it
tire_buy = input("\nWould you like to buy a tire? (y/n)")
if tire_buy.lower() == "y":
    phone_num = input("Please enter your phone number: ")
    with open("volumes.txt", "at") as vol_file:
        print(phone_num, file=vol_file)
        print("Thank you. You will be contacted by a representative shortly")
