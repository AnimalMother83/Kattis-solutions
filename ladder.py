#!  /usr/bin/python3
import sys
import math

def readIn():
    for line in sys.stdin:
        uv = line.split()
    return int(uv[0]), int(uv[1])

h, v = readIn()
angle_rad = math.radians(v)
sinus = math.sin(angle_rad)
ans = math.ceil(h/sinus)
#print(ans)
sys.stdout.write(str(ans))
