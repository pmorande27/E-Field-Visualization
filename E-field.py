import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
plt.rcParams["figure.figsize"] = (10, 10)

class Charge():
    def __init__(self,charge,pos_x,pos_y):
        self.charge = charge
        self.pos_x = pos_x
        self.pos_y = pos_y

def E(charge, x, y):
    """Return the electric field vector E=(Ex,Ey) due to charge q at r0."""
    den = np.hypot(x-charge.pos_x, y-charge.pos_y)**3
    return charge.charge * (x - charge.pos_x) / den, charge.charge * (y - charge.pos_y) / den
def efield_dist(distribution, X, Y):
    
    Ex, Ey = np.zeros((ny, nx)), np.zeros((ny, nx))
    for charge in distribution:
        ex, ey = E(charge, X, Y)
        Ex += ex
        Ey += ey
    return Ex, Ey
def plot(distribution):
    nx, ny = 100, 100
    x = np.linspace(-10, 10, nx)
    y = np.linspace(-10, 10, ny)
    X, Y = np.meshgrid(x, y)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    Ex, Ey = efield_dist(distribution)
    # Plot the streamlines with an appropriate colormap and arrow style
    color = 2 * np.log(np.hypot(Ex, Ey))
    ax.streamplot(x, y, Ex, Ey, color=color, linewidth=1, cmap=plt.cm.inferno,
                density=4, arrowstyle='->', arrowsize=1.5)

    # Add filled circles for the charges themselves
    charge_colors = {True: '#aa0000', False: '#0000aa'}
    for charge in distribution:
        ax.add_artist(Circle((charge.pos_x,charge.pos_y), 0.05, color=charge_colors[charge.charge>0]))

    ax.set_xlabel('$x$')
    ax.set_ylabel('$y$')
    ax.set_xlim(-10,10)
    ax.set_ylim(-10,10)
    ax.set_aspect('equal')
    plt.show()