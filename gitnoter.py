#!/bin/python3
from time import sleep
import argparse
import curses
import datetime
import os

"""
    this script should:
        check if current repo state is committable checking for:
        - file size
        - existing swap files
        * try to understand better the content of git filter-repo analyze output

        if the state is not committable, try to automatically fix problems:
        - if file size is too big, if possible, compress or split in multiple files.

        if it is not possible to automatically fix, prompt user with actions to take
            in order to fix the problem BEFORE makeing a commit

        if it is all OK, only then commit and push to origin

    future ideas:
        - handle remote storage (maybe with rclone)
"""



def commit(message):
    """ makes the commit """
    pass

def check_health():
    """ check health of waht you're committing
        returns a list of actions to take before committing
    """
    pass

def main(stdscr):
    parser = argparse.ArgumentParser(description="gitnote will take care of you're notes")
    parser.add_argument('-t','--time',
        metavar='interval',
        help="interval between updates, in seconds (default is 10 mins)",
        type=int,
        default=60000)
    args = parser.parse_args()

    while True:
        try:
            sleep(args.time)
        except KeyboardInterrupt:
            raise KeyboardInterrupt

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("goodbye")
