# gridutil.py
#  Some useful functions for navigating square 2d grids
import math

from graphics import Polygon, Point
import numpy as np

DIRECTIONS = "NESW"
ORIENTATIONS = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0)}

def nextDirection(d, inc):
    return DIRECTIONS[(DIRECTIONS.index(d)+inc)%len(DIRECTIONS)]

def leftTurn(d):
    return nextDirection(d, -1)

def rightTurn(d):
    return nextDirection(d, 1)

def nextLoc(loc, d):
    x,y = loc
    dx, dy = ORIENTATIONS[d]
    return (x+dx, y+dy)

def legalLoc(loc, n):
    x,y = loc
    return 0<=x<n and 0<=y<n

def locations(n):
    for x in range(n):
        for y in range(n):
            yield (x,y)

def manhatDist(loc1, loc2):
    x1,y1 = loc1
    x2,y2 = loc2
    return abs(x1-x2) + abs(y1-y2)

def adjacent(l1,l2):
    x1,y1 = l1
    x2,y2 = l2
    return (abs(x1-x2) + abs(y2-y1)) == 1

def angledRectangle(center, size, angle):
    px, py = center
    sx, sy = size
    trig = [np.cos(np.deg2rad(angle)), np.sin(np.deg2rad(angle))]
    p1 = Point(px - sx * trig[0] / 2 - sy * trig[1] / 2, py - sx * trig[1] / 2 + sy * trig[0] / 2)
    p2 = Point(px - sx * trig[0] / 2 + sy * trig[1] / 2, py - sx * trig[1] / 2 - sy * trig[0] / 2)
    p3 = Point(px + sx * trig[0] / 2 + sy * trig[1] / 2, py + sx * trig[1] / 2 - sy * trig[0] / 2)
    p4 = Point(px + sx * trig[0] / 2 - sy * trig[1] / 2, py + sx * trig[1] / 2 + sy * trig[0] / 2)
    poly = Polygon(p1, p2, p3, p4)
    return poly

def tempFunc(center, size, angle):
    px, py = center
    sx, sy = size
    trig = [np.cos(np.deg2rad(angle)), np.sin(np.deg2rad(angle))]
    p1 = Point(px - sx * trig[0] / 2 - sy * trig[1] / 2, py - sx * trig[1] / 2 + sy * trig[0] / 2)
    p2 = Point(px - sx * trig[0] / 2 + sy * trig[1] / 2, py - sx * trig[1] / 2 - sy * trig[0] / 2)
    p3 = Point(px + sx * trig[0] / 2 + sy * trig[1] / 2, py + sx * trig[1] / 2 - sy * trig[0] / 2)
    p4 = Point(px + sx * trig[0] / 2 - sy * trig[1] / 2, py + sx * trig[1] / 2 + sy * trig[0] / 2)
    poly1 = Polygon(p1, p2, p4)
    poly2 = Polygon(p2, p3, p4)
    return poly1, poly2

def recContainsPoint(point, rectangle):
    x1 = rectangle.getP1().x
    y1 = rectangle.getP1().y
    x2 = rectangle.getP2().x
    y2 = rectangle.getP2().y
    x = point.x
    y = point.y
    if x1 > x2:
        temp_val = x1
        x1 = x2
        x2 = temp_val
    if y1 > y2:
        temp_val = y1
        y1 = y2
        y2 = temp_val
    return x1 <= point.x <= x2 and y1 <= point.y <= y2

def roadContainsPoint(point, road):
    angledRec = road.shapes[0]
    angle = road.angle
    points = []
    if road.type and not road.tunnel:
        points.append((road.shapes[0].points[0].x, road.shapes[0].points[0].y))
        points.append((road.shapes[0].points[1].x, road.shapes[0].points[1].y))
        points.append((road.shapes[1].points[1].x, road.shapes[1].points[1].y))
        points.append((road.shapes[1].points[2].x, road.shapes[1].points[2].y))
    else:
        for i in range(4):
            points.append((angledRec.points[i].x, angledRec.points[i].y))
    a = math.sqrt((points[2][0] - points[1][0])**2+(points[2][1]-points[1][1])**2)
    b = math.sqrt((points[0][0] - points[1][0])**2+(points[0][1]-points[1][1])**2)
    sn = np.sin(np.deg2rad(angle))
    cs = np.cos(np.deg2rad(angle))
    tn = np.tan(np.deg2rad(angle))
    if sn == 0 or cs == 0:
        # Prostokąt jest pod kątem prostym
        a1 = points[0][0]
        a2 = points[2][0]
        b1 = points[0][1]
        b2 = points[2][1]
        return min(a1, a2) <= point.x <= max(a1, a2) and min(b1, b2) <= point.y <= max(b1, b2)
    else:
        # Prostokąt nie jest pod kątem prostym
        center = ((points[0][0]+points[2][0]) / 2, (points[0][1] + points[2][1]) / 2)
        return -abs(b / 2 / cs) <= -point.x * tn + point.y - center[1] + center[0] * tn <= abs(b / 2 / cs) and \
               -abs(a / 2 / sn) <= point.x / tn + point.y - center[1] - center[0] / tn <= abs(a / 2 / sn)

