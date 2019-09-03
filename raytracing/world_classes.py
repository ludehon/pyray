from math import tan, pi, sqrt

from vec3 import Vec3

class World():
    def __init__(self, elements=[], lights=[], cameras=[]):
        self.elements = elements
        self.lights = lights
        self.cameras = cameras

    def add_element(self, e):
        self.elements.append(e)
    
    def add_light(self, l):
        self.lights.append(l)
        
    def add_camera(self, c):
        self.cameras.append(c)
        
class Object3D:
    """
    Object3D is abstract object in 3D space
    """
    def __init__(self, position, speed=Vec3()):
        self.position = position
        self.speed = speed
        
class Element(Object3D):
    """
    Element is 3D object that has 3D volume
    """
    def __init__(self, type, position, speed=0):
        super().__init__(position, speed)
        self.type = type
        
class Light(Object3D):
    def __init__(self, position, speed, color=Vec3(255, 255, 255), intensity=1):
        super().__init__(position, speed)
        self.color = color
        self.intensity = intensity

class Camera(Object3D):
    def __init__(self, position, speed, at, up, fov, height, width):
        super().__init__(position, speed)
        self.at = at
        self.up = up
        self.fov = fov
        self.zdir = self.at.minus(self.position).get_normalized()
        self.xdir = self.up.cross(self.zdir).get_normalized()
        self.ydir = self.zdir.cross(self.xdir).get_normalized()
        self.center = self.zdir.float_mul(1 / tan(((self.fov * pi) / 180) * 0.5))
        self.HEIGHT = height
        self.WIDTH = width
        self.aspect = self.WIDTH / self.HEIGHT
        
    def d(self, i, j):
        """
        Return ray from (i, j) picture coordinates
        
        :return: ray that comes from the camera
        :rtype: vec3
        """
        xr = self.xdir
        yr = self.ydir.float_mul(1 / self.aspect)
        zr = self.zdir.float_mul(1 / tan(0.5 * (self.fov * (pi / 180))))
        
        v1 = xr.float_mul((i + 0.5 - self.WIDTH / 2) / (self.WIDTH / 2))
        v2 = yr.float_mul((j + 0.5 - self.HEIGHT / 2) / (self.HEIGHT / 2))
        v3 = v1.plus(v2)
        vec = zr.plus(v3)
        vec = vec.get_normalized()
        return vec

class Sphere(Element):
    def __init__(self, position, speed, radius, color):
        super().__init__("sphere", position, speed)
        self.radius = radius
        self.color = color
        
    def get_normal(self, point):
        vec = point.minus(self.position)
        vec = vec.get_normalized()
        return vec
 
    def process(self, camera, ray):
        """
        Return nearest point from the collision between ray and self 
        """
        O = camera.center
        co = O.minus(self.position)
        
        a = ray.dot(ray)        
        b = 2 * ray.dot(co)
        c = co.dot(co) - self.radius*self.radius # CAN OPTIMIZE SQUARE BY ADDING COMPUTED CONSTANT IN SPHERE OBJECT
        
        det = b*b - 4*a*c
        
        if (det < 0): # ray does not pass through self
            return -1
        
        t1 = (-b + sqrt(det)) / (2 * a)
        t2 = (-b - sqrt(det)) / (2 * a)
        
        if (t1 <= t2):
            nearest = t1
        else:
            nearest = t2
        return nearest  
    