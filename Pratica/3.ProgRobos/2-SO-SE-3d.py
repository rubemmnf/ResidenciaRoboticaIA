from spatialmath import *
from math import pi

rx = SO3.Rx (pi/2)
#print(rx)

ry = SO3.Ry (pi/2)
#print(ry)

rz = SO3.Rz (pi/2)
#print(rz)

Rxyz = rx * ry * rz
#print(Rxyz)

Rxzy = rx * rz * ry
print(Rxzy)

Tx = SE3.Tx(1)
Ty = SE3.Ty(2)
Tz = SE3.Tz(3)

Txyz = Tx * Ty * Tz

a = [1,0,0]

a_t = Txyz * a

print(a_t)