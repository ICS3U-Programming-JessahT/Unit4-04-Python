#!/usr/bin/env python3

# Created By: Jessah
# Date: Nov 23, 2022
# This program generates a random number and loops until
# the user guesses correctly

import random


def main():
    # generate random number from 0 - 9
    random_num = random.randint(0, 9)

    while True:
        # input from user
        string_num = input("Enter a number from 0 - 9: ")

        try:
            integer_num = int(string_num)
        except Exception:
            print("{} is not a valid input".format(string_num))

        else:
            if integer_num > 9 or integer_num < 0:
                print("error")

            else:  # if the user guesses the num right
                if integer_num == random.randint:
                    print("correct")
                    break
                else:  # loop and try again
                    print("Try again")

    if __name__ == "__main__":
        main()
