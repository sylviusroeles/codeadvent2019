#!/usr/bin/env python

def main():
    opcodes_ = get_opcodes()
    
    for noun in range(0, 98):
        for verb in range(0, 98):
            opcodes = opcodes_[:]
            output = compile(patch(opcodes, noun, verb))
            if output[0] == 19690720:
                print ''.join([str(noun), str(verb)])

def get_opcodes():
    opcodes = []
    with open('input.txt') as f:
        for line in f:
            opcodes += [int(opcode) for opcode in line.split(',')]
    return opcodes


def patch(data, noun, verb):
    data[1] = noun
    data[2] = verb
    return data

def compile(data):
    for opcode in range(0, len(data), 4):
        if data[opcode] is 99:
            return data
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
