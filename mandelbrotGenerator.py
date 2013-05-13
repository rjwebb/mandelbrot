#/bin/python

# Mandelbrot pattern generator by Bob Webb, 2012.
# Generates a Mandelbrot pattern as a 2D array of numerical values (number of iterations) that's then pickled.
# I need to get round to pickling metadata as well but not now. Har har.
import sys
import numpy
import pickle
import math
import functools

def _pow(z,d):
    if z == 0j:
        return 0
    else:
        if d == 2:
            return z * z
        else:
            return pow(z,d)

def mandelbrot(c,iters,threshold,d):
    z = 0
    i = 0
    while i < iters and abs(z) < threshold:
        z = _pow(z,d) + c
        i += 1
    return i

def generateFractal(func, winWidth,winHeight):
    outputValues = []
    
    for x in numpy.arange(0,winWidth):
        outputValues.append([])
        for y in numpy.arange(0,winHeight):
            if x % 100 == 0  and y % 100 == 0:
                print x,y
            mX = x*(3.0/winWidth) - 2
            mY = y*(2.0/winHeight) - 1
            
            c = complex(mX,mY)
            
            m = func(c)
            outputValues[x].append(m)
    
    return outputValues

def generateMandelbrot(winWidth,winHeight,iterations,threshold,d=2):
    frac = functools.partial(mandelbrot,d=d,iters=iterations,threshold=threshold)
    return generateFractal(frac,winWidth,winHeight)

def fmt_values(values):
    out = ""

    numrows = len(values)
    numcols = len(values[0])

    out += str(numrows)+"\n"
    out += str(numcols)+"\n"

    for line in values:
        out += ",".join(str(c) for c in line) + "\n"

    return out

def writeToFile(s,path):
    f = open(path,'w')
    f.write(s)
    f.close()

def main():
    outputFileName = sys.argv[1]
    
    winWidth = int(sys.argv[2])
    winHeight = int(sys.argv[3])
    
    numIterations = int(sys.argv[4])
    
    threshold = float(sys.argv[5])
    
    try:
        powers = int(sys.argv[6])
        values = generateMandelbrot(winWidth,winHeight,numIterations,threshold,powers)
    except IndexError:
        values = generateMandelbrot(winWidth,winHeight,numIterations,threshold)
    
    writeToFile(fmt_values(values), outputFileName)

if __name__== '__main__' : main()
