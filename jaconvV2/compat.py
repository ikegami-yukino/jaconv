# -*- coding: utf-8 -*-
from sys import version_info

if version_info < (3,):
    # noinspection PyUnresolvedReferences
    from itertools import imap, izip

    # noinspection PyShadowingBuiltins
    map = imap
    zip = izip
else:
    map = map
    zip = zip
