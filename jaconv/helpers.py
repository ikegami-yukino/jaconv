# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .compat import map


def _exclude_ignorechar(ignore, conv_map):
    for character in map(ord, ignore):
        del conv_map[character]
    return conv_map


def _convert(text, conv_map):
    return text.translate(conv_map)


def _translate(text, ignore, conv_map):
    if ignore:
        _conv_map = _exclude_ignorechar(ignore, conv_map.copy())
        return _convert(text, _conv_map)
    return _convert(text, conv_map)
