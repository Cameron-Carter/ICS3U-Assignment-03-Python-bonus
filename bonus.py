#!/usr/bin/env python3

# Created by: Cameron Carter
# Created on May 2021
# This program tells you your bonus to your salary


def main():
    # This function determines salary bonus

    # Input
    salary = float(input("Enter your salary ($): "))
    years = float(input("\nEnter your years of service: "))

    # Process and Output
    if years > 5:
        bonus = salary * 0.05
        print("\nYou get a bonus of ${:,.2f}!".format(bonus))
    else:
        print("\nYou get no bonus!")
    print("\nDone.")


if __name__ == "__main__":
    main()
