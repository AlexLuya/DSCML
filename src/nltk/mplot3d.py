import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

sigmoid = lambda x,y: 1/sqrt(1 + 2*exp(20.1-27*(x**2 + y**2)))
ts = arange(0,1.001,.01)
fig = plt.figure()
ax = fig.gca(projection='3d')
(XX,YY) = meshgrid(ts,ts)
ZZ = vectorize(sigmoid)(XX,YY)
ax.plot_surface(XX,YY,ZZ,rstride = 5, cstride = 5, cmap = cm.jet)