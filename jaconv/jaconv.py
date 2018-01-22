# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import unicodedata
from .conv_table import (H2K_TABLE, H2HK_TABLE, K2H_TABLE, H2Z_A, H2Z_AD,
                         H2Z_AK, H2Z_D, H2Z_K, H2Z_DK, H2Z_ALL, Z2H_A, Z2H_AD,
                         Z2H_AK, Z2H_D, Z2H_K, Z2H_DK, Z2H_ALL, KANA2HEP, HEP2KANA)
from .compat import map

consonants = frozenset('sdfghjklqwrtypzxcvbnm')

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
        text = text.replace("ｶﾞ", "ガ").replace("ｷﾞ", "ギ")
        text = text.replace("ｸﾞ", "グ").replace("ｹﾞ", "ゲ")
        text = text.replace("ｺﾞ", "ゴ").replace("ｻﾞ", "ザ")
        text = text.replace("ｼﾞ", "ジ").replace("ｽﾞ", "ズ")
        text = text.replace("ｾﾞ", "ゼ").replace("ｿﾞ", "ゾ")
        text = text.replace("ﾀﾞ", "ダ").replace("ﾁﾞ", "ヂ")
        text = text.replace("ﾂﾞ", "ヅ").replace("ﾃﾞ", "デ")
        text = text.replace("ﾄﾞ", "ド").replace("ﾊﾞ", "バ")
        text = text.replace("ﾋﾞ", "ビ").replace("ﾌﾞ", "ブ")
        text = text.replace("ﾍﾞ", "ベ").replace("ﾎﾞ", "ボ")
        text = text.replace("ﾊﾟ", "パ").replace("ﾋﾟ", "ピ")
        text = text.replace("ﾌﾟ", "プ").replace("ﾍﾟ", "ペ")
        return text.replace("ﾎﾟ", "ポ").replace("ｳﾞ", "ヴ")

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
    """Convert Half-width (Hankaku) Katakana to Full-width (Zenkaku) Katakana,
    Full-width (Zenkaku) ASCII and DIGIT to Half-width (Hankaku) ASCII
    and DIGIT.
    Additionally, Full-width wave dash (〜) etc. are normalized

    Params:
        <unicode> text
        <unicode> ignore
    Return:
        <unicode> converted_text
    """
    text = text.replace('〜', 'ー').replace('～', 'ー')
    text = text.replace("’", "'").replace('”', '"').replace('“', '``')
    text = text.replace('―', '-').replace('‐', '-').replace('˗', '-').replace('֊', '-')
    text = text.replace('‐', '-').replace('‑', '-').replace('‒', '-').replace('–', '-')
    text = text.replace('⁃', '-').replace('⁻', '-').replace('₋', '-').replace('−', '-')
    text = text.replace('﹣', 'ー').replace('－', 'ー').replace('—', 'ー').replace('―', 'ー')
    text = text.replace('━', 'ー').replace('─', 'ー')
    return unicodedata.normalize(mode, text)


def kana2alphabet(text):
    """Convert hiragana to hepburn-style alphabets

    Params:
        <unicode> text
    Return:
        <unicode> converted_text
    """
    text = text.replace('きゃ', 'kya').replace('きゅ', 'kyu').replace('きょ', 'kyo')
    text = text.replace('ぎゃ', 'gya').replace('ぎゅ', 'gyu').replace('ぎょ', 'gyo')
    text = text.replace('しゃ', 'sha').replace('しゅ', 'shu').replace('しょ', 'sho')
    text = text.replace('じゃ', 'ja').replace('じゅ', 'ju').replace('じょ', 'jo')
    text = text.replace('ちゃ', 'cha').replace('ちゅ', 'chu').replace('ちょ', 'cho')
    text = text.replace('にゃ', 'nya').replace('にゅ', 'nyu').replace('にょ', 'nyo')
    text = text.replace('ふぁ', 'fa').replace('ふぃ', 'fi').replace('ふぇ', 'fe')
    text = text.replace('ふぉ', 'fo')
    text = text.replace('ひゃ', 'hya').replace('ひゅ', 'hyu').replace('ひょ', 'hyo')
    text = text.replace('みゃ', 'mya').replace('みゅ', 'myu').replace('みょ', 'myo')
    text = text.replace('りゃ', 'rya').replace('りゅ', 'ryu').replace('りょ', 'ryo')
    text = text.replace('びゃ', 'bya').replace('びゅ', 'byu').replace('びょ', 'byo')
    text = text.replace('ぴゃ', 'pya').replace('ぴゅ', 'pyu').replace('ぴょ', 'pyo')
    text = text.replace('が', 'ga').replace('ぎ', 'gi').replace('ぐ', 'gu')
    text = text.replace('げ', 'ge').replace('ご', 'go').replace('ざ', 'za')
    text = text.replace('じ', 'ji').replace('ず', 'zu').replace('ぜ', 'ze')
    text = text.replace('ぞ', 'zo').replace('だ', 'da').replace('ぢ', 'ji')
    text = text.replace('づ', 'zu').replace('で', 'de').replace('ど', 'do')
    text = text.replace('ば', 'ba').replace('び', 'bi').replace('ぶ', 'bu')
    text = text.replace('べ', 'be').replace('ぼ', 'bo').replace('ぱ', 'pa')
    text = text.replace('ぴ', 'pi').replace('ぷ', 'pu').replace('ぺ', 'pe')
    text = text.replace('ぽ', 'po')
    text = text.replace('か', 'ka').replace('き', 'ki').replace('く', 'ku')
    text = text.replace('け', 'ke').replace('こ', 'ko').replace('さ', 'sa')
    text = text.replace('し', 'shi').replace('す', 'su').replace('せ', 'se')
    text = text.replace('そ', 'so').replace('た', 'ta').replace('ち', 'chi')
    text = text.replace('つ', 'tsu').replace('て', 'te').replace('と', 'to')
    text = text.replace('な', 'na').replace('に', 'ni').replace('ぬ', 'nu')
    text = text.replace('ね', 'ne').replace('の', 'no').replace('は', 'ha')
    text = text.replace('ひ', 'hi').replace('ふ', 'fu').replace('へ', 'he')
    text = text.replace('ほ', 'ho').replace('ま', 'ma').replace('み', 'mi')
    text = text.replace('む', 'mu').replace('め', 'me').replace('も', 'mo')
    text = text.replace('ら', 'ra').replace('り', 'ri').replace('る', 'ru')
    text = text.replace('れ', 're').replace('ろ', 'ro')
    text = text.replace('や', 'ya').replace('ゆ', 'yu').replace('よ', 'yo')
    text = text.replace('わ', 'wa').replace('ゐ', 'we').replace('を', 'we')
    text = text.replace('ゑ', 'wo')
    text = _convert(text, KANA2HEP)
    while 'っ' in text:
        text = list(text)
        tsu_pos = text.index('っ')
        if len(text) <= tsu_pos + 1:
            return ''.join(text[:-1]) + 'xtsu'
        text[tsu_pos] = text[tsu_pos + 1]
        text = ''.join(text)
    return text


def alphabet2kana(text):
    """Convert alphabets to hiragana

    Params:
        <unicode> text
    Return:
        <unicode> converted_text
    """
    text = text.replace('kya', 'きゃ').replace('kyu', 'きゅ').replace('kyo', 'きょ')
    text = text.replace('gya', 'ぎゃ').replace('gyu', 'ぎゅ').replace('gyo', 'ぎょ')
    text = text.replace('sha', 'しゃ').replace('shu', 'しゅ').replace('sho', 'しょ')
    text = text.replace('zya', 'じゃ').replace('zyu', 'じゅ').replace('zyo', 'じょ')
    text = text.replace('zyi', 'じぃ').replace('zye', 'じぇ')
    text = text.replace('ja', 'じゃ').replace('ju', 'じゅ').replace('jo', 'じょ')
    text = text.replace('jya', 'じゃ').replace('jyu', 'じゅ').replace('jyo', 'じょ')
    text = text.replace('cha', 'ちゃ').replace('chu', 'ちゅ').replace('cho', 'ちょ')
    text = text.replace('tya', 'ちゃ').replace('tyu', 'ちゅ').replace('tyo', 'ちょ')
    text = text.replace('nya', 'にゃ').replace('nyu', 'にゅ').replace('nyo', 'にょ')
    text = text.replace('hya', 'ひゃ').replace('hyu', 'ひゅ').replace('hyo', 'ひょ')
    text = text.replace('mya', 'みゃ').replace('myu', 'みゅ').replace('myo', 'みょ')
    text = text.replace('rya', 'りゃ').replace('ryu', 'りゅ').replace('ryo', 'りょ')
    text = text.replace('bya', 'びゃ').replace('byu', 'びゅ').replace('byo', 'びょ')
    text = text.replace('pya', 'ぴゃ').replace('pyu', 'ぴゅ').replace('pyo', 'ぴょ')
    text = text.replace('oh', 'おお')
    text = text.replace('ga', 'が').replace('gi', 'ぎ').replace('gu', 'ぐ')
    text = text.replace('ge', 'げ').replace('go', 'ご').replace('za', 'ざ')
    text = text.replace('ji', 'じ').replace('zu', 'ず').replace('ze', 'ぜ')
    text = text.replace('zo', 'ぞ').replace('da', 'だ').replace('ji', 'ぢ').replace('di', 'ぢ')
    text = text.replace('va', 'ゔぁ').replace('vi', 'ゔぃ').replace('vu', 'ゔ')
    text = text.replace('ve', 'ゔぇ').replace('vo', 'ゔぉ').replace('vya', 'ゔゃ')
    text = text.replace('vyi', 'ゔぃ').replace('vyu', 'ゔゅ').replace('vye', 'ゔぇ')
    text = text.replace('vyo', 'ゔょ')
    text = text.replace('zu', 'づ').replace('de', 'で').replace('do', 'ど')
    text = text.replace('ba', 'ば').replace('bi', 'び').replace('bu', 'ぶ')
    text = text.replace('be', 'べ').replace('bo', 'ぼ').replace('pa', 'ぱ')
    text = text.replace('pi', 'ぴ').replace('pu', 'ぷ').replace('pe', 'ぺ')
    text = text.replace('po', 'ぽ').replace('dha', 'でゃ').replace('dhi', 'でぃ')
    text = text.replace('dhu', 'でゅ').replace('dhe', 'でぇ').replace('dho', 'でょ')
    text = text.replace('ka', 'か').replace('ki', 'き').replace('ku', 'く')
    text = text.replace('ke', 'け').replace('ko', 'こ').replace('sa', 'さ')
    text = text.replace('shi', 'し').replace('su', 'す').replace('se', 'せ')
    text = text.replace('so', 'そ').replace('ta', 'た').replace('chi', 'ち')
    text = text.replace('tsu', 'つ').replace('te', 'て').replace('to', 'と')
    text = text.replace('na', 'な').replace('ni', 'に').replace('nu', 'ぬ')
    text = text.replace('ne', 'ね').replace('no', 'の').replace('ha', 'は')
    text = text.replace('hi', 'ひ').replace('fu', 'ふ').replace('he', 'へ')
    text = text.replace('ho', 'ほ').replace('ma', 'ま').replace('mi', 'み')
    text = text.replace('mu', 'む').replace('me', 'め').replace('mo', 'も')
    text = text.replace('ra', 'ら').replace('ri', 'り').replace('ru', 'る')
    text = text.replace('re', 'れ').replace('ro', 'ろ')
    text = text.replace('ya', 'や').replace('yu', 'ゆ').replace('yo', 'よ')
    text = text.replace('wa', 'わ').replace('we', 'ゐ').replace('we', 'を')
    text = text.replace('wo', 'ゑ').replace('wo', 'を').replace('wo', 'を')
    text = text.replace('nn', 'ん').replace('tu', 'つ').replace('hu', 'ふ')
    text = text.replace('fa', 'ふぁ').replace('fi', 'ふぃ').replace('fe', 'ふぇ')
    text = text.replace('fo', 'ふぉ').replace('-', 'ー')
    text = _convert(text, HEP2KANA)
    ret = []
    for (i, char) in enumerate(text):
        if char in consonants:
            char = 'っ'
        ret.append(char)
    return ''.join(ret)
