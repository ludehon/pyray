import sys
import unittest
sys.path.append('..')

from raytracing.vec3 import Vec3

""" 
To test, execute command in the test.py folder : python -m unittest [test.<test_class>]
test_class is the test class below. Tests functions from test_class will be executed.
"""

class Vec3_test(unittest.TestCase):
    def test_plus(self):
        v1 = Vec3(1, 2, 3)
        v2 = Vec3(3, 2, 1)
        addition = v1.plus(v2)
        assert((addition.x == v1.x + v2.x) and (addition.y == v1.y + v2.y) and (addition.z == v1.z + v2.z))
        
    def test_minus(self):
        v1 = Vec3(1, 2, 3)
        v2 = Vec3(3, 2, 1)
        addition = v1.minus(v2)
        assert((addition.x == v1.x - v2.x) and (addition.y == v1.y - v2.y) and (addition.z == v1.z - v2.z)) 
    
    def test_dot(self):
        v1 = Vec3(1, 2, 3)
        v2 = Vec3(3, 2, 1)
        dot = v1.dot(v2)
        assert(dot == (v1.x * v2.x + v1.y * v2.y + v1.z * v2.z))
        
    def test_float_mul(self):
        v1 = Vec3(1, 2, 3)
        f = 3
        mul = v1.float_mul(f)
        assert((mul.x == v1.x * f) and (mul.y == v1.y * f) and (mul.z == v1.z * f))
    
    def test_cross(self):
        # TODO
        assert(False)   
        
    def test_get_norm(self):
        # TODO
        assert(False)    
        
    def test_get_normalized(self):
        # TODO
        assert(False)      
        
    def test_get_angle(self):
        # TODO
        assert(False) 