# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import jaconv
"""jaconv

This module provides Japanese and ASCII character interconverting between
Hiragana and full-/half-width Katakana/ASCII characters.

Author:
    Yukino Ikegami

Lisence:
    MIT License

Usage:
    import jaconv
    jaconv.hira2kata(text, [ignore]) # ひらがなを全角カタカナに変換
    jaconv.hira2hkata(text, [ignore]) # ひらがなを半角カタカナに変換
    jaconv.kata2hira(text, [ignore]) # 全角カタカナをひらがなに変換
    jaconv.h2z(text, [ignore, kana, ascii, digit]) # 半角文字を全角文字に変換
    jaconv.z2h(text, [ignore, kana, ascii, digit]) # 全角文字を半角文字に変換
    jaconv.normalize(text, [nomalizemode]) # 半角カナを全角カナへ、全角英数字を半角英数字に変換
"""

VERSION = (0, 2, 2)
__version__ = '0.2.2'
__all__ = ['hira2kata', 'hira2hkata', 'kata2hira', 'h2z', 'z2h', 'normalize',
           'kana2alphabet', 'alphabet2kana']

hira2kata = jaconv.hira2kata
hira2hkata = jaconv.hira2hkata
kata2hira = jaconv.kata2hira
h2z = jaconv.h2z
z2h = jaconv.z2h
normalize = jaconv.normalize
kana2alphabet = jaconv.kana2alphabet
alphabet2kana = jaconv.alphabet2kana
