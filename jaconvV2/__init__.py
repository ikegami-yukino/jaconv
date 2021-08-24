# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import jaconv
"""jaconvV2

This module provides Japanese and ASCII character interconverting between
Hiragana and full-/half-width Katakana/ASCII characters.

Author:
    Yukino Ikegami

Lisence:
    MIT License

Usage:
    import jaconvV2
    jaconvV2.hira2kata(text, [ignore])  # ひらがなを全角カタカナに変換
    jaconvV2.hira2hkata(text, [ignore])  # ひらがなを半角カタカナに変換
    jaconvV2.kata2hira(text, [ignore])  # 全角カタカナをひらがなに変換
    jaconvV2.h2z(text, [ignore, kana, ascii, digit])  # 半角文字を全角文字に変換
    jaconvV2.z2h(text, [ignore, kana, ascii, digit])  # 全角文字を半角文字に変換
    jaconvV2.han2zen(text, [ignore, kana, ascii, digit])  # 半角文字を全角文字に変換
    jaconvV2.zen2han(text, [ignore, kana, ascii, digit])  # 全角文字を半角文字に変換
    jaconvV2.normalize(text, [nomalizemode])  # 半角カナを全角カナへ、全角英数字を半角英数字に変換
    jaconvV2.kana2alphabet(text)  # かなをヘボン式アルファベットに変換
    jaconvV2.alphabet2kana(text)  # アルファベットをかなに変換
    jaconvV2.kata2alphabet(text)  # カタカナをアルファベットに変換
    jaconvV2.alphabet2kata(text)  # アルファベットをカタカナに変換
    jaconvV2.hiragana2julius(text)  # ひらがなをJuliusの音素表現に変換
    jaconvV2.is_zen(char)         # Check if char is Zenkaku 全角キャラクタを確認
    jaconvV2.is_han(char)         # Check if char is Hankaku 半角キャラクタを確認
"""

VERSION = (0, 3)
__version__ = '0.3'
__all__ = ['hira2kata', 'hira2hkata', 'kata2hira', 'h2z', 'z2h',
           'hankaku2zenkaku', 'zenkaku2hankaku', 'normalize',
           'kana2alphabet', 'alphabet2kana', 'kata2alphabet', 'alphabet2kata',
           'hiragana2julius', 'is_zen', 'is_han']

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
is_zen = jaconv.is_zen
is_han = jaconv.is_han