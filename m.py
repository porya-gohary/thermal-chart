# library
from mpl_toolkits.mplot3d import Axes3D
from matplotlib._png import read_png
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import pandas as pd
import seaborn as sns
import sys
import numpy as np
 
img =  mpimg.imread('floorplan2.png')
#img = cv2.imread('floorplan-n.png')

data = pd.read_csv('input.csv')
 
# Transform it to a long format
df=data.unstack().reset_index()
df.columns=["X","Y","Z"]
 
# And transform the old column name in something numeric
df['X']=pd.Categorical(df['X'])
df['X']=df['X'].cat.codes
 
# Make the plot
fig = plt.figure()
ax = fig.gca(projection='3d')


ax.set_zlim3d(45, 80)
surf=ax.plot_trisurf(df['Y'], df['X'], df['Z'], cmap=plt.cm.jet, linewidth=0.2, vmin=60, vmax=80)


height, width = img.shape[:2]
# 10 is equal length of x and y axises of your surface
stepX, stepY = 64.0/width, 64.0/height

#x, y = np.ogrid[0:80, 0:60]


X1 = np.arange(0, 64, stepX)
Y1 = np.arange(0, 64, stepY)
X1, Y1 = np.meshgrid(X1, Y1)


ax.plot_surface(X1, Y1, np.atleast_2d(47.0), rstride=1, cstride=1, facecolors=img)
#plt.show()

ax.set_yticklabels([])
ax.set_xticklabels([])

# to Add a color bar which maps values to colors.
   
#surf=ax.plot_trisurf(df['Y'], df['X'], df['Z'], cmap=plt.cm.jet, linewidth=0.2)
cb=fig.colorbar( surf, shrink=0.6, aspect=10,fraction=0.046, pad=0.04)
#cb.ax.set_clim(vmin=0, vmax=15)
plt.show()
# Rotate it
#ax.view_init(30, 45)
#plt.show()


# Other palette
#ax.plot_trisurf(df['Y'], df['X'], df['Z'], cmap=plt.cm.jet, linewidth=0.01)

#plt.show()




