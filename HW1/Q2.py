
def calculate_plate_number(x, y):
    if x == 0 and y == 0:
        return 1

    counter = 0
    layer = 1


    # Calculate the distance from the origin
    if x == 0 or y == 0:
        layer += max(abs(x), abs(y))
    else:
        layer += abs(x) + abs(y)

    #print("layer:", layer)

    for i in range(1, layer , 1):
        if i == 1:
            counter += 1
        else:
            counter += (2 * i) + 2 * (i - 2)

    #print("counter:", counter)


    # top point
    if x == 0 and y == layer - 1:
        return counter + 1
    # right point
    elif x == layer - 1 and y == 0:
        return counter + layer
    # bottom point
    elif x == 0 and y == -layer + 1:
        return counter + (2 * layer) - 1
    # left point
    elif x == -layer + 1 and y == 0:
        return counter + (3 * layer) - 2
    # top right edge
    elif x > 0 and y > 0:
        return counter + 1 + x
    # bottem right edge
    elif x > 0 and y < 0:
        return counter + layer + abs(y)
    # bottom left edge
    elif x < 0 and y < 0:
        return counter + (2 *layer) - 1 + abs(x)
    # top left edge
    else:
        return counter + (3 * layer) - 2 + y


# Number of test cases
t = int(input())

# Iterate through each test case
for _ in range(t):
    # Read the coordinates of the house
    x, y = map(int, input().split())

    # Calculate the plate number
    plate_number = calculate_plate_number(x, y)

    # Print the plate number
    print(plate_number)
