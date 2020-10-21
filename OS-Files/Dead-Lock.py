'''
Implementations of 'Look' disk scheduling algorithms in python.
'''
import sys
import pdb

LEFT = "LEFT"
RIGHT = "RIGHT"

LOWER_CYLINDER = 0
UPPER_CYLINDER = 4999

'''
LOOK algorithm
'''
def LOOK(requests, initialPosition):
    direction = RIGHT
    localRequests = list(requests)
    localRequests.sort()
    position = initialPosition
    movement = 0

    while localRequests:
        if position <= localRequests[0]: direction = RIGHT
        if position >= localRequests[-1]:
            direction = LEFT

        if position in localRequests:
            print
            "Servicing " + str(position)
            localRequests.remove(position)

            if not localRequests:
                break

        if direction == LEFT and position > LOWER_CYLINDER:
            position -= 1
        if direction == RIGHT and position < UPPER_CYLINDER: position += 1
        movement += 1
        return movement



# main function
if __name__ == '__main__':
    # requests = [2069, 1212, 2296, 2800, 544, 1618, 356, 1523, 4965, 3681]
    # requests = [98, 183, 37, 122, 14, 124, 65, 67]
    requests = [2069, 1212, 2296, 2800, 544, 1618, 356, 1523, 4965, 3681]
    initialPosition = int(sys.argv[1])
    print
    "\tLOOK = " + str(LOOK(requests, initialPosition))

