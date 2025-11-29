from sys import version_info

if version_info < (3,):
    from itertools import imap, izip  # type: ignore[attr-defined]
    map = imap
    zip = izip
    from codecs import open
    open = open
else:
    map = map
    zip = zip
