#!/bin/python

# Mandelbrot Set Viewer! By Bob Webb, 2012

import sys
import functools
import time
import pygame
import pickle
import colorsys
from pygame.locals import *

class memoized(object):
   '''Decorator. Caches a function's return value each time it is called.
   If called later with the same arguments, the cached value is returned 
   (not reevaluated).
   '''
   def __init__(self, func):
      self.func = func
      self.cache = {}
      self.reqs = 0
      self.misses = 0
   def __call__(self, *args):
      self.reqs += 1
      try:
         return self.cache[args]
      except KeyError:
         self.misses += 1
         value = self.func(*args)
         self.cache[args] = value
         return value
      except TypeError:
         # uncachable -- for instance, passing a list as an argument.
         # Better to not cache than to blow up entirely.
         return self.func(*args)

def drawData(surface,data,colourScheme):
    '''
    Draws a 2D grid of values ('data') to 'surface' using the given 'colourScheme'
    '''
    for x in range(len(data) - 1):
        for y in range(len(data[x]) - 1):
            surface.set_at((x,y),colourScheme(data[x][y]))
            
    return surface


@memoized
def itersToColour(iters):
    rgb = [int(255*x) for x in colorsys.hls_to_rgb(1.0/(iters+1),0.5,1)]
    return Color(*rgb)

def loadMandelbrot(path):
    dataFile = open(path,'r')
    
    values = []
    lines = dataFile.readlines()
    for line in lines[2:]:
        values.append([int(c) for c in line.split(',')])
    return values

def main():
    inputFileName = sys.argv[1] # the pickle file to be read ^^
    
    data = loadMandelbrot(inputFileName)
    
    pygame.init()
    
    winWidth,winHeight = len(data),len(data[0])
    
    surf = pygame.display.set_mode((winWidth,winHeight))
    pygame.display.set_caption("Mandelbrot set!")
    
    
    drawData(surf,data,itersToColour)
    
    pygame.image.save(surf,"mandelbrot "+time.asctime(time.gmtime())+".png")
    print "Image displayed!"
    
    pygame.display.flip()
    
    while True:
        # loop shite
        # handle input
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.event.post(pygame.event.Event(QUIT))


if __name__== '__main__' : main()
