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


import sys
import getopt
from random import randint, choice


def main():
    l, r, n = None, None, None
    out_pref = None
    
    try:
        opts, _ = getopt.getopt(sys.argv[1:], 'l:r:n:p:')
    except getopt.GetoptError as err:
        print >> sys.stderr, str(err)
        sys.exit(1)
        
    for opt, arg in opts:
        if opt == '-l':
            # subject seq length
            l = int(arg)
        if opt == '-r':
            # read seq length
            r = int(arg)
        if opt == '-n':
            # # of reads
            n = int(arg)
        if opt == '-p':
            # output file prefix
            out_pref = arg
    
    if (not l 
        or not r 
        or not n
        or not out_pref):
        print >> sys.stderr, "missing"
        sys.exit(1)
    
    s_seq = "".join(choice("ACGT") for _ in xrange(l))
    
    with open("%s_s.fasta", 'w') as fout_s_seq:
        fout_s_seq.write(">s\n%s\n" % s_seq)
        
    with open("%s_q.fasta", 'w') as fout_q_seq:
        for _ in xrange(n):
            start_pos = randint(0, l - r)
            fout_q_seq.write(">%d.%d\n%s\n" 
                             % (start_pos,
                                start_pos + r,
                                s_seq[start_pos, start_pos + r]))


if __name__ == '__main__':
    main()

