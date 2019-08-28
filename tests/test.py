import sys
import unittest
sys.path.append('..')

from raytracing.vec3 import Vec3

""" 
To test, execute command in the test.py folder : python -m unittest [test.<test_class>]
test_class is the test class below. Tests functions from test_class will be executed.
"""

class Vec3_test(unittest.TestCase):
    def test_dot(self):
        v1 = Vec3(0, 0, 1)
        v2 = Vec3(0, 1, 0)
        dot = v1.dot(v2)
        assert(dot == "TODO")