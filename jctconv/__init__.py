# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import jctconv
"""jctconv

This module provides Japanese and ASCII character interconverting between
Hiragana and full-/half-width Katakana/ASCII characters.

Author:
    Yukino Ikegami

Lisence:
    MIT License

Usage:
    import jctconv
    jctconv.hira2kata(text, [ignore]) # ひらがなを全角カタカナに変換
    jctconv.hira2hkata(text, [ignore]) # ひらがなを半角カタカナに変換
    jctconv.kata2hira(text, [ignore]) # 全角カタカナをひらがなに変換
    jctconv.h2z(text, [ignore, kana, ascii, digit]) # 半角文字を全角文字に変換
    jctconv.z2h(text, [ignore, kana, ascii, digit]) # 全角文字を半角文字に変換
    jctconv.normalize(text, [nomalizemode]) # 半角カナを全角カナへ、全角英数字を半角英数字に変換
"""

VERSION = (0, 1, 1)
__version__ = '0.1.1'
__all__ = ['hira2kata', 'hira2hkata', 'kata2hira', 'h2z', 'z2h', 'normalize']

hira2kata = jctconv.hira2kata
hira2hkata = jctconv.hira2hkata
kata2hira = jctconv.kata2hira
h2z = jctconv.h2z
z2h = jctconv.z2h
normalize = jctconv.normalize
