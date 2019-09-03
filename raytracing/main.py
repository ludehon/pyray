from world_classes import World, Camera, Light, Sphere
from vec3 import Vec3
from renderer import Renderer
from displayer import Displayer

# some optimization are possible. 
# Rendering is too "pixelated", it's maybe due to float/int casts

def main1():
    world = World()    
    
    camera = Camera(Vec3(2, 1, 3), Vec3(0, 0, 0), Vec3(0, 0, 1), Vec3(0, 1, 0), 60, 400, 400)
    
    sphereB = Sphere(Vec3(0, 0.5, 0), Vec3(0, 0, 0), 0.3, Vec3(0, 0, 255))
    sphereR = Sphere(Vec3(0, 0, 1), Vec3(0, 0, 0), 0.3, Vec3(255, 0, 0))
    sphereG = Sphere(Vec3(1, 0, 1), Vec3(0, 0, 0), 0.3, Vec3(0, 255, 0))
    
    light1 = Light(Vec3(3, 2, 5), Vec3(0, 0, 0))
    light2 = Light(Vec3(-2, 1, 1), Vec3(0, 0, 0))
    
    world.add_camera(camera)
    world.add_element(sphereB)
    world.add_element(sphereR)
    world.add_element(sphereG)

    world.add_light(light1)
    # world.add_light(light2)

    r = Renderer(world)
    picture = r.render(0)
    
    d = Displayer()
    d.display(picture)

if __name__ == "__main__":
    main1()