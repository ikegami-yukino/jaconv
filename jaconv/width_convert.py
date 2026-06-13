# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .conv_table import (
    H2Z_A,
    H2Z_AD,
    H2Z_AK,
    H2Z_ALL,
    H2Z_D,
    H2Z_DK,
    H2Z_K,
    Z2H_A,
    Z2H_AD,
    Z2H_AK,
    Z2H_ALL,
    Z2H_D,
    Z2H_DK,
    Z2H_K,
)
from .helpers import _convert, _exclude_ignorechar


def h2z(text, ignore='', kana=True, ascii=False, digit=False):
    """Convert Half-width (Hankaku) Katakana to Full-width (Zenkaku) Katakana

    Parameters
    ----------
    text : str
        Half-width Katakana string.
    ignore : str, optional
        Characters to be ignored in converting.
    kana : bool, optional
        Either converting Kana or not.
    ascii : bool, optional
        Either converting ascii or not.
    digit : bool, optional
        Either converting digit or not.

    Return
    ------
    str
        Full-width Katakana string.

    Examples
    --------
    >>> print(jaconv.h2z('ﾃｨﾛﾌｨﾅｰﾚ'))
    ティロフィナーレ
    >>> print(jaconv.h2z('ﾃｨﾛﾌｨﾅｰﾚ', ignore='ｨ'))
    テｨロフｨナーレ
    >>> print(jaconv.h2z('abcd', ascii=True))
    ＡＢＣＤ
    >>> print(jaconv.h2z('1234', digit=True))
    １２３４
    """

    def _conv_dakuten(text):
        """Convert Hankaku Dakuten Kana to Zenkaku Dakuten Kana"""
        text = text.replace('ｶﾞ', 'ガ').replace('ｷﾞ', 'ギ')
        text = text.replace('ｸﾞ', 'グ').replace('ｹﾞ', 'ゲ')
        text = text.replace('ｺﾞ', 'ゴ').replace('ｻﾞ', 'ザ')
        text = text.replace('ｼﾞ', 'ジ').replace('ｽﾞ', 'ズ')
        text = text.replace('ｾﾞ', 'ゼ').replace('ｿﾞ', 'ゾ')
        text = text.replace('ﾀﾞ', 'ダ').replace('ﾁﾞ', 'ヂ')
        text = text.replace('ﾂﾞ', 'ヅ').replace('ﾃﾞ', 'デ')
        text = text.replace('ﾄﾞ', 'ド').replace('ﾊﾞ', 'バ')
        text = text.replace('ﾋﾞ', 'ビ').replace('ﾌﾞ', 'ブ')
        text = text.replace('ﾍﾞ', 'ベ').replace('ﾎﾞ', 'ボ')
        text = text.replace('ﾊﾟ', 'パ').replace('ﾋﾟ', 'ピ')
        text = text.replace('ﾌﾟ', 'プ').replace('ﾍﾟ', 'ペ')
        return text.replace('ﾎﾟ', 'ポ').replace('ｳﾞ', 'ヴ')

    if ascii:
        if digit:
            if kana:
                h2z_map = H2Z_ALL
            else:
                h2z_map = H2Z_AD
        elif kana:
            h2z_map = H2Z_AK
        else:
            h2z_map = H2Z_A
    elif digit:
        if kana:
            h2z_map = H2Z_DK
        else:
            h2z_map = H2Z_D
    else:
        if kana:
            h2z_map = H2Z_K
        else:
            h2z_map = {}  # empty
    if kana:
        text = _conv_dakuten(text)
    if ignore:
        h2z_map = _exclude_ignorechar(ignore, h2z_map.copy())
    return _convert(text, h2z_map)


def hankaku2zenkaku(text, ignore='', kana=True, ascii=False, digit=False):
    """An alias of h2z"""
    return h2z(text, ignore, kana, ascii, digit)


def han2zen(text, ignore='', kana=True, ascii=False, digit=False):
    """An alias of h2z"""
    return h2z(text, ignore, kana, ascii, digit)


def z2h(text, ignore='', kana=True, ascii=False, digit=False):
    """Convert Full-width (Zenkaku) Katakana to Half-width (Hankaku) Katakana

    Parameters
    ----------
    text : str
        Full-width Katakana string.
    ignore : str, optional
        Characters to be ignored in converting.
    kana : bool, optional
        Either converting Kana or not.
    ascii : bool, optional
        Either converting ascii or not.
    digit : bool, optional
        Either converting digit or not.

    Return
    ------
    str
        Half-width Katakana string.

    Examples
    --------
    >>> print(jaconv.z2h('ティロフィナーレ'))
    ﾃｨﾛﾌｨﾅｰﾚ
    >>> print(jaconv.z2h('ティロフィナーレ', ignore='ィ'))
    ﾃィﾛﾌィﾅｰﾚ
    >>> print(jaconv.z2h('ＡＢＣＤ', ascii=True))
    abcd
    >>> print(jaconv.z2h('１２３４', digit=True))
    1234
    """
    if ascii:
        if digit:
            if kana:
                z2h_map = Z2H_ALL
            else:
                z2h_map = Z2H_AD
        elif kana:
            z2h_map = Z2H_AK
        else:
            z2h_map = Z2H_A
    elif digit:
        if kana:
            z2h_map = Z2H_DK
        else:
            z2h_map = Z2H_D
    else:
        if kana:
            z2h_map = Z2H_K
        else:
            z2h_map = {}  # empty
    if ignore:
        z2h_map = _exclude_ignorechar(ignore, z2h_map.copy())
    return _convert(text, z2h_map)


def zenkaku2hankaku(text, ignore='', kana=True, ascii=False, digit=False):
    """An alias of z2h"""
    return z2h(text, ignore, kana, ascii, digit)


def zen2han(text, ignore='', kana=True, ascii=False, digit=False):
    """An alias of z2h"""
    return z2h(text, ignore, kana, ascii, digit)
