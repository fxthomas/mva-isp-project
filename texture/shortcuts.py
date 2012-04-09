#!/usr/bin/python
# coding=utf-8

# Base Python File (shortcuts.py)
# Created: Mon Apr  9 16:28:22 2012
# Version: 1.0
#
# This Python script was developped by François-Xavier Thomas.
# You are free to copy, adapt or modify it.
# If you do so, however, leave my name somewhere in the credits, I'd appreciate it ;)
# 
# (ɔ) François-Xavier Thomas <fx.thomas@gmail.com>

import texturize,randomize
from texturize import perdecomp,harmonize,tile

def rpn (sample, ni=2, nj=2):
  p,_ = perdecomp (sample)
  return tile (p, ni, nj, randomize.rpn)
