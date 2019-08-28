from math import tan, pi

from vec3 import Vec3

class World():
    def __init__(self, elements=[], lights=[], cameras=[]):
        self.elements = elements
        self.lights = lights
        self.cameras = cameras

    def add_element(self, e):
        self.elements.add(e)
    
    def add_lights(self, l):
        self.lights.add(l)
        
    def add_camera(self, c):
        self.cameras.add(c)
        
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
    def __init__(self, position, speed, at, up, fov, aspect):
        super().__init__(position, speed)
        self.at = at
        self.up = up
        self.fov = fov
        self.aspect = aspect
        self.zdir = self.at.minus(self.position).get_normalized()
        self.xdir = self.up.cross(self.zdir).get_normalized()
        self.ydir = self.zdir.cross(self.xdir).get_normalized()
        self.center = self.zdir.float_mul(1 / tan(((self.fov * pi) / 180) * 0.5))
        
    def d(self, i, j):
        # TODO
        """
            let xr = wcamera.xdir;
            let yr = vector_float_mul(wcamera.ydir, 1 / wcamera.aspect);
            let zr = vector_float_mul(
                wcamera.zdir,
                1 / Math.tan(0.5 * (wcamera.fov * (Math.PI / 180)))
            );
            let vec = vector_normalized(
                vector_add(
                zr,
                vector_add(
                    vector_float_mul(xr, (i + 0.5 - WIDTH / 2) / (WIDTH / 2)),
                    vector_float_mul(yr, (j + 0.5 - HEIGHT / 2) / (HEIGHT / 2))
                )
                )
            );
            // console.log("i", i);
            // console.log("vec", vec);
            return vec;
        """
        pass

class Sphere(Element):
    def __init__(self, position, speed, radius, color):
        super().__init__("sphere", position, speed)
        self.radius = radius
        self.color = color
        
    def get_normal(self, point):
        vec = point.minus(self.position)
        vec = vec.get_norm()
        return vec
 
    def process(self, camera, ray):
        """
        Return nearest point from the collision between ray and self 
        """
        # TODO
        """
            let O = wcamera.center;

            // console.log("ray", ray);
            a = vector_dot(ray, ray);

            let co = vector_minus(O, sphere.position);
            b = 2 * vector_dot(ray, co);

            c = vector_dot(co, co) - sphere.radius * sphere.radius;

            det = b * b - 4 * a * c;

            // console.log("det", det);

            if (det < 0) {
                return -1;
            }

            t1 = (-b + Math.sqrt(det)) / (2 * a);
            t2 = (-b - Math.sqrt(det)) / (2 * a);
            // console.log("t1", t1);
            // console.log("t2", t2);

            let nearest;
            if (t1 <= t2) {
                nearest = t1;
            } else {
                nearest = t2;
            }
            return nearest;
        """
        pass 

def ray_at(ray, O, t):
    """
    Return position from the vector "ray" and distance "t" and origin "O"
    """
    point = ray.float_mul(t).add(O)
    return point