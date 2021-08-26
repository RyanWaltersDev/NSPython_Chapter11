#!/usr/bin/env python3
from name_function import get_formatted_name

print("Enter 'q' any time to quit")
while True:
    first = input("\nPlease enter your first name: ")
    if first == 'q' or first == 'Q':
        break
    last = input("\nPlease enter your last name: ")
    if last == 'q' or last == 'Q':
        break
    print(f"You have entered {first} {last}.")
    answer = input("Is this correct? [Y/N] ")
    if answer == 'y' or answer == 'Y':
        break
    elif answer == 'q' or answer == 'Q':
        break
    elif answer == 'n' or answer == 'N':
        print("Ok, let's try this again.")
    else:
        print("Please enter a valid response")

formatted_name = get_formatted_name(first, last)
print(f"\tNeatly formatted name: {formatted_name}.")
