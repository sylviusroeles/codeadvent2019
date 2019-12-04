#!/usr/bin/env python

def main():
    min_r = 382345
    max_r = 843167

    #challenge 1 tests
    #print matches(111111), "expect True double and increasing"
    #print matches(122345) #expect True double and increasing
    #print matches(123789) #expect False no adjecent doubles
    #print matches(223450) #expect False double but decreasing at last digit

    #challenge 2 tests
    print matches(112233), True #expect True doubles, increasing, doubles not part of greater group
    print matches(123444), False #expect False doubles, increasing, but doubles part of 444
    print matches(111122), True #expect True doubles, increasing, fail on 1111, succeed on 22
    print matches(666789), False
    passwords = 0
    guesses = []

    for x in range(min_r, max_r):
        if matches(x): 
            passwords += 1
            guesses.append(x)
    print passwords, guesses

def matches(pw):
    pw = [int(i) for i in str(pw)]
    incrementing = [i <= x for i, x in zip(pw, pw[1:])]
    pw = [""] + pw + [""] #temp add nonce to prevent premature conditional abort
    doubles = [a is not prev and a is b and a is not nex for prev, a, b, nex in zip(pw, pw[1:], pw[2:], pw[3:])]
    return all(incrementing) and any(doubles)

if __name__ == "__main__":
    main()
