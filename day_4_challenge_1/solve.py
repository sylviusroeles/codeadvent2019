#!/usr/bin/env python

def main():
    min_r = 382345
    max_r = 843167

    #print matches(111111) #expect True double and increasing
    #print matches(122345) #expect True double and increasing
    #print matches(123789) #expect False no adjecent doubles
    #print matches(223450) #expect False double but decreasing at last digit

    passwords = 0

    for x in range(min_r, max_r):
        if matches(x): passwords += 1
    print passwords

def matches(pw):
    pw = [int(i) for i in str(pw)]
    incrementing = [i <= x for i, x in zip(pw, pw[1:])]
    doubles = [x is i for i, x in zip(pw, pw[1:])]
    return all(incrementing) and any(doubles)

if __name__ == "__main__":
    main()
