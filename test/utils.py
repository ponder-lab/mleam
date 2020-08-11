import numpy as np


def rotation_matrix(n, alpha):
    """
    n: (3,) rotation axis. Input vector is normalized in the function.
    alpha: angle in radians.

    output: (3x3) rotation matrix
    """
    # From https://de.wikipedia.org/wiki/Drehmatrix#Drehmatrizen_des_Raumes
    n = n/np.linalg.norm(n)
    cos_a = np.cos(alpha)
    sin_a = np.sin(alpha)
    # (1 - cos(a))
    foo = 1 - cos_a
    R = np.array([[n[0]*n[0]*foo + cos_a,
                   n[0]*n[1]*foo - n[2]*sin_a,
                   n[0]*n[2]*foo + n[1]*sin_a],
                  [n[1]*n[0]*foo + n[2]*sin_a,
                   n[1]*n[1]*foo + cos_a,
                   n[1]*n[2]*foo - n[0]*sin_a],
                  [n[2]*n[0]*foo - n[1]*sin_a,
                   n[2]*n[1]*foo + n[0]*sin_a,
                   n[2]*n[2]*foo + cos_a]])
    return R
