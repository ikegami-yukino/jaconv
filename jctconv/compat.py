# -*- coding: utf-8 -*-
from sys import version_info

if version_info < (3,):
    from itertools import imap, izip
    map = imap
    zip = izip
else:
    map = map
    zip = zip
