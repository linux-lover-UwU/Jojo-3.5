import global_variable
from math import *

def mul_vec_mat(vec:list[float], mat:list[list[float]]) -> list[float]:
    return = [mat[i][0]*vec[0] + mat[i][1]*vec[1] + mat[i][2]*vec[2] + mat[i][3]*vec[3] for i in range(4)]

def normalize(vec:list[float]) -> list[float]:


def create_view_mat() -> list[list[float]]:
    eye = [global_variable.position_3d[0], 0, global_variable.position_3d[1]]
    f = [cos(global_variable.camera_rotation[0]) * cos(global_variable.camera_rotation[1]),
              sin(global_variable.camera_rotation[1]),
              sin(global_variable.camera_rotation[0]) * cos(global_variable.camera_rotation[1])]
    r = [sin(global_variable.camera_rotation[0] - PI/2.0),0,cos(global_variable.camera_rotation[0] - PI/2.0)]
    up = [r[1] * f[2] - r[2] * f[1],
          r[2] * f[0] - r[0] * f[2],
          r[0] * f[1] - r[1] * f[0]
          ]
    t = [r[0] * global_variable.position_3d[0] + r[1] * global_variable.position_3d[1] + r[2] * global_variable.position_3d[2],
        r[0] * global_variable.position_3d[0] + r[1] * global_variable.position_3d[1] + r[2] * global_variable.position_3d[2]
        f[0] * global_variable.position_3d[0] + f[1] * global_variable.position_3d[1] + f[2] * global_variable.position_3d[2]
         ]

    return [[r[0], up[0], -f[0], 0],
            [r[1], up[1], -f[1], 0],
            [r[2], up[2], -f[2], 0],
            [t[0], t[0], t[0], 1]]
