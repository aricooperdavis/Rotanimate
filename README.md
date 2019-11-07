# Rotanimate
A Python library/function that saves frames from a rotating 3D matplotlib plot so that you can animate them using [ImageMagick](https://www.imagemagick.org/script/command-line-processing.php)/[Gifsicle](https://www.lcdf.org/gifsicle/)/[ImageJ](https://imagej.nih.gov/ij/docs/guide/146-8.html) or your tool of choice.

## Motivation
I wished to [explain a linear regression](https://stackoverflow.com/a/58736858/6144626) using an [animated 3d matplotlib plot](https://gist.github.com/aricooperdavis/c658fc1c5d9bdc5b50ec94602328073b#gistcomment-3076177) but couldn't find a super simple tool to do the job until I found [Zulko's "The Sugar High" blogpost](https://zulko.wordpress.com/2012/09/29/animate-your-3d-plots-with-pythons-matplotlib/). It was coded in Python 2.7 and was a little too bulky for my liking, so I've modernised it and cut it down to the bare essentials.

## Usage
Place the `rotanimate.py` file in the same directory as your python script so that you can `import rotanimate` then use as follows:

```python
# The usual imports
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import axes3d
import rotanimate

# Setup your 3D plot as normal
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
X, Y, Z = axes3d.get_test_data()
ax.plot_surface(X, Y, Z, cmap=plt.cm.Set1)

# Setup rotanimate
plt.axis('off') # remove axes for visual appeal
angles = np.linspace(0, 360, 31)[:-1] # Generate viewing angles
rotanimate.rotanimate(ax, angles)
```

Or, because the function is only 19 lines long, just copy and paste the function into your code and use it directly - just remember to `import os`.

Either way, the output is a new directory `~/Frames/` containing sequentially numbered `angle_*.jpeg`s for your enjoyment.

## Arguments
You can pass the function some keyword arguments:
- `elevation`: the viewing elevation.
- `width`: the width (in inches) of the resulting plot.
- `height`: the height (in inches) of the resulting plot.

## Example
Calling the file from the command line generates:

![Screenshot of resultant directory](https://raw.githubusercontent.com/aricooperdavis/Rotanimate/master/directory_demo.jpeg)

And after processing (I used ImageJ) the result is an animated rotating 3d matplot lib plot:

![Animated example plot](https://raw.githubusercontent.com/aricooperdavis/Rotanimate/master/animated_demo.gif)

## Credits

*Initial code and design shamelessly stolen from [Zulko's "The Sugar High" blog](https://zulko.wordpress.com/2012/09/29/animate-your-3d-plots-with-pythons-matplotlib/)*.
