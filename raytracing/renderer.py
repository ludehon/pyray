import numpy as np
from vec3 import Vec3


class Renderer():
    def __init__(self, world):
        self.world = world
        
    def render(self, camera_num):
        """
        :param camera_num: camera numero
        :type camera_num: int
        """
        wcamera = self.world.cameras[camera_num]
        picture = np.zeros((wcamera.HEIGHT, wcamera.WIDTH, 3))
        
        for x in range(wcamera.WIDTH):
            for y in range(wcamera.HEIGHT):
                ray = wcamera.d(x, y)
                color = Vec3()
                intensity = 0
                
                for e in self.world.elements:
                    if (e.type == "sphere"):
                        t = e.process(wcamera, ray)
                        
                        if (t != -1):
                            color = e.color
                        
                        for l in self.world.lights:
                            pos = ray.ray_at(wcamera.center, t)
                            normal = e.get_normal(pos)
                            vec_lum = l.position.minus(pos)
                            angle = normal.get_angle(vec_lum)
                            if (angle < 90 and angle > -90):
                                lux = (90 - angle) / 90
                            else:
                                lux = 0
                            
                            intensity = intensity + (lux * l.intensity)  
                            
                if (intensity > 1):
                    intensity = 1
                
                picture[x][y][0] = color.x * intensity
                picture[x][y][1] = color.y * intensity
                picture[x][y][2] = color.z * intensity
                
        return picture
