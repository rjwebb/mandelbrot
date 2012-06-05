mandelbrot
==========

Mandelbrot fractal generator and viewer.

## Mandelbrot Generator
To create a normal Mandelbrot fractal, use this command:

	python ./mandelbrotGenerator.py [output filename] [width of graph] [height of graph] [max number of iterations for mandelbrot function] [threshold of mandelbrot function]

To create a [Multibrot](https://en.wikipedia.org/wiki/Multibrot_set) fractal, use this command:

	python ./mandelbrotGenerator.py [output filename] [width of graph] [height of graph] [max number of iterations for mandelbrot function] [threshold of mandelbrot function] [index]

Both of these scripts will output a 2D array of the values using the [pickle](http://docs.python.org/library/pickle.html) algorithm.

This can then be opened and displayed by the Mandelbrot Viewer script.

## Mandelbrot Viewer

	python ./mandelbrotViewer.py [input file]

This script displays a representation of the data created by the previous script on screen using Pygame(SDL), and saves a copy onto disk which is timestamped.
