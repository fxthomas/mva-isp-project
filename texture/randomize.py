#!/usr/bin/python
# coding=utf-8

# Base Python File (rpn.py)
# Created: Mon Apr  9 16:03:21 2012
# Version: 1.0
#
# This Python script was developped by François-Xavier Thomas.
# You are free to copy, adapt or modify it.
# If you do so, however, leave my name somewhere in the credits, I'd appreciate it ;)
# 
# (ɔ) François-Xavier Thomas <fx.thomas@gmail.com>

import numpy as np

# Return basic 
def rpn (sample):
  # Compute the Fourier transform of the sample
  fsample = np.fft.fftn (sample, axes=(0,1))

  # Multiply each channel by the same randomized phase
  mult = np.random.rand (sample.shape[0], sample.shape[1])
  fsampler = fsample * np.exp((0+1j) * (2*np.pi*mult.reshape(sample.shape[0], sample.shape[1],1) - np.pi))

  # The inverse FFT is a randomized texture based on the sample
  return np.abs(np.fft.ifftn (fsampler, axes=(0,1)))
