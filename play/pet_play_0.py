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

import getopt
import sys

from util import blat_0

def main():
    try:
        opts, _ = getopt.getopt(sys.argv[1:],
                                '',
                                ['read1', 'read2',
                                 'psl1', 'psl2', 'gtf'])
    except getopt.GetoptError as err:
        print >> sys.stderr, str(err)
        sys.exit(1)


