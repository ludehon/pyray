from math import pow, sqrt, pi, acos

class Vec3():
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
    
    def plus(self, v2):
        x = self.x + v2.x
        y = self.y + v2.y
        z = self.z + v2.z
        return Vec3(x, y, z)
    
    def minus(self, v2):
        x = self.x - v2.x
        y = self.y - v2.y
        z = self.z - v2.z
        return Vec3(x, y, z)
    
    def dot(self, v2):
        res = self.x * v2.x + self.y * v2.y + self.z * v2.z
        return res
    
    def float_mul(self, f):
        x = self.x * f
        y = self.y * f
        z = self.z * f
        return Vec3(x, y, z)
    
    def cross(self, v2):
        x = self.y * v2.z - self.z * v2.y
        y = self.z * v2.x - self.x * v2.z
        z = self.x * v2.y - self.y * v2.x
        return Vec3(x, y, z)

    def get_norm(self):
        res = sqrt(pow(self.x, 2) + pow(self.y, 2) + pow(self.z, 2))
        return res
    
    def get_normalized(self):
        norm = self.get_norm()
        x = self.x / norm
        y = self.y / norm
        z = self.z / norm
        return Vec3(x, y, z)
        
    def get_angle(self, v2):
        norm1 = self.get_norm()
        norm2 = v2.get_norm()
        dot = self.dot(v2)
        cos = dot / (norm1 * norm2)
        angle = (acos(cos) * 180) / pi
        return angle
    
    def ray_at(self, O, t):
        """
        Return position from the vector self and distance "t" and origin "O"
        """
        point = self.float_mul(t).plus(O)
        return point
    