# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re
import unicodedata
from .conv_table import (H2K_TABLE, H2HK_TABLE, K2H_TABLE, H2Z_A, H2Z_AD,
                         H2Z_AK, H2Z_D, H2Z_K, H2Z_DK, H2Z_ALL,
                         SMALL_KANA2BIG_KANA, Z2H_A, Z2H_AD, Z2H_AK, Z2H_D,
                         Z2H_K, Z2H_DK, Z2H_ALL, KANA2HEP, HEP2KANA,
                         JULIUS_LONG_VOWEL)
from .compat import map

consonants = frozenset('sdfghjklqwrtypzxcvbnm')
ending_h_pattern = re.compile(r'h$')


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


def enlargesmallkana(text, ignore='') -> str:
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
    return _translate(text, ignore, SMALL_KANA2BIG_KANA)


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
        if kana:
            h2z_map = H2Z_K
        else:
            h2z_map = {}  # empty
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


def normalize(text, mode='NFKC'):
    """Convert Half-width (Hankaku) Katakana to Full-width (Zenkaku) Katakana,
    Full-width (Zenkaku) ASCII and DIGIT to Half-width (Hankaku) ASCII
    and DIGIT.
    Additionally, Full-width wave dash (〜) etc. are normalized

    Parameters
    ----------
    text : str
        Source string.
    mode : str, optional
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
    text = text.replace("’", "'").replace('”', '"').replace('“', '"')
    text = text.replace('―', '-').replace('‐',
                                          '-').replace('˗',
                                                       '-').replace('֊', '-')
    text = text.replace('‐', '-').replace('‑',
                                          '-').replace('‒',
                                                       '-').replace('–', '-')
    text = text.replace('⁃', '-').replace('⁻',
                                          '-').replace('₋',
                                                       '-').replace('−', '-')
    text = text.replace('﹣', 'ー').replace('－',
                                          'ー').replace('—',
                                                       'ー').replace('―', 'ー')
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
        Roman-input-style alphabets string.

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
        chars = list(text)
        tsu_pos = chars.index('っ')
        if len(chars) <= tsu_pos + 1:
            return ''.join(chars[:-1]) + 'xtsu'
        if tsu_pos == 0:
            chars[tsu_pos] = 'xtsu'
        elif chars[tsu_pos + 1] == 'っ':
            chars[tsu_pos] = 'xtsu'
        else:
            chars[tsu_pos] = chars[tsu_pos + 1]
        text = ''.join(chars)
    return text


def alphabet2kana(text):
    """Convert alphabets to Hiragana

    Parameters
    ----------
    text : str
        Roman-input-style alphabets string.

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
    text = text.replace('tha', 'てゃ').replace('thu',
                                             'てゅ').replace('t\'yu', 'てゅ')
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


def hiragana2julius(text):
    """Convert Hiragana to Julius's phoneme format.

    Parameters
    ----------
    text : str
        Hiragana string.

    Return
    ------
    str
        Alphabet string.

    Examples
    --------
    >>> print(jaconv.hiragana2julius('てんきすごくいいいいいい'))
    t e N k i s u g o k u i:
    """

    # 3文字以上からなる変換規則
    text = text.replace('う゛ぁ', ' b a')
    text = text.replace('う゛ぃ', ' b i')
    text = text.replace('う゛ぇ', ' b e')
    text = text.replace('う゛ぉ', ' b o')
    text = text.replace('う゛ゅ', ' by u')

    # 2文字からなる変換規則
    text = text.replace('ぅ゛', ' b u')

    text = text.replace('あぁ', ' a a')
    text = text.replace('いぃ', ' i i')
    text = text.replace('いぇ', ' i e')
    text = text.replace('いゃ', ' y a')
    text = text.replace('うぅ', ' u:')
    text = text.replace('えぇ', ' e e')
    text = text.replace('おぉ', ' o:')
    text = text.replace('かぁ', ' k a:')
    text = text.replace('きぃ', ' k i:')
    text = text.replace('くぅ', ' k u:')
    text = text.replace('くゃ', ' ky a')
    text = text.replace('くゅ', ' ky u')
    text = text.replace('くょ', ' ky o')
    text = text.replace('けぇ', ' k e:')
    text = text.replace('こぉ', ' k o:')
    text = text.replace('がぁ', ' g a:')
    text = text.replace('ぎぃ', ' g i:')
    text = text.replace('ぐぅ', ' g u:')
    text = text.replace('ぐゃ', ' gy a')
    text = text.replace('ぐゅ', ' gy u')
    text = text.replace('ぐょ', ' gy o')
    text = text.replace('げぇ', ' g e:')
    text = text.replace('ごぉ', ' g o:')
    text = text.replace('さぁ', ' s a:')
    text = text.replace('しぃ', ' sh i:')
    text = text.replace('すぅ', ' s u:')
    text = text.replace('すゃ', ' sh a')
    text = text.replace('すゅ', ' sh u')
    text = text.replace('すょ', ' sh o')
    text = text.replace('せぇ', ' s e:')
    text = text.replace('そぉ', ' s o:')
    text = text.replace('ざぁ', ' z a:')
    text = text.replace('じぃ', ' j i:')
    text = text.replace('ずぅ', ' z u:')
    text = text.replace('ずゃ', ' zy a')
    text = text.replace('ずゅ', ' zy u')
    text = text.replace('ずょ', ' zy o')
    text = text.replace('ぜぇ', ' z e:')
    text = text.replace('ぞぉ', ' z o:')
    text = text.replace('たぁ', ' t a:')
    text = text.replace('ちぃ', ' ch i:')
    text = text.replace('つぁ', ' ts a')
    text = text.replace('つぃ', ' ts i')
    text = text.replace('つぅ', ' ts u:')
    text = text.replace('つゃ', ' ch a')
    text = text.replace('つゅ', ' ch u')
    text = text.replace('つょ', ' ch o')
    text = text.replace('つぇ', ' ts e')
    text = text.replace('つぉ', ' ts o')
    text = text.replace('てぇ', ' t e:')
    text = text.replace('とぉ', ' t o:')
    text = text.replace('だぁ', ' d a:')
    text = text.replace('ぢぃ', ' j i:')
    text = text.replace('づぅ', ' d u:')
    text = text.replace('づゃ', ' zy a')
    text = text.replace('づゅ', ' zy u')
    text = text.replace('づょ', ' zy o')
    text = text.replace('でぇ', ' d e:')
    text = text.replace('どぉ', ' d o:')
    text = text.replace('なぁ', ' n a:')
    text = text.replace('にぃ', ' n i:')
    text = text.replace('ぬぅ', ' n u:')
    text = text.replace('ぬゃ', ' ny a')
    text = text.replace('ぬゅ', ' ny u')
    text = text.replace('ぬょ', ' ny o')
    text = text.replace('ねぇ', ' n e:')
    text = text.replace('のぉ', ' n o:')
    text = text.replace('はぁ', ' h a:')
    text = text.replace('ひぃ', ' h i:')
    text = text.replace('ふぅ', ' f u:')
    text = text.replace('ふゃ', ' hy a')
    text = text.replace('ふゅ', ' hy u')
    text = text.replace('ふょ', ' hy o')
    text = text.replace('へぇ', ' h e:')
    text = text.replace('ほぉ', ' h o:')
    text = text.replace('ばぁ', ' b a:')
    text = text.replace('びぃ', ' b i:')
    text = text.replace('ぶぅ', ' b u:')
    text = text.replace('ふゃ', ' hy a')
    text = text.replace('ぶゅ', ' by u')
    text = text.replace('ふょ', ' hy o')
    text = text.replace('べぇ', ' b e:')
    text = text.replace('ぼぉ', ' b o:')
    text = text.replace('ぱぁ', ' p a:')
    text = text.replace('ぴぃ', ' p i:')
    text = text.replace('ぷぅ', ' p u:')
    text = text.replace('ぷゃ', ' py a')
    text = text.replace('ぷゅ', ' py u')
    text = text.replace('ぷょ', ' py o')
    text = text.replace('ぺぇ', ' p e:')
    text = text.replace('ぽぉ', ' p o:')
    text = text.replace('まぁ', ' m a:')
    text = text.replace('みぃ', ' m i:')
    text = text.replace('むぅ', ' m u:')
    text = text.replace('むゃ', ' my a')
    text = text.replace('むゅ', ' my u')
    text = text.replace('むょ', ' my o')
    text = text.replace('めぇ', ' m e:')
    text = text.replace('もぉ', ' m o:')
    text = text.replace('やぁ', ' y a:')
    text = text.replace('ゆぅ', ' y u:')
    text = text.replace('ゆゃ', ' y a:')
    text = text.replace('ゆゅ', ' y u:')
    text = text.replace('ゆょ', ' y o:')
    text = text.replace('よぉ', ' y o:')
    text = text.replace('らぁ', ' r a:')
    text = text.replace('りぃ', ' r i:')
    text = text.replace('るぅ', ' r u:')
    text = text.replace('るゃ', ' ry a')
    text = text.replace('るゅ', ' ry u')
    text = text.replace('るょ', ' ry o')
    text = text.replace('れぇ', ' r e:')
    text = text.replace('ろぉ', ' r o:')
    text = text.replace('わぁ', ' w a:')
    text = text.replace('をぉ', ' o:')

    text = text.replace('う゛', ' b u')
    text = text.replace('でぃ', ' d i')
    text = text.replace('でぇ', ' d e:')
    text = text.replace('でゃ', ' dy a')
    text = text.replace('でゅ', ' dy u')
    text = text.replace('でょ', ' dy o')
    text = text.replace('てぃ', ' t i')
    text = text.replace('てぇ', ' t e:')
    text = text.replace('てゃ', ' ty a')
    text = text.replace('てゅ', ' ty u')
    text = text.replace('てょ', ' ty o')
    text = text.replace('すぃ', ' s i')
    text = text.replace('ずぁ', ' z u a')
    text = text.replace('ずぃ', ' z i')
    text = text.replace('ずぅ', ' z u')
    text = text.replace('ずゃ', ' zy a')
    text = text.replace('ずゅ', ' zy u')
    text = text.replace('ずょ', ' zy o')
    text = text.replace('ずぇ', ' z e')
    text = text.replace('ずぉ', ' z o')
    text = text.replace('きゃ', ' ky a')
    text = text.replace('きゅ', ' ky u')
    text = text.replace('きょ', ' ky o')
    text = text.replace('しゃ', ' sh a')
    text = text.replace('しゅ', ' sh u')
    text = text.replace('しぇ', ' sh e')
    text = text.replace('しょ', ' sh o')
    text = text.replace('ちゃ', ' ch a')
    text = text.replace('ちゅ', ' ch u')
    text = text.replace('ちぇ', ' ch e')
    text = text.replace('ちょ', ' ch o')
    text = text.replace('とぅ', ' t u')
    text = text.replace('とゃ', ' ty a')
    text = text.replace('とゅ', ' ty u')
    text = text.replace('とょ', ' ty o')
    text = text.replace('どぁ', ' d o a')
    text = text.replace('どぅ', ' d u')
    text = text.replace('どゃ', ' dy a')
    text = text.replace('どゅ', ' dy u')
    text = text.replace('どょ', ' dy o')
    text = text.replace('どぉ', ' d o:')
    text = text.replace('にゃ', ' ny a')
    text = text.replace('にゅ', ' ny u')
    text = text.replace('にょ', ' ny o')
    text = text.replace('ひゃ', ' hy a')
    text = text.replace('ひゅ', ' hy u')
    text = text.replace('ひょ', ' hy o')
    text = text.replace('みゃ', ' my a')
    text = text.replace('みゅ', ' my u')
    text = text.replace('みょ', ' my o')
    text = text.replace('りゃ', ' ry a')
    text = text.replace('りゅ', ' ry u')
    text = text.replace('りょ', ' ry o')
    text = text.replace('ぎゃ', ' gy a')
    text = text.replace('ぎゅ', ' gy u')
    text = text.replace('ぎょ', ' gy o')
    text = text.replace('ぢぇ', ' j e')
    text = text.replace('ぢゃ', ' j a')
    text = text.replace('ぢゅ', ' j u')
    text = text.replace('ぢょ', ' j o')
    text = text.replace('じぇ', ' j e')
    text = text.replace('じゃ', ' j a')
    text = text.replace('じゅ', ' j u')
    text = text.replace('じょ', ' j o')
    text = text.replace('びゃ', ' by a')
    text = text.replace('びゅ', ' by u')
    text = text.replace('びょ', ' by o')
    text = text.replace('ぴゃ', ' py a')
    text = text.replace('ぴゅ', ' py u')
    text = text.replace('ぴょ', ' py o')
    text = text.replace('うぁ', ' u a')
    text = text.replace('うぃ', ' w i')
    text = text.replace('うぇ', ' w e')
    text = text.replace('うぉ', ' w o')
    text = text.replace('ふぁ', ' f a')
    text = text.replace('ふぃ', ' f i')
    text = text.replace('ふぅ', ' f u')
    text = text.replace('ふゃ', ' hy a')
    text = text.replace('ふゅ', ' hy u')
    text = text.replace('ふょ', ' hy o')
    text = text.replace('ふぇ', ' f e')
    text = text.replace('ふぉ', ' f o')

    # 1音からなる変換規則
    text = text.replace('あ', ' a')
    text = text.replace('い', ' i')
    text = text.replace('う', ' u')
    text = text.replace('え', ' e')
    text = text.replace('お', ' o')
    text = text.replace('か', ' k a')
    text = text.replace('き', ' k i')
    text = text.replace('く', ' k u')
    text = text.replace('け', ' k e')
    text = text.replace('こ', ' k o')
    text = text.replace('さ', ' s a')
    text = text.replace('し', ' sh i')
    text = text.replace('す', ' s u')
    text = text.replace('せ', ' s e')
    text = text.replace('そ', ' s o')
    text = text.replace('た', ' t a')
    text = text.replace('ち', ' ch i')
    text = text.replace('つ', ' ts u')
    text = text.replace('て', ' t e')
    text = text.replace('と', ' t o')
    text = text.replace('な', ' n a')
    text = text.replace('に', ' n i')
    text = text.replace('ぬ', ' n u')
    text = text.replace('ね', ' n e')
    text = text.replace('の', ' n o')
    text = text.replace('は', ' h a')
    text = text.replace('ひ', ' h i')
    text = text.replace('ふ', ' f u')
    text = text.replace('へ', ' h e')
    text = text.replace('ほ', ' h o')
    text = text.replace('ま', ' m a')
    text = text.replace('み', ' m i')
    text = text.replace('む', ' m u')
    text = text.replace('め', ' m e')
    text = text.replace('も', ' m o')
    text = text.replace('ら', ' r a')
    text = text.replace('り', ' r i')
    text = text.replace('る', ' r u')
    text = text.replace('れ', ' r e')
    text = text.replace('ろ', ' r o')
    text = text.replace('が', ' g a')
    text = text.replace('ぎ', ' g i')
    text = text.replace('ぐ', ' g u')
    text = text.replace('げ', ' g e')
    text = text.replace('ご', ' g o')
    text = text.replace('ざ', ' z a')
    text = text.replace('じ', ' j i')
    text = text.replace('ず', ' z u')
    text = text.replace('ぜ', ' z e')
    text = text.replace('ぞ', ' z o')
    text = text.replace('だ', ' d a')
    text = text.replace('ぢ', ' j i')
    text = text.replace('づ', ' z u')
    text = text.replace('で', ' d e')
    text = text.replace('ど', ' d o')
    text = text.replace('ば', ' b a')
    text = text.replace('び', ' b i')
    text = text.replace('ぶ', ' b u')
    text = text.replace('べ', ' b e')
    text = text.replace('ぼ', ' b o')
    text = text.replace('ぱ', ' p a')
    text = text.replace('ぴ', ' p i')
    text = text.replace('ぷ', ' p u')
    text = text.replace('ぺ', ' p e')
    text = text.replace('ぽ', ' p o')
    text = text.replace('や', ' y a')
    text = text.replace('ゆ', ' y u')
    text = text.replace('よ', ' y o')
    text = text.replace('わ', ' w a')
    text = text.replace('ゐ', ' i')
    text = text.replace('ゑ', ' e')
    text = text.replace('ん', ' N')
    text = text.replace('っ', ' q')
    # ここまでに処理されてない ぁぃぅぇぉ はそのまま大文字扱い
    text = text.replace('ぁ', ' a')
    text = text.replace('ぃ', ' i')
    text = text.replace('ぅ', ' u')
    text = text.replace('ぇ', ' e')
    text = text.replace('ぉ', ' o')
    text = text.replace('ゎ', ' w a')
    text = text.replace('ぉ', ' o')

    # 長音の処理
    for (pattern, replace_str) in JULIUS_LONG_VOWEL:
        text = pattern.sub(replace_str, text)
    text = text.replace('o u', 'o:')  # おう -> おーの音便
    text = text.replace('ー', ':')
    text = text.replace('〜', ':')
    text = text.replace('−', ':')
    text = text.replace('-', ':')

    #その他特別な処理
    text = text.replace('を', ' o')

    text = text.strip()

    text = text.replace(':+', ':')
    return text
