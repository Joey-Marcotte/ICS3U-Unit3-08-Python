#!/usr/bin/env python3

# Created by: Joey Marcotte
# Created on: October 2019
# This program shows tif a year is a leap year


def main():

    while True:
        # imput
        year = input("Input the year you would like to see: ")

        # process
        try:
            year_as_number = int(year)
            if year_as_number >= 0:
                if year_as_number % 4 == 0 and year_as_number % 100 != 0:
                    print("")
                    print("{0} is a leap year".format(year_as_number))
                    break
                elif year_as_number % 1000 == 0:
                    # output
                    print("")
                    print("{0} is a leap year".format(year_as_number))
                    break
                else:
                    print("")
                    print("{0} is not a leap year".format(year_as_number))
                    break
        except(ValueError):
            print("That is not a valid year")
        finally:
            print("")


if __name__ == "__main__":
    main()
