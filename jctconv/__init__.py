from . import jctconv

VERSION = (0, 1)
__version__ = '0.1'
__all__ = ['hira2kata', 'hira2hkata', 'kata2hira', 'h2z', 'z2h', 'normalize']

hira2kata = jctconv.hira2kata
hira2hkata = jctconv.hira2hkata
kata2hira = jctconv.kata2hira
h2z = jctconv.h2z
z2h = jctconv.z2h
normalize = jctconv.normalize
