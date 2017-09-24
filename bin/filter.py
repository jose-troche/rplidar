#!/usr/bin/env python
import sys
import re
import json

last_angle = -1
cycle = 1
max_cycle = 10
angles_count = 360
distances = [[]] * angles_count
filename = "../web/data.txt"

def save():
    for i in xrange(angles_count):
        distances[i] = sum(distances[i])/(len(distances[i]) or 1)

    print "Saving data:", distances
    
    with open(filename, 'w') as f:
        json.dump({"Data": distances}, f)

for line in sys.stdin:
    m = re.match(r".*theta: (?P<angle>\d+\.\d+) Dist: (?P<distance>\d+\.\d+) Q: (?P<quality>\d+) ", line)
    if m is not None:
        angle = int(float(m.group('angle')))
        distance = int(float(m.group('distance')))
        quality = int(m.group('quality'))

        if angle < last_angle:
            #print 'Cycle:', cycle
            cycle += 1
            if cycle > max_cycle:
                cycle = 1
                save()
                distances = [[]] * angles_count

        last_angle = angle

        if distance > 0 and quality > 0:
            distances[angle] = distances[angle] + [distance]





