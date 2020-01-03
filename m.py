# library
from mpl_toolkits.mplot3d import Axes3D
from matplotlib._png import read_png
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import pandas as pd
import seaborn as sns
import sys
import numpy as np
 
img =  mpimg.imread('floorplan.png')


# Get the data (csv file is hosted on the web)
url = 'https://python-graph-gallery.com/wp-content/uploads/volcano.csv'
data = pd.read_csv(url)
 
# Transform it to a long format
df=data.unstack().reset_index()
df.columns=["X","Y","Z"]
 
# And transform the old column name in something numeric
df['X']=pd.Categorical(df['X'])
df['X']=df['X'].cat.codes
 
# Make the plot
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot_trisurf(df['Y'], df['X'], df['Z'], cmap=plt.cm.viridis, linewidth=0.2)


height, width = img.shape[:2]
# 10 is equal length of x and y axises of your surface
stepX, stepY = 80.0/width, 60.0/height

#x, y = np.ogrid[0:80, 0:60]


X1 = np.arange(0, 80, stepX)
Y1 = np.arange(0, 60, stepY)
X1, Y1 = np.meshgrid(X1, Y1)


ax.plot_surface(X1, Y1, np.atleast_2d(2.0), rstride=1, cstride=1, facecolors=img)
plt.show()
 
# to Add a color bar which maps values to colors.
surf=ax.plot_trisurf(df['Y'], df['X'], df['Z'], cmap=plt.cm.viridis, linewidth=0.2)
fig.colorbar( surf, shrink=0.5, aspect=5)
plt.show()
 
# Rotate it
ax.view_init(30, 45)
plt.show()

    
# Other palette
ax.plot_trisurf(df['Y'], df['X'], df['Z'], cmap=plt.cm.jet, linewidth=0.01)
plt.show()




