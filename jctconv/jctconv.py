# -*- coding: utf-8 -*-
import unicodedata
from .conv_table import (H2K_TABLE, H2HK_TABLE, K2H_TABLE, H2Z_A, H2Z_AD,
                         H2Z_AK, H2Z_D, H2Z_K, H2Z_DK, H2Z_ALL, Z2H_A, Z2H_AD,
                         Z2H_AK, Z2H_D, Z2H_K, Z2H_DK, Z2H_ALL)
from .compat import map


def _exclude_ignorechar(ignore, conv_map):
    for character in map(ord, ignore):
        conv_map[character] = character
    return conv_map


def _convert(text, conv_map):
    return text.translate(conv_map)


def hira2kata(text, ignore=''):
    """Convert Hiragana to Full-width (Zenkaku) Katakana

    Params:
        <unicode> text
        <unicode> ignore
    Return:
        <unicode> converted_text
    """
    if ignore:
        h2k_map = _exclude_ignorechar(ignore, H2K_TABLE.copy())
        return _convert(text, h2k_map)
    return _convert(text, H2K_TABLE)


def hira2hkata(text, ignore=''):
    """Convert Hiragana to Half-width (Hankaku) Katakana

    Params:
        <unicode> text
        <unicode> ignore
    Return:
        <unicode> converted_text
    """
    if ignore:
        h2hk_map = _exclude_ignorechar(ignore, H2HK_TABLE.copy())
        return _convert(text, h2hk_map)
    return _convert(text, H2HK_TABLE)


def kata2hira(text, ignore=''):
    """Convert Full-width Katakana to Hiragana

    Params:
        <unicode> text
        <unicode> ignore
    Return:
        <unicode> converted_text
    """
    if ignore:
        k2h_map = _exclude_ignorechar(ignore, K2H_TABLE.copy())
        return _convert(text, k2h_map)
    return _convert(text, K2H_TABLE)


def h2z(text, ignore='', kana=True, ascii=False, digit=False):
    """Convert Half-width (Hankaku) Katakana to Full-width (Zenkaku) Katakana

    Params:
        <unicode> text
        <unicode> ignore
    Return:
        <unicode> converted_text
    """
    def _conv_dakuten(text):
        """
        半角濁点カナを全角に変換
        """
        text = text.replace(u"ｶﾞ", u"ガ").replace(u"ｷﾞ", u"ギ")
        text = text.replace(u"ｸﾞ", u"グ").replace(u"ｹﾞ", u"ゲ")
        text = text.replace(u"ｺﾞ", u"ゴ").replace(u"ｻﾞ", u"ザ")
        text = text.replace(u"ｼﾞ", u"ジ").replace(u"ｽﾞ", u"ズ")
        text = text.replace(u"ｾﾞ", u"ゼ").replace(u"ｿﾞ", u"ゾ")
        text = text.replace(u"ﾀﾞ", u"ダ").replace(u"ﾁﾞ", u"ヂ")
        text = text.replace(u"ﾂﾞ", u"ヅ").replace(u"ﾃﾞ", u"デ")
        text = text.replace(u"ﾄﾞ", u"ド").replace(u"ﾊﾞ", u"バ")
        text = text.replace(u"ﾋﾞ", u"ビ").replace(u"ﾌﾞ", u"ブ")
        text = text.replace(u"ﾍﾞ", u"ベ").replace(u"ﾎﾞ", u"ボ")
        text = text.replace(u"ﾊﾟ", u"パ").replace(u"ﾋﾟ", u"ピ")
        text = text.replace(u"ﾌﾟ", u"プ").replace(u"ﾍﾟ", u"ペ")
        return text.replace(u"ﾎﾟ", u"ポ").replace(u"ｳﾞ", u"ヴ")

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
        h2z_map = H2Z_K
    if kana:
        text = _conv_dakuten(text)
    if ignore:
        h2z_map = _exclude_ignorechar(ignore, h2z_map.copy())
    return _convert(text, h2z_map)


def z2h(text, ignore='', kana=True, ascii=False, digit=False):
    """Convert Full-width (Zenkaku) Katakana to Half-width (Hankaku) Katakana

    Params:
        <unicode> text
        <unicode> ignore
    Return:
        <unicode> converted_text
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
        z2h_map = Z2H_K
    if ignore:
        z2h_map = _exclude_ignorechar(ignore, z2h_map.copy())
    return _convert(text, z2h_map)


def normalize(text, mode='NFKC', ignore=''):
    u"""Convert Half-width (Hankaku) Katakana to Full-width (Zenkaku) Katakana,
    Full-width (Zenkaku) ASCII and DIGIT to Half-width (Hankaku) ASCII
    and DIGIT.
    Additionally, Full-width wave dash (〜) etc. are normalized

    Params:
        <unicode> text
        <unicode> ignore
    Return:
        <unicode> converted_text
    """
    text = text.replace(u'〜', u'ー').replace(u'～', u'ー')
    text = text.replace(u"’", "'").replace(u'”', '"').replace(u'“', '``')
    text = text.replace(u'―', '-').replace(u'‐', u'-')
    return unicodedata.normalize(mode, text)
