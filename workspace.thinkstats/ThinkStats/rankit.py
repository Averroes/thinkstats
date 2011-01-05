"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2010 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

import random
import thinkstats
import myplot
import matplotlib.pyplot as pyplot

def Sample(n=6):
    t = [random.normalvariate(0.0, 1.0) for i in range(n)]
    t.sort()
    return t


def Samples(n=6, m=1000):
    t = [Sample(n) for i in range(m)]
    return t


def EstimateRankits(n=6, m=1000):
    t = Samples(n, m)
    t = zip(*t)
    means = [thinkstats.Mean(x) for x in t]
    return means


def MakeNormalPlot(ys, root=None, lineoptions={}, **options):
    """Makes a normal probability plot.
    
    Args:
        ys: sequence of values
        lineoptions: dictionary of options for pyplot.plot        
        options: dictionary of options for myplot.Plot
    """
    # TODO: when n is small, generate a larger sample and desample
    n = len(ys)
    ys.sort()
    xs = [random.normalvariate(0.0, 1.0) for i in range(n)]
    xs.sort()
    
    pyplot.clf()
    pyplot.plot(sorted(xs), sorted(ys), 'x', markersize=2, **lineoptions)
 
    myplot.Plot(root,
                xlabel = 'Standard normal values',
                legend=False,
                **options)
    

def main():
    means = EstimateRankits()
    print means
    

if __name__ == "__main__":
    main()
