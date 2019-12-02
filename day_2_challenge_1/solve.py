#!/usr/bin/env python

def main():
    opcodes = []
    with open('input.txt') as f:
        for line in f:
            opcodes += [int(opcode) for opcode in line.split(',')]
    compile(patch(opcodes))

def patch(data):
    data[1] = 12
    data[2] = 2
    return data

def compile(data):
    for opcode in range(0, len(data), 4):
        if data[opcode] is 99:
            print data
            break
        if data[opcode] is 2:
            data[data[opcode + 3]] = multiply(data[data[opcode + 1]], data[data[opcode + 2]])
            continue
        if data[opcode] is 1: 
            data[data[opcode + 3]] = add(data[data[opcode + 1]], data[data[opcode + 2]])
            continue

def add(x, y):
    return x + y

def multiply(x, y):
    return x * y

if __name__ == "__main__":
    main()
