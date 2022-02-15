'''
Week 3 Checkpoint Fuel Efficiency
Computes the efficiency of fuel in a vehicle
May 4 2021
'''


def main():
    odom_start = int(input("Enter starting odometer value (miles): "))

    odom_end = int(input("Enter ending odometer value (miles): "))

    # Get a fuel amount in U.S. gallons from the user.
    fuel_gal = float(input("Enter fuel used (gallons): "))

    mpg = miles_per_gallon(odom_start, odom_end, fuel_gal)
    # Call the miles_per_gallon function and store
    # the result in a variable named mpg.

    lp100k = lp100k_from_mpg(mpg)
    # Call the lp100k_from_mpg function to convert the
    # miles per gallon to liters per 100 kilometers and
    # store the result in a variable named lp100k.

    # Round the miles per gallon to one digit after the decimal.

    # Round the liters per 100 km to two digits after the decimal.

    # Display the results for the user to see.
    print(f"{mpg:.1f} miles per gallon")
    print(f'{lp100k:.2f} litres per 100 kilometres')
    pass


def miles_per_gallon(start_miles, end_miles, amount_gallons):
    miles_per_gal = (end_miles - start_miles) / amount_gallons
    return miles_per_gal
    """Compute and return the average number of miles
    that a vehicle traveled per gallon of fuel.

    Parameters
        start_miles: An odometer value in miles.
        end_miles: Another odometer value in miles.
        amount_gallons: A fuel amount in U.S. gallons.
    Return: Fuel efficiency in miles per gallon.
    """


def lp100k_from_mpg(mpg):
    lp100k = 235.215 / mpg
    return lp100k
    """Convert miles per gallon to liters per 100
    kilometers and return the converted value.

    Parameter mpg: A value in miles per gallon
    Return: The converted value in liters per 100km.
    """


# Call the main function so that
# this program will start executing.
main()
