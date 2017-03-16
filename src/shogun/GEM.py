# -*- coding: utf-8 -*-

# import all Shogun classes
from modshogun import *

from matplotlib.patches import Ellipse

# a tool for visualisation
def get_gaussian_ellipse_artist(mean, cov, nstd=1.96, color="red", linewidth=3):
    """
    Returns an ellipse artist for nstd times the standard deviation of this
    Gaussian, specified by mean and covariance
    """
    # compute eigenvalues (ordered)
    vals, vecs = eigh(cov)
    order = vals.argsort()[::-1]
    vals, vecs = vals[order], vecs[:, order]
    
    theta = numpy.degrees(arctan2(*vecs[:, 0][::-1]))

    # width and height are "full" widths, not radius
    width, height = 2 * nstd * sqrt(vals)
    e = Ellipse(xy=mean, width=width, height=height, angle=theta, \
               edgecolor=color, fill=False, linewidth=linewidth)
    
    return e
    
# create mixture of three Gaussians
num_components=3
num_max_samples=100
gmm=GMM(num_components)

dimension=2

# set means (TODO interface should be to construct mixture from individuals with set parameters)
means=zeros((num_components, dimension))
means[0]=[-5.0, -4.0]
means[1]=[7.0, 3.0]
means[2]=[0, 0.]
[gmm.set_nth_mean(means[i], i) for i in range(num_components)]

# set covariances
covs=zeros((num_components, dimension, dimension))
covs[0]=array([[2, 1.3],[.6, 3]])
covs[1]=array([[1.3, -0.8],[-0.8, 1.3]])
covs[2]=array([[2.5, .8],[0.8, 2.5]])
[gmm.set_nth_cov(covs[i],i) for i in range(num_components)]

# set mixture coefficients, these have to sum to one (TODO these should be initialised automatically)
weights=array([0.5, 0.3, 0.2])
gmm.set_coef(weights)

  # now sample from each component seperately first, the from the joint model
hold(True)
colors=["red", "green", "blue"]
for i in range(num_components):
    # draw a number of samples from current component and plot
    num_samples=int(rand()*num_max_samples)+1
    
    # emulate sampling from one component (TODO fix interface of GMM to handle this)
    w=zeros(num_components)
    w[i]=1.
    gmm.set_coef(w)
    
    # sample and plot (TODO fix interface to have loop within)
    X=array([gmm.sample() for _ in range(num_samples)])
    plot(X[:,0], X[:,1], "o", color=colors[i])
    
    # draw 95% elipsoid for current component
    gca().add_artist(get_gaussian_ellipse_artist(means[i], covs[i], color=colors[i]))
    
hold(False)
_=title("%dD Gaussian Mixture Model with %d components" % (dimension, num_components))
 
# since we used a hack to sample from each component
gmm.set_coef(weights) 