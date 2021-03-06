#!/usr/bin/env python3
import random as rnd
import pandas as pd
from datetime import datetime as dt
from pair import Pair, User


def check_location(pairs):
    for pair in pairs:
        if pair.sameLocations():
            return False
    return True


MAX_RETRIES = 5


def main():
    print("Posty Pal Randomizer!")

    df = pd.read_csv('data.csv')
    print(df)
    users = []
    for row in df.itertuples():
        users.append(User(row.username, row.location))

    rnd.shuffle(users)

    retry = 0
    pairs = []
    while retry < MAX_RETRIES:
        retry += 1
        pairs = []
        for i in range(0, len(users), 2):
            pairs.append(Pair(users[i], users[i + 1]))
        if check_location(pairs):
            break

    print()
    f = open("results-" + dt.now().strftime("%m-%d-%Y") + ".txt", "w")
    for pair in pairs:
        print(pair)
        f.write(repr(pair) + "\n")
    f.close()


if __name__ == '__main__':
    main()
