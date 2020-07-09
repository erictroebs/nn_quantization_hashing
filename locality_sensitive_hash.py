from random import uniform
from math import tan, pi


def generate_line():
    alpha = uniform(0, pi)
    m = tan(alpha)
    return m


def generate_lines(count):
    return [generate_line() for i in range(0, count)]


def hash(point, lines):
    return [point[1] >= point[1] * line for line in lines]


def hamming(a, b):
    distance = 0
    for x, y in zip(a, b):
        if x != y:
            distance += 1

    return distance


if __name__ == '__main__':
    points = [
        (1, 50),
        (1, 0),
        (1, -1)
    ]
    lines = generate_lines(16)

    # calculate hashes
    hashes = [hash(p, lines) for p in points]

    # print hashes
    for p, h in zip(points, hashes):
        print(p, h)

    print()

    # calculate hamming distances
    for i1 in range(len(points)):
        for i2 in range(i1 + 1, len(points)):
            print(points[i1], "<>", points[i2], "->", hamming(hashes[i1], hashes[i2]))

    print()

    # estimate cosine distance
    for i1 in range(len(points)):
        for i2 in range(i1 + 1, len(points)):
            print(points[i1], "<>", points[i2], "->", "%0.2f * pi" % (hamming(hashes[i1], hashes[i2]) / len(lines)))
