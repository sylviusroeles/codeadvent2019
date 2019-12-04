#!/usr/bin/env python

from collections import Counter

def main():
    with open('input.txt') as f:
        wires = [line.strip().split(',') for line in f.readlines()]
    
    wire_1 = wires[0]
    wire_2 = wires[1]
    #testing examples
    #wire_1 = ['R75','D30','R83','U83','L12','D49','R71','U7','L72']
    #wire_2 = ['U62','R66','U55','R34','D71','R55','D58','R83']
    
    #wire_1 = 'R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51'.split(',')
    #wire_2 = 'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7'.split(',')

    print "simulating wire 1"
    wire_1 = walk(wire_1)
    print "simulating wire 2"
    wire_2 = walk(wire_2)
    print "getting intersections"
    intersections = intersect(wire_1, wire_2)

    #print "min distance is:"
    #print min(calc_distance(intersections))
    print min(calc_steps(wire_1, wire_2, intersections))-1 #somehow there is an excess of 1, subtracting here


def walk(wire):
    path = [['0','0']]

    for direction in wire:
        x, y = get_latest_coordinate(path)
        if direction[:1] is 'R':
            for i in range(x, x + int(direction[1:])):
                path.append([str(i), str(y)])
        if direction[:1] is 'L':
            for i in range(x, x - int(direction[1:]), -1):
                path.append([str(i), str(y)])
        if direction[:1] is 'U':
            for i in range(y, y + int(direction[1:])):
                path.append([str(x), str(i)])
        if direction[:1] is 'D':
            for i in range(y, y - int(direction[1:]), -1):
                path.append([str(x), str(i)])
    return path[1:]
            
def get_latest_coordinate(path):
    x = int(path[len(path)-1][0])
    y = int(path[len(path)-1][1])
    return x, y;

def intersect(wire_1, wire_2):
    wire_1 = [tuple(wire) for wire in wire_1[1:]] 
    wire_2 = [tuple(wire) for wire in wire_2[1:]] #remove the initial intersection at origin
    return set(wire_1) & set(wire_2) 
    #return [x for x in wires if x not in duplicates and not duplicates.add(x)]

def calc_steps(wire_1, wire_2, intersections):
    steps = []

    for intersection in list(intersections):
        cur_steps = 0
        for wire in [wire_1, wire_2]:
            for step in wire:
                if int(step[0]) == int(intersection[0]) and int(step[1]) == int(intersection[1]):
                    break
                else:
                    cur_steps += 1
        steps.append(cur_steps)
    return steps


def calc_distance(intersections):
    return [abs(int(intersection[0])) + abs(int(intersection[1])) for intersection in intersections]

if __name__ == "__main__":
    main()
