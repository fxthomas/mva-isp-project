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

from numpy import zeros,real,arange,cos,sin,min,max,meshgrid,pi
from numpy.fft import ifftn,fftn

def harmonize (t):
  return (t - min(t))/(max(t) - min(t))

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
  multi = 4 - 2.*cos(2*pi*xx) - 2.*cos(2*pi*yy)
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

def tile (a, ni=2, nj=2):
  nshape = list(a.shape)
  nshape[0] = nshape[0] * ni
  nshape[1] = nshape[1] * nj

  ret = zeros (nshape, dtype=a.dtype)
  for i in range(ni):
    for j in range(nj):
      ret[i*a.shape[0]:(i+1)*a.shape[0], j*a.shape[1]:(j+1)*a.shape[1]] = a

  return ret
