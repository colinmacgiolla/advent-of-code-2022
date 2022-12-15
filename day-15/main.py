#!/bin/python

class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __eq__(self, other) -> bool:
        return (self.x, self.y) == (other.x,other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __hash__(self) -> int:
        return hash((self.x, self.y))
        
    def location(self):
        return (self.x, self.y)



def m_distance(a: Point, b: Point):
    return abs(a.x - b.x) + abs(a.y - b.y)


class Sensor:
    def __init__(self, sensor, beacon) -> None:
        self.sensor = sensor
        self.beacon = beacon
        self.distance = m_distance(self.sensor, self.beacon)


    def position(self):
        return self.sensor.location()


def solve_part_one(sensors, beacons, row):

    covered = set()

    for index,s in enumerate(sensors):
        
        # The distance between the sensor and where it would intersect the row
        row_distance = m_distance(s.sensor, Point(s.sensor.x, row))
        
        # if the row is too far away
        if row_distance > s.distance:
            # sensor isn't in range
            continue

        #print("Sensor number " + str(index+1) + " is in range. Location: " + str(s.position()) )
        
        
        # X position - the position - the difference between the probe range, and the point of intersection with the row
        for x in range( s.sensor.x - (s.distance - row_distance), s.sensor.x + ( s.distance - row_distance ) + 1 ):
            if Point(x,row) not in beacons:
                covered.add( Point(x,row) )

    return covered




def main():

    with open('C:\\Users\\colinmac\\Documents\\Git Projects\\advent-of-code-2022\\day-15\\input\\data.txt') as f:
        raw_input = f.read()

    beacons = set()
    sensors = []


    for line in raw_input.split("\n"):
        elements = line.split()
        sensor = ( Point( int(elements[2][2:-1]), int(elements[3][2:-1]) ) )
        beacon = ( Point( int(elements[8][2:-1]), int(elements[9][2:]) ) )
        sensors.append( Sensor(sensor, beacon) )

        beacons.add(beacon)


    print("%d sensors placed, and %d beacons located" % (len(sensors), len(beacons) ))



    y = 2000000
    empty = solve_part_one(sensors,beacons,y)


    # We count the 
    print("Beacon cannot be in: %d locations" % len(empty))
 

    print("End of Line")
    return 0



if __name__ == "__main__":
    main()
