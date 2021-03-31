"""
    Geometry (2D)
"""

# center of circumscribed circle
def ccc(x, y, z):
    r = 2*(x[0]*(y[1] - z[1]) + y[0]*(z[1] - x[1]) + z[0]*(x[1] - y[1]))

    if r == 0:
        return 10e9, -1, -1

    cx = ((x[0]**2 + x[1]**2)*(y[1] - z[1]) + 
          (y[0]**2 + y[1]**2)*(z[1] - x[1]) + 
          (z[0]**2 + z[1]**2)*(x[1] - y[1]))/r
    cy = ((x[0]**2 + x[1]**2)*(z[0] - y[0]) + 
          (y[0]**2 + y[1]**2)*(x[0] - z[0]) + 
          (z[0]**2 + z[1]**2)*(y[0] - x[0]))/r

    return dis(x, [cx, cy]), cx, cy

# distance between two points
def dis(x, y):
    return ((x[0]-y[0])**2 + (x[1]-y[1])**2)**.5