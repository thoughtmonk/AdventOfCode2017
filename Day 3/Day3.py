"""
Advent of Code Day 3

Part 1:
You come across an experimental new kind of memory stored on an infinite two-dimensional grid.

Each square on the grid is allocated in a spiral pattern starting at a location marked 1 and 
then counting up while spiraling outward. For example, the first few squares are allocated like 
this:

17  16  15  14  13
18   5   4   3  12
19   6   1   2  11
20   7   8   9  10
21  22  23---> ...

While this is very space-efficient (no squares are skipped), requested data must be carried back 
to square 1 (the location of the only access port for this memory system) by programs that can 
only move up, down, left, or right. They always take the shortest path: the Manhattan Distance 
between the location of the data and square 1.

For example:

    Data from square 1 is carried 0 steps, since it's at the access port.
    Data from square 12 is carried 3 steps, such as: down, left, left.
    Data from square 23 is carried only 2 steps: up twice.
    Data from square 1024 must be carried 31 steps.

How many steps are required to carry the data from the square identified in your puzzle input all 
the way to the access port?

Part 2:
As a stress test on the system, the programs here clear the grid and then store the value 1 in 
square 1. Then, in the same allocation order as shown above, they store the sum of the values 
in all adjacent squares, including diagonals.

So, the first few squares' values are chosen as follows:

    Square 1 starts with the value 1.
    Square 2 has only one adjacent filled square (with value 1), so it also stores 1.
    Square 3 has both of the above squares as neighbors and stores the sum of their values, 2.
    Square 4 has all three of the aforementioned squares as neighbors and stores the sum of their values, 4.
    Square 5 only has the first and fourth squares as neighbors, so it gets the value 5.

Once a square is written, its value does not change. Therefore, the first few squares would
receive the following values:

147  142  133  122   59
304    5    4    2   57
330   10    1    1   54
351   11   23   25   26
362  747  806--->   ...

What is the first value written that is larger than your puzzle input?
"""

def findSpiralCoordinate(location):
    
    i = 1
    coordinates = [0, 0]
    incrementer = 1

    while(1):
        i = i + incrementer
        coordinates[0] = coordinates[0] + incrementer
        
        if(i > location):
            if(i != location):
                coordinates[0] -= i - location 
            return coordinates

        i = i + incrementer
        coordinates[1] = coordinates[1] - incrementer

        if(i > location):
            if(i != location):
                coordinates[1] += i - location 
            return coordinates

        incrementer+=1

        i = i + incrementer
        coordinates[0] = coordinates[0] - incrementer
        
        if(i > location):
            if(i != location):
                coordinates[0] += i - location 
            return coordinates

        i = i + incrementer
        coordinates[1] = coordinates[1] + incrementer

        if(i > location):
            if(i != location):
                coordinates[1] -= i - location 
            return coordinates

        incrementer+=1
        
def findSpiralAdderValue(compareValue):
    # Create our array
    w,h = 20,20
    array = [[0 for x in range(w)] for y in range(h)]
    centerValue = 10
    array[centerValue][centerValue] = 1

    locationValue = 0
    location = 1

    while(locationValue < compareValue):
        location+=1
        coordinates = findSpiralCoordinate(location)
        coordinates[0] += centerValue
        coordinates[1] += centerValue
        locationValue = 0

        locationValue += array[coordinates[0] - 1][coordinates[1]]
        locationValue += array[coordinates[0] + 1][coordinates[1]]
        locationValue += array[coordinates[0] - 1][coordinates[1] + 1]
        locationValue += array[coordinates[0] + 1][coordinates[1] + 1]
        locationValue += array[coordinates[0] - 1][coordinates[1] - 1]
        locationValue += array[coordinates[0] + 1][coordinates[1] - 1]
        locationValue += array[coordinates[0]][coordinates[1] - 1]
        locationValue += array[coordinates[0]][coordinates[1] + 1]

        array[coordinates[0]][coordinates[1]] = locationValue

    return(locationValue)

        

location = findSpiralCoordinate(265149)

print(findSpiralAdderValue(265149))

print(abs(location[0]) + abs(location[1]))
