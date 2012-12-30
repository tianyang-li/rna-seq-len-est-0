#!/usr/bin/env python

#  Copyright (C) 2012 Tianyang Li
#  ty@li-tianyang.com
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License


# may be commented out
import matplotlib
matplotlib.rcParams['backend'] = "Qt4Agg"

import getopt
import sys
from collections import defaultdict

import matplotlib.pyplot as plt

from util import blat_0


def main():
    try:
        opts, _ = getopt.getopt(sys.argv[1:],
                                '',
                                ['read=', 'psl=', 'gtf='])
    except getopt.GetoptError as err:
        print >> sys.stderr, str(err)
        sys.exit(1)
    
    psl_file = None
    
    for opt, arg in opts:
        if opt == '--psl':
            psl_file = arg
    
    if (not psl_file):
        print >> sys.stderr, "missing"
        sys.exit(1)
        
    align_counts = defaultdict(int)
    
    for align in blat_0.read_psl(psl_file):
        align_counts[align.qName] += 1

    plt.figure()
    
    plt.hist([x for x in align_counts.itervalues()], bins=1000)
    
    plt.show()

if __name__ == '__main__':
    main()
    
    
    
