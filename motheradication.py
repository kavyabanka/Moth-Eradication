import sys
import math

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0
    elif val > 0:
        return 1
    else:
        return 2 

def convex_hull(points):
    n = len(points)
    if n < 3:
        return []
    hull = []
    l = 0
    for i in range(1, n):
        if points[i][0] < points[l][0]:
            l = i
    p = l
    q = 0
    while True:
        hull.append(points[p])
        q = (p + 1) % n
        for i in range(n):
            if orientation(points[p], points[i], points[q]) == 2:
                q = i
        p = q
        if p == l:
            break
    return hull

def main(argv):
    region = 0
    n = int(argv[0])
    if n == 0:
        return
    region += 1
    points = []
    for i in range(n):
         
        x, y = map(float, argv[i * 2 + 1: i * 2 + 3])
        points.append((x, y))
    hull = convex_hull(points)
    print("Region #{}:".format(region))
    for i, p in enumerate(hull):
        print("({:.1f}, {:.1f})".format(p[0], p[1]), end="")
        if i == len(hull) - 1:
            print("-({:.1f}, {:.1f})".format(hull[0][0], hull[0][1]))
        else:
            print("-", end="")
    perimeter = 0
    for i in range(len(hull) - 1):
        perimeter += distance(hull[i], hull[i + 1])
    perimeter += distance(hull[-1], hull[0])
    print("Perimeter length = {:.2f}".format(perimeter))
    print()

if __name__ == "__main__":
    main(sys.argv[1:])
