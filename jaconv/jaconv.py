# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re
import unicodedata
from .conv_table import (H2K_TABLE, H2HK_TABLE, K2H_TABLE, H2Z_A, H2Z_AD,
                         H2Z_AK, H2Z_D, H2Z_K, H2Z_DK, H2Z_ALL, Z2H_A, Z2H_AD,
                         Z2H_AK, Z2H_D, Z2H_K, Z2H_DK, Z2H_ALL, KANA2HEP, HEP2KANA)
from .compat import map

consonants = frozenset('sdfghjklqwrtypzxcvbnm')
ending_h_pattern = re.compile(r'h$')


def _exclude_ignorechar(ignore, conv_map):
    for character in map(ord, ignore):
        conv_map[character] = character
    return conv_map


def _convert(text, conv_map):
    return text.translate(conv_map)


def hira2kata(text, ignore=''):
    """Convert Hiragana to Full-width (Zenkaku) Katakana.

    Parameters
    ----------
    text : str
        Hiragana string.
    ignore : str
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
    if ignore:
        h2k_map = _exclude_ignorechar(ignore, H2K_TABLE.copy())
        return _convert(text, h2k_map)
    return _convert(text, H2K_TABLE)


def hira2hkata(text, ignore=''):
    """Convert Hiragana to Half-width (Hankaku) Katakana

    Parameters
    ----------
    text : str
        Hiragana string.
    ignore : str
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
    if ignore:
        h2hk_map = _exclude_ignorechar(ignore, H2HK_TABLE.copy())
        return _convert(text, h2hk_map)
    return _convert(text, H2HK_TABLE)


def kata2hira(text, ignore=''):
    """Convert Full-width Katakana to Hiragana

    Parameters
    ----------
    text : str
        Full-width Katakana string.
    ignore : str
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
    if ignore:
        k2h_map = _exclude_ignorechar(ignore, K2H_TABLE.copy())
        return _convert(text, k2h_map)
    return _convert(text, K2H_TABLE)


def h2z(text, ignore='', kana=True, ascii=False, digit=False):
    """Convert Half-width (Hankaku) Katakana to Full-width (Zenkaku) Katakana

    Parameters
    ----------
    text : str
        Half-width Katakana string.
    ignore : str
        Characters to be ignored in converting.
    kana : bool
        Either converting Kana or not.
    ascii : bool
        Either converting ascii or not.
    digit : bool
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
        """Convert Hankaku Dakuten Kana to Zenkaku Dakuten Kana
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

    Parameters
    ----------
    text : str
        Full-width Katakana string.
    ignore : str
        Characters to be ignored in converting.
    kana : bool
        Either converting Kana or not.
    ascii : bool
        Either converting ascii or not.
    digit : bool
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
        z2h_map = Z2H_K
    if ignore:
        z2h_map = _exclude_ignorechar(ignore, z2h_map.copy())
    return _convert(text, z2h_map)


def normalize(text, mode='NFKC'):
    """Convert Half-width (Hankaku) Katakana to Full-width (Zenkaku) Katakana,
    Full-width (Zenkaku) ASCII and DIGIT to Half-width (Hankaku) ASCII
    and DIGIT.
    Additionally, Full-width wave dash (〜) etc. are normalized

    Parameters
    ----------
    text : str
        Source string.
    mode : str
        Unicode normalization mode.

    Return
    ------
    str
        Normalized string.

    Examples
    --------
    >>> print(jaconv.normalize('ﾃｨﾛ･フィナ〜レ', 'NFKC'))
    ティロ・フィナーレ
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
    """Convert Hiragana to hepburn-style alphabets

    Parameters
    ----------
    text : str
        Hiragana string.

    Return
    ------
    str
        Hepburn-style alphabets string.

    Examples
    --------
    >>> print(jaconv.kana2alphabet('まみさん'))
    mamisan
    """
    text = text.replace('きゃ', 'kya').replace('きゅ', 'kyu').replace('きょ', 'kyo')
    text = text.replace('ぎゃ', 'gya').replace('ぎゅ', 'gyu').replace('ぎょ', 'gyo')
    text = text.replace('しゃ', 'sha').replace('しゅ', 'shu').replace('しょ', 'sho')
    text = text.replace('じゃ', 'ja').replace('じゅ', 'ju').replace('じょ', 'jo')
    text = text.replace('ちゃ', 'cha').replace('ちゅ', 'chu').replace('ちょ', 'cho')
    text = text.replace('にゃ', 'nya').replace('にゅ', 'nyu').replace('にょ', 'nyo')
    text = text.replace('ひゃ', 'hya').replace('ひゅ', 'hyu').replace('ひょ', 'hyo')
    text = text.replace('ふぁ', 'fa').replace('ふぃ', 'fi').replace('ふぇ', 'fe')
    text = text.replace('ふぉ', 'fo')
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
    text = text.replace('わ', 'wa').replace('ゐ', 'wi').replace('を', 'wo')
    text = text.replace('ゑ', 'we')
    text = _convert(text, KANA2HEP)
    while 'っ' in text:
        text = list(text)
        tsu_pos = text.index('っ')
        if len(text) <= tsu_pos + 1:
            return ''.join(text[:-1]) + 'xtsu'
        if tsu_pos == 0:
            text[tsu_pos] = 'xtsu'
        else:
            text[tsu_pos] = text[tsu_pos + 1]
        text = ''.join(text)
    return text


def alphabet2kana(text):
    """Convert alphabets to Hiragana

    Parameters
    ----------
    text : str
        Alphabets string.

    Return
    ------
    str
        Hiragana string.

    Examples
    --------
    >>> print(jaconv.alphabet2kana('mamisan'))
    まみさん
    """
    # replace final h with う, e.g., Itoh -> いとう
    text = re.sub(ending_h_pattern, 'う', text)

    text = text.replace('kya', 'きゃ').replace('kyi', 'きぃ').replace('kyu', 'きゅ')
    text = text.replace('kye', 'きぇ').replace('kyo', 'きょ')
    text = text.replace('gya', 'ぎゃ').replace('gyi', 'ぎぃ').replace('gyu', 'ぎゅ')
    text = text.replace('gye', 'ぎぇ').replace('gyo', 'ぎょ')
    text = text.replace('sha', 'しゃ').replace('shu', 'しゅ').replace('she', 'しぇ')
    text = text.replace('sho', 'しょ')
    text = text.replace('sya', 'しゃ').replace('syi', 'しぃ').replace('syu', 'しゅ')
    text = text.replace('sye', 'しぇ').replace('syo', 'しょ')
    text = text.replace('zya', 'じゃ').replace('zyu', 'じゅ').replace('zyo', 'じょ')
    text = text.replace('zyi', 'じぃ').replace('zye', 'じぇ')
    text = text.replace('ja', 'じゃ').replace('ju', 'じゅ').replace('jo', 'じょ')
    text = text.replace('jya', 'じゃ').replace('jyi', 'じぃ').replace('jyu', 'じゅ')
    text = text.replace('jye', 'じぇ').replace('jyo', 'じょ')
    text = text.replace('dya', 'ぢゃ').replace('dyi', 'ぢぃ').replace('dyu', 'ぢゅ')
    text = text.replace('dye', 'ぢぇ').replace('dyo', 'ぢょ')
    text = text.replace('cha', 'ちゃ').replace('chu', 'ちゅ').replace('che', 'ちぇ')
    text = text.replace('cho', 'ちょ')
    text = text.replace('cya', 'ちゃ').replace('cyi', 'ちぃ').replace('cyu', 'ちゅ')
    text = text.replace('cye', 'ちぇ').replace('cyo', 'ちょ')
    text = text.replace('tya', 'ちゃ').replace('tyi', 'ちぃ').replace('tyu', 'ちゅ')
    text = text.replace('tye', 'ちぇ').replace('tyo', 'ちょ')
    text = text.replace('tsa', 'つぁ').replace('tsi', 'つぃ').replace('tse', 'つぇ')
    text = text.replace('tso', 'つぉ')
    text = text.replace('thi', 'てぃ').replace('t\'i', 'てぃ')
    text = text.replace('tha', 'てゃ').replace('thu', 'てゅ').replace('t\'yu', 'てゅ')
    text = text.replace('the', 'てぇ').replace('tho', 'てょ')
    text = text.replace('dha', 'でゃ').replace('dhi', 'でぃ').replace('d\'i', 'でぃ')
    text = text.replace('dhu', 'でゅ').replace('dhe', 'でぇ').replace('dho', 'でょ')
    text = text.replace('d\'yu', 'でゅ')
    text = text.replace('twa', 'とぁ').replace('twi', 'とぃ').replace('twu', 'とぅ')
    text = text.replace('twe', 'とぇ').replace('two', 'とぉ').replace('t\'u', 'とぅ')
    text = text.replace('dwa', 'どぁ').replace('dwi', 'どぃ').replace('dwu', 'どぅ')
    text = text.replace('dwe', 'どぇ').replace('dwo', 'どぉ').replace('d\'u', 'どぅ')
    text = text.replace('nya', 'にゃ').replace('nyi', 'にぃ').replace('nyu', 'にゅ')
    text = text.replace('nye', 'にぇ').replace('nyo', 'にょ')
    text = text.replace('hya', 'ひゃ').replace('hyi', 'ひぃ').replace('hyu', 'ひゅ')
    text = text.replace('hye', 'ひぇ').replace('hyo', 'ひょ')
    text = text.replace('mya', 'みゃ').replace('myi', 'みぃ').replace('myu', 'みゅ')
    text = text.replace('mye', 'みぇ').replace('myo', 'みょ')
    text = text.replace('rya', 'りゃ').replace('ryi', 'りぃ').replace('ryu', 'りゅ')
    text = text.replace('rye', 'りぇ').replace('ryo', 'りょ')
    text = text.replace('bya', 'びゃ').replace('byi', 'びぃ').replace('byu', 'びゅ')
    text = text.replace('bye', 'びぇ').replace('byo', 'びょ')
    text = text.replace('pya', 'ぴゃ').replace('pyi', 'ぴぃ').replace('pyu', 'ぴゅ')
    text = text.replace('pye', 'ぴぇ').replace('pyo', 'ぴょ')
    text = text.replace('vyi', 'ゔぃ').replace('vyu', 'ゔゅ').replace('vye', 'ゔぇ')
    text = text.replace('vyo', 'ゔょ')
    text = text.replace('fya', 'ふゃ').replace('fyu', 'ふゅ').replace('fyo', 'ふょ')
    text = text.replace('hwa', 'ふぁ').replace('hwi', 'ふぃ').replace('hwe', 'ふぇ')
    text = text.replace('hwo', 'ふぉ').replace('hwyu', 'ふゅ')
    text = text.replace('pha', 'ふぁ').replace('phi', 'ふぃ').replace('phu', 'ふぅ')
    text = text.replace('phe', 'ふぇ').replace('pho', 'ふぉ')
    text = text.replace('xn', 'ん').replace('xa', 'ぁ').replace('xi', 'ぃ')
    text = text.replace('xu', 'ぅ').replace('xe', 'ぇ').replace('xo', 'ぉ')
    text = text.replace('lyi', 'ぃ').replace('xyi', 'ぃ').replace('lye', 'ぇ')
    text = text.replace('xye', 'ぇ').replace('xka', 'ヵ').replace('xke', 'ヶ')
    text = text.replace('lka', 'ヵ').replace('lke', 'ヶ')
    text = text.replace('ca', 'か').replace('ci', 'し').replace('cu', 'く')
    text = text.replace('co', 'こ')
    text = text.replace('qa', 'くぁ').replace('qi', 'くぃ').replace('qu', 'く')
    text = text.replace('qe', 'くぇ').replace('qo', 'くぉ')
    text = text.replace('kwa', 'くぁ').replace('kwi', 'くぃ').replace('kwu', 'くぅ')
    text = text.replace('kwe', 'くぇ').replace('kwo', 'くぉ')
    text = text.replace('gwa', 'ぐぁ').replace('gwi', 'ぐぃ').replace('gwu', 'ぐぅ')
    text = text.replace('gwe', 'ぐぇ').replace('gwo', 'ぐぉ')
    text = text.replace('swa', 'すぁ').replace('swi', 'すぃ').replace('swu', 'すぅ')
    text = text.replace('swe', 'すぇ').replace('swo', 'すぉ')
    text = text.replace('zwa', 'ずぁ').replace('zwi', 'ずぃ').replace('zwu', 'ずぅ')
    text = text.replace('zwe', 'ずぇ').replace('zwo', 'ずぉ')
    text = text.replace('je', 'じぇ')
    text = text.replace('ti', 'ち')
    text = text.replace('xtu', 'っ').replace('xtsu', 'っ')
    text = text.replace('ltu', 'っ').replace('ltsu', 'っ')
    text = text.replace('xya', 'ゃ').replace('lya', 'ゃ')
    text = text.replace('xyu', 'ゅ').replace('lyu', 'ゅ')
    text = text.replace('xyo', 'ょ').replace('lyo', 'ょ')
    text = text.replace('wha', 'うぁ').replace('whi', 'うぃ').replace('whu', 'う')
    text = text.replace('whe', 'うぇ').replace('who', 'うぉ')
    text = text.replace('xwa', 'ゎ').replace('lwa', 'ゎ')
    text = text.replace('tsu', 'つ')
    text = text.replace('ga', 'が').replace('gi', 'ぎ').replace('gu', 'ぐ')
    text = text.replace('ge', 'げ').replace('go', 'ご')
    text = text.replace('za', 'ざ').replace('ji', 'じ').replace('zi', 'じ')
    text = text.replace('zu', 'ず').replace('ze', 'ぜ').replace('zo', 'ぞ')
    text = text.replace('da', 'だ').replace('di', 'ぢ')
    text = text.replace('zu', 'づ').replace('du', 'づ')
    text = text.replace('de', 'で').replace('do', 'ど')
    text = text.replace('va', 'ゔぁ').replace('vi', 'ゔぃ').replace('vu', 'ゔ')
    text = text.replace('ve', 'ゔぇ').replace('vo', 'ゔぉ').replace('vya', 'ゔゃ')
    text = text.replace('ba', 'ば').replace('bi', 'び').replace('bu', 'ぶ')
    text = text.replace('be', 'べ').replace('bo', 'ぼ').replace('pa', 'ぱ')
    text = text.replace('pi', 'ぴ').replace('pu', 'ぷ').replace('pe', 'ぺ')
    text = text.replace('po', 'ぽ')
    text = text.replace('ka', 'か').replace('ki', 'き').replace('ku', 'く')
    text = text.replace('ke', 'け').replace('ko', 'こ').replace('sa', 'さ')
    text = text.replace('shi', 'し').replace('su', 'す').replace('se', 'せ')
    text = text.replace('so', 'そ').replace('ta', 'た').replace('chi', 'ち')
    text = text.replace('te', 'て').replace('to', 'と')
    text = text.replace('na', 'な').replace('ni', 'に').replace('nu', 'ぬ')
    text = text.replace('ne', 'ね').replace('no', 'の').replace('ha', 'は')
    text = text.replace('hi', 'ひ').replace('fu', 'ふ').replace('he', 'へ')
    text = text.replace('ho', 'ほ').replace('ma', 'ま').replace('mi', 'み')
    text = text.replace('mu', 'む').replace('me', 'め').replace('mo', 'も')
    text = text.replace('ra', 'ら').replace('ri', 'り').replace('ru', 'る')
    text = text.replace('re', 'れ').replace('ro', 'ろ')
    text = text.replace('la', 'ら').replace('li', 'り').replace('lu', 'る')
    text = text.replace('le', 'れ').replace('lo', 'ろ')
    text = text.replace('ya', 'や').replace('yu', 'ゆ').replace('yo', 'よ')
    text = text.replace('wa', 'わ').replace('wyi', 'ゐ').replace('wu', 'う')
    text = text.replace('wye', 'ゑ')
    text = text.replace('wo', 'を')
    text = text.replace('nn', 'ん').replace('m', 'ん')
    text = text.replace('tu', 'つ').replace('hu', 'ふ')
    text = text.replace('fa', 'ふぁ').replace('fi', 'ふぃ').replace('fe', 'ふぇ')
    text = text.replace('fo', 'ふぉ').replace('oh', 'おお')
    text = text.replace('l', 'る').replace('-', 'ー')
    text = _convert(text, HEP2KANA)
    ret = []
    for (i, char) in enumerate(text):
        if char in consonants:
            char = 'っ'
        ret.append(char)
    return ''.join(ret)
