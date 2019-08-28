# define vector class and functions here

class Vec3():
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
    
    def dot(self, v2):
        print("TODO")
        return Vec3(0, 0, 0)

    
    

"""
let vector_minus = (v1, v2) => {
      let x = v1.x - v2.x;
      let y = v1.y - v2.y;
      let z = v1.z - v2.z;

      return new Vec3(x, y, z);
    };
    let vector_add = (v1, v2) => {
      let x = v1.x + v2.x;
      let y = v1.y + v2.y;
      let z = v1.z + v2.z;

      return new Vec3(x, y, z);
    };
    let vector_float_mul = (v, f) => {
      let x = v.x * f;
      let y = v.y * f;
      let z = v.z * f;

      return new Vec3(x, y, z);
    };
    let vector_cross = (v1, v2) => {
      let x = v1.y * v2.z - v1.z * v2.y;
      let y = v1.z * v2.x - v1.x * v2.z;
      let z = v1.x * v2.y - v1.y * v2.x;

      return new Vec3(x, y, z);
    };
    let vector_norm = v => {
      return Math.sqrt(Math.pow(v.x, 2) + Math.pow(v.y, 2) + Math.pow(v.z, 2));
    };
    //vecteur au carré
    let vector_dot = (v1, v2) => {
      return v1.x * v2.x + v1.y * v2.y + v1.z * v2.z;
    };

    let vector_normalized = v => {
      let norm = vector_norm(v);
      let x = v.x / norm;
      let y = v.y / norm;
      let z = v.z / norm;

      return new Vec3(x, y, z);
    };

    let vectors_angle = (vec1, vec2) => {
      norm1 = vector_norm(vec1);

      norm2 = vector_norm(vec2);
      dot = vector_dot(vec1, vec2);

      cos = dot / (norm1 * norm2);
      angle = (Math.acos(cos) * 180) / Math.PI;
      return angle;
    };

    class Vec3 {
      constructor(x = 0, y = 0, z = 0) {
        this.x = x;
        this.y = y;
        this.z = z;
      }
    }
"""