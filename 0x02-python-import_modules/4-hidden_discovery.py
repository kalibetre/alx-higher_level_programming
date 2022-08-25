#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":

    for names in dir(hidden_4):
        if not names.startswith("__"):
            print(names)
