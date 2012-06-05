#/bin/python

# Mandelbrot pattern generator by Bob Webb, 2012.
# Generates a Mandelbrot pattern as a 2D array of numerical values (number of iterations) that's then pickled.
# I need to get round to pickling metadata as well but not now. Har har.
import sys
import numpy
import pickle
import math


def mandelbrot(c, iters,threshold):
    z = 0
    i = 0
    while i < iters and abs(z) < threshold:
        z = z*z + c
        i += 1
    
    return i

def _pow(z,d):
    if z == 0j:
        return 0
    else:
        return pow(z,d)

def multibrot(c, d, iters,threshold):
    #print "Creating multibrot......"
    z = 0
    i = 0
    while i < iters and abs(z) < threshold:
        z = _pow(z,d) + c
        
        i += 1
    
    return i

def generateMandelbrot(winWidth,winHeight,iterations,threshold):
    outputValues = []
    
    for x in numpy.arange(0,winWidth):
        outputValues.append([])
        for y in numpy.arange(0,winHeight):
            if x % 100 == 0  and y % 100 == 0:
                print x,y
                #print outputValues
            mX = x*(3.0/winWidth) - 2
            mY = y*(2.0/winHeight) - 1
            
            c = complex(mX,mY)
            
            m = mandelbrot(c,iterations,threshold)
            outputValues[x].append(m)
    
    return outputValues

def generateMultibrot(d,winWidth,winHeight,iterations,threshold):
    outputValues = []
    
    for x in numpy.arange(0,winWidth):
        outputValues.append([])
        for y in numpy.arange(0,winHeight):
            if x % 100 == 0  and y % 100 == 0:
                print x,y
                #print outputValues
            mX = x*(3.0/winWidth) - 2
            mY = y*(2.0/winHeight) - 1
            
            c = complex(mX,mY)
            
            m = multibrot(d,c,iterations,threshold)
            outputValues[x].append(m)
    
    return outputValues


def main():
	outputFileName = sys.argv[1]
	
	winWidth = int(sys.argv[2])
	winHeight = int(sys.argv[3])
	
	numIterations = int(sys.argv[4])
	
	threshold = float(sys.argv[5])
	
	try:
		print "trying multibrot..."
		powers = int(sys.argv[6])
		print "got #powers"
		print "Creating a Multibrot set with power:",powers
		values = generateMultibrot(powers,winWidth,winHeight,numIterations,threshold)
	except IndexError:
		values = generateMandelbrot(winWidth,winHeight,numIterations,threshold)
	
	
	#values = generateMandelbrot(winWidth,winHeight,numIterations,threshold)
	
	
	f = open(outputFileName,'w')
	
	
	pickle.dump(values,f)
	
	


if __name__== '__main__' : main()
