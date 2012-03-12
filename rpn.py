#!/usr/bin/python
# coding=utf-8

# Base Python File (rpn.py)
# Created: Sun Mar 11 16:13:13 2012
# Version: 1.0
#
# This Python script was developped by François-Xavier Thomas.
# You are free to copy, adapt or modify it.
# If you do so, however, leave my name somewhere in the credits, I'd appreciate it ;)
# 
# (ɔ) François-Xavier Thomas <fx.thomas@gmail.com>

# This script processes an image through periodic+smooth decomposition
# See: http://www.math-info.univ-paris5.fr/~moisan/p+s/ for more details
#
# Usage: python rpn.py sample.png
# Or: from rpn import perdecomp

from numpy import *
from scipy import *
from pylab import *

from sys import argv

def harmonize (t):
  return (t - np.min(t))/(np.max(t) - np.min(t))

def imagesc (i):
  imshow (harmonize (i))

def perdecomp (image):
  # Compute boundary image
  h,w,d = image.shape
  v = zeros (image.shape)
  v[:,0,:] = v[:,0,:] + image[:,0,:] - image[:,w-1,:]
  v[:,w-1,:] = v[:,w-1,:] + image[:,w-1,:] - image[:,0,:]
  v[0,:,:] = v[0,:,:] + image[0,:,:] - image[h-1,:,:]
  v[h-1,:,:] = v[h-1,:,:] + image[h-1,:,:] - image[0,:,:]

  # Compute multiplier
  x = arange (0., 1., 1./w)
  y = arange (0., 1., 1./h)
  xx,yy = meshgrid (x,y)
  multi = 4 - 2.*cos(2*np.pi*xx) - 2.*cos(2*np.pi*yy)
  multi[0,0] = 1.

  # Compute DFT of boundary image
  sh = fftn (v, axes=(-3, -2))

  # Multiply by inverse of multiplier
  sh = sh / multi.reshape((h,w,1))
  sh[0,0,:] = zeros ((d))

  # Then, compute s as the iDFT of sh
  smooth = real (ifftn (sh, axes=(-3, -2)))
  periodic = image - smooth

  return harmonize(periodic),harmonize(smooth)

if __name__ == '__main__':
  # Read image
  image = imread (argv[1])

  # Compute periodic decomposition
  per, smo = perdecomp (image)

  # Show periodic component
  imagesc (per)
  show()

  # Show smooth component
  imagesc (smo)
  show()
