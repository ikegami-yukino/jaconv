# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import warnings

from .conv_table import (
    H2HK_TABLE,
    H2K_TABLE,
    K2H_TABLE,
    SMALL_KANA2NORMAL_KANA,
)
from .helpers import _translate


def hira2kata(text, ignore=''):
    """Convert Hiragana to Full-width (Zenkaku) Katakana.

    Parameters
    ----------
    text : str
        Hiragana string.
    ignore : str, optional
        Characters to be ignored in converting.

    Return
    ------
    str
        Katakana string.

    Examples
    --------
    >>> print(jaconv.hira2kata('ともえまみ'))
    トモエマミ
    >>> print(jaconv.hira2kata('まどまぎ', ignore='ど'))
    マどマギ
    """
    return _translate(text, ignore, H2K_TABLE)


def hira2hkata(text, ignore=''):
    """Convert Hiragana to Half-width (Hankaku) Katakana

    Parameters
    ----------
    text : str
        Hiragana string.
    ignore : str, optional
        Characters to be ignored in converting.

    Return
    ------
    str
        Half-width Katakana string.

    Examples
    --------
    >>> print(jaconv.hira2hkata('ともえまみ'))
    ﾄﾓｴﾏﾐ
    >>> print(jaconv.hira2hkata('ともえまみ', ignore='み'))
    ﾄﾓｴﾏみ
    """
    return _translate(text, ignore, H2HK_TABLE)


def kata2hira(text, ignore=''):
    """Convert Full-width Katakana to Hiragana

    Parameters
    ----------
    text : str
        Full-width Katakana string.
    ignore : str, optional
        Characters to be ignored in converting.

    Return
    ------
    str
        Hiragana string.

    Examples
    --------
    >>> print(jaconv.kata2hira('巴マミ'))
    巴まみ
    >>> print(jaconv.kata2hira('マミサン', ignore='ン'))
    まみさン
    """
    return _translate(text, ignore, K2H_TABLE)


def enlargesmallkana(text, ignore=''):
    warn_msg = (
        '`enlargesmallkana` is deprecated and will be removed in future versions.'
        ' Use `enlarge_smallkana` instead.'
    )
    warnings.warn(warn_msg, UserWarning)
    return enlarge_smallkana(text, ignore)


def enlarge_smallkana(text, ignore=''):
    """Convert small Hiragana or Katakana to normal size

    Parameters
    ----------
    text : str
        Full-width Hiragana or Katakana string.
    ignore : str, optional
        Characters to be ignored in converting.

    Return
    ------
    str
        Hiragana or Katakana string, enlarged small Kana

    Examples
    --------
    >>> print(jaconv.enlargesmallkana('さくらきょうこ'))
    さくらきようこ
    >>> print(jaconv.enlargesmallkana('キュゥべえ'))
    キユウべえ
    """
    return _translate(text, ignore, SMALL_KANA2NORMAL_KANA)
