

def main1():
    # TODO
    """
    let camera = new Camera({
    position: new Vec3(2, 1, 3),
    // at: new Vec3(0, 0.3, 0),
    at: new Vec3(0, 0, 1),
    up: new Vec3(0, 1, 0),
    fov: 60,
    aspect: 400 / 400
    });

    let world = new World();

    let sphereB = new Sphere({
    position: new Vec3(0, 0.5, 0),
    radius: 0.3,
    color: new Vec3(0, 0, 255)
    });

    let sphereR = new Sphere({
    position: new Vec3(0, 0, 1),
    radius: 0.3,
    color: new Vec3(255, 0, 0)
    });

    let sphereG = new Sphere({
    position: new Vec3(1, 0, 1),
    radius: 0.3,
    color: new Vec3(0, 255, 0)
    });

    let light = new Light({ position: new Vec3(3, 2, 5) });

    let light2 = new Light({ position: new Vec3(-2, 1, 1) });

    world.addCamera(camera);
    world.addElement(sphereB);
    world.addElement(sphereR);
    world.addElement(sphereG)

    world.addLight(light);
    // world.addLight(light2);

    display(render(world));
    """
    pass

if __name__ == "__main__":
    main1()