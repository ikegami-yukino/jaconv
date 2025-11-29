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
    jaconv.hira2kata(text, [ignore])  # ひらがなを全角カタカナに変換
    jaconv.hira2hkata(text, [ignore])  # ひらがなを半角カタカナに変換
    jaconv.kata2hira(text, [ignore])  # 全角カタカナをひらがなに変換
    jaconv.enlargesmallkana(text, [ignore])  # 小文字かなを大文字かなに変換
    jaconv.h2z(text, [ignore, kana, ascii, digit])  # 半角文字を全角文字に変換
    jaconv.z2h(text, [ignore, kana, ascii, digit])  # 全角文字を半角文字に変換
    jaconv.han2zen(text, [ignore, kana, ascii, digit])  # 半角文字を全角文字に変換
    jaconv.zen2han(text, [ignore, kana, ascii, digit])  # 全角文字を半角文字に変換
    jaconv.normalize(text, [nomalizemode])  # 半角カナを全角カナへ、全角英数字を半角英数字に変換
    jaconv.kana2alphabet(text)  # かなをローマ字入力アルファベットに変換
    jaconv.alphabet2kana(text)  # ローマ字入力アルファベットをかなに変換
    jaconv.kata2alphabet(text)  # カタカナをローマ字入力アルファベットに変換
    jaconv.alphabet2kata(text)  # ローマ字入力アルファベットをカタカナに変換
    jaconv.hiragana2julius(text)  # ひらがなをJuliusの音素表現に変換
"""

VERSION = (0, 4, 1)
__version__ = '0.4.1'
__all__ = [
    'hira2kata', 'hira2hkata', 'kata2hira', 'h2z', 'z2h', 'hankaku2zenkaku',
    'zenkaku2hankaku', 'normalize', 'kana2alphabet', 'alphabet2kana',
    'kata2alphabet', 'alphabet2kata', 'hiragana2julius', 'enlargesmallkana'
]

hira2kata = jaconv.hira2kata
hira2hkata = jaconv.hira2hkata
kata2hira = jaconv.kata2hira
h2z = jaconv.h2z
z2h = jaconv.z2h
han2zen = jaconv.h2z  # an alias of h2z
zen2han = jaconv.z2h  # an alias of z2h
hankaku2zenkaku = jaconv.h2z  # an alias of h2z
zenkaku2hankaku = jaconv.z2h  # an alias of z2h
normalize = jaconv.normalize
kana2alphabet = jaconv.kana2alphabet
alphabet2kana = jaconv.alphabet2kana
kata2alphabet = lambda text: jaconv.kana2alphabet(jaconv.kata2hira(text))
alphabet2kata = lambda text: jaconv.hira2kata(jaconv.alphabet2kana(text))
hiragana2julius = jaconv.hiragana2julius
enlargesmallkana = jaconv.enlargesmallkana
