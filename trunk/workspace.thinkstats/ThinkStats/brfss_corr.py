"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2010 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

import math
import matplotlib
import matplotlib.pyplot as pyplot
import random
import sys

import brfss
import brfss_scatter
import correlation
import myplot


"""
Results:

Number of records: 414509
Pearson correlation (weights): 0.508736478974
Pearson correlation (log weights): 0.531728260599
Spearman correlation (weights): 0.541529498192

The Pearson correlation is low because of the effect of outliers.
Either of the others is a reasonable choice, but in this case because
we know the distribution of weights is lognormal, the log transform
might be the best choice.

If we didn't know what transform to use, I would be more inclined to
use Spearman's correlation, but I am less comfortable with it because
MapToRanks to ranks is an information-losing transform, and Log is
not.

"""

def Log(t):
    """Computes the log of a sequence."""
    return [math.log(x) for x in t]


def ComputeCorrelations():
    resp = brfss_scatter.Respondents()
    resp.ReadRecords()
    print 'Number of records:', len(resp.records)

    heights, weights = resp.GetHeightWeight()
    pearson = correlation.Corr(heights, weights)
    print 'Pearson correlation (weights):', pearson

    log_weights = Log(weights)
    pearson = correlation.Corr(heights, log_weights)
    print 'Pearson correlation (log weights):', pearson

    spearman = correlation.SpearmanCorr(heights, weights)
    print 'Spearman correlation (weights):', spearman


def main(name):
    ComputeCorrelations()


if __name__ == '__main__':
    main(*sys.argv)