#!/usr/bin/python
# coding=utf-8

# Base Python File (test.py)
# Created: Mon Apr  9 16:33:30 2012
# Version: 1.0
#
# This Python script was developped by François-Xavier Thomas.
# You are free to copy, adapt or modify it.
# If you do so, however, leave my name somewhere in the credits, I'd appreciate it ;)
# 
# (ɔ) François-Xavier Thomas <fx.thomas@gmail.com>

from texture.shortcuts import rpn
from pylab import *
from cv2 import imwrite,imread
import sys
import os

filename,ext = os.path.splitext (sys.argv[1])
sizes = [int(s) for s in sys.argv[2:]]
outnames = ["{0}@{1}x{2}".format(filename, size, ext) for size in sizes]

im = imread (sys.argv[1])
for s,fn in zip(sizes,outnames):
  imwrite (fn, rpn(im, s, s)*255.)
