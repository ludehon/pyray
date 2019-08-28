

class Renderer():
    def __init__(self, world, resolution=(200, 200)):
        self.world = world
        self.resolution = resolution
        
    def render(self, camera):
        """
        :param camera: camera numero
        :type camera: int
        """
        # TODO
        """
        let wcamera = world.cameras[0];

        let picture = [];
        for (let y = 0; y < 400; y++) {
            // 0-400
            for (let x = 00; x <= 400; x++) {
            // let x = 100;
            // let y = 50;
            let ray = d(wcamera, x, y);

            let color = new Vec3();
            let intensity = 0;
            for (let i = 0; i < world.elements.length; i++) {
                if ((world.elements[i].type = "sphere")) {
                let t = process_sphere(wcamera, ray, world.elements[i]);
                // console.log(t)
                if (t != -1) {
                    color = world.elements[i].color;
                }
                for (let j = 0; j < world.lights.length; j++) {
                    let pos = ray_at(ray, wcamera.center, t);
                    let norm = calculateNormals(world.elements[i], pos);
                    // console.log("norm", norm);
                    let vec_lum = vector_minus(world.lights[j].position, pos);

                    angle = vectors_angle(norm, vec_lum);
                    // console.log("angle", angle);

                    if (angle < 90 && angle > -90) {
                    lux = (90 - angle) / 90;
                    } else {
                    lux = 0;
                    }
                    intensity += lux * world.lights[j].intensity;
                }
                }
            }
            if (intensity > 1) {
                intensity = 1;
            }
            // console.log("intensity", intensity)

            let indexPic = y * 400 * 3 + x * 3;
            picture[indexPic] = color.x * intensity;
            picture[indexPic + 1] = color.y * intensity;
            picture[indexPic + 2] = color.z * intensity;
            }
        }
        return picture;
        """
        pass