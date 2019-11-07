"""
Python 3 module that facilitates the generation of rotating animations of
3D Matplotlib figures. Code and idea shamelessly stolen from Zulko.
"""

import os
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import numpy as np

def rotanimate(ax, angles, elevation=None, width=8, height=5):
    """
    Makes jpeg pictures of the given 3d ax, with different angles.
    Args:
        ax (3D axis): the ax
        angles (list): the list of angles (in degree) under which to
                       take the picture.
        width,height (float): size, in inches, of the output images.
    """

    ax.figure.set_size_inches(width, height)
    if not os.path.isdir('./Frames'): os.mkdir('./Frames')

    for i, angle in enumerate(angles):
        ax.view_init(elev=elevation, azim=angle)
        fname = '{}_{}.jpeg'.format('angle', i)
        ax.figure.savefig('./Frames/{}'.format(fname))

    return

# Example usage

if __name__ == '__main__':

    # Setup your 3D plot as normal
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    X, Y, Z = axes3d.get_test_data()
    ax.plot_surface(X, Y, Z, cmap=plt.cm.Set1)

    # Setup rotanimate
    plt.axis('off') # remove axes for visual appeal
    angles = np.linspace(0, 360, 31)[:-1] # Generate viewing angles
    rotanimate(ax, angles)
