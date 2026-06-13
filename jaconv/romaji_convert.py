# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .conv_table import HEP2KANA, KANA2HEP
from .helpers import _convert
from .kana_convert import hira2kata, kata2hira

consonants = frozenset('sdfghjklqwrtypzxcvbnm')


def kana2alphabet(text):
    """Convert Hiragana to Roman-input-style alphabets

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
    text = text.replace('ゔぁ', 'va').replace('ゔぃ', 'vi').replace('ゔぅ', 'vuu')
    text = text.replace('ゔぇ', 've').replace('ゔぉ', 'vo')
    text = text.replace('ゃ', 'ya').replace('ゅ', 'yu').replace('ょ', 'yo')
    text = text.replace('ぁ', 'a').replace('ぃ', 'i').replace('ぅ', 'u')
    text = text.replace('ぇ', 'e').replace('ぉ', 'o')
    text = text.replace('ゎ', 'wa')
    text = text.replace('ゔ', 'vu')
    text = text.replace('ヵ', 'ka')  # Strictly, it's kanji, not kana.
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


def kata2alphabet(text):
    """Convert Katakana to Roman-input-style alphabets

    Parameters
    ----------
    text : str
        Katakana string.

    Return
    ------
    str
        Roman-input-style alphabets string.

    Examples
    --------
    >>> print(jaconv.kata2alphabet('マミサン'))
    mamisan
    """
    return kana2alphabet(kata2hira(text))


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
    text = text.lower()  # ensure lower case.

    # replace final h with う, e.g., Itoh -> いとう
    if text.endswith('h') and len(text) >= 2:
        text = text[:-1] + 'う'

    text = text.replace('tch', 'っch')
    text = text.replace('bb', 'っb').replace('cc', 'っc').replace('dd', 'っd')
    text = text.replace('ff', 'っf').replace('gg', 'っg').replace('hh', 'っh')
    text = text.replace('jj', 'っj').replace('kk', 'っk').replace('ll', 'っl')
    text = text.replace('mm', 'っm').replace('pp', 'っp').replace('qq', 'っq')
    text = text.replace('rr', 'っr').replace('ss', 'っs').replace('tt', 'っt')
    text = text.replace('vv', 'っv').replace('ww', 'っw').replace('xx', 'っx')
    text = text.replace('yy', 'っy').replace('zz', 'っz')
    text = text.replace('kya', 'きゃ').replace('kyi', 'きぃ').replace('kyu', 'きゅ')
    text = text.replace('kye', 'きぇ').replace('kyo', 'きょ')
    text = text.replace('gya', 'ぎゃ').replace('gyi', 'ぎぃ').replace('gyu', 'ぎゅ')
    text = text.replace('gye', 'ぎぇ').replace('gyo', 'ぎょ')
    text = text.replace('sha', 'しゃ').replace('shi', 'し').replace('shu', 'しゅ')
    text = text.replace('she', 'しぇ').replace('sho', 'しょ')
    text = text.replace('sya', 'しゃ').replace('syi', 'しぃ').replace('syu', 'しゅ')
    text = text.replace('sye', 'しぇ').replace('syo', 'しょ')
    text = text.replace('zya', 'じゃ').replace('zyu', 'じゅ').replace('zyo', 'じょ')
    text = text.replace('zyi', 'じぃ').replace('zye', 'じぇ')
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
    text = text.replace('thi', 'てぃ').replace("t'i", 'てぃ')
    text = text.replace('tha', 'てゃ').replace('thu', 'てゅ').replace("t'yu", 'てゅ')
    text = text.replace('the', 'てぇ').replace('tho', 'てょ')
    text = text.replace('dha', 'でゃ').replace('dhi', 'でぃ').replace("d'i", 'でぃ')
    text = text.replace('dhu', 'でゅ').replace('dhe', 'でぇ').replace('dho', 'でょ')
    text = text.replace("d'yu", 'でゅ')
    text = text.replace('twa', 'とぁ').replace('twi', 'とぃ').replace('twu', 'とぅ')
    text = text.replace('twe', 'とぇ').replace('two', 'とぉ').replace("t'u", 'とぅ')
    text = text.replace('dwa', 'どぁ').replace('dwi', 'どぃ').replace('dwu', 'どぅ')
    text = text.replace('dwe', 'どぇ').replace('dwo', 'どぉ').replace("d'u", 'どぅ')
    text = text.replace('nya', 'にゃ').replace('nyi', 'にぃ').replace('nyu', 'にゅ')
    text = text.replace('nye', 'にぇ').replace('nyo', 'にょ')
    text = text.replace('hya', 'ひゃ').replace('hyi', 'ひぃ').replace('hyu', 'ひゅ')
    text = text.replace('hye', 'ひぇ').replace('hyo', 'ひょ')
    text = text.replace('hwa', 'ふぁ').replace('hwi', 'ふぃ').replace('hwe', 'ふぇ')
    text = text.replace('hwo', 'ふぉ').replace('hwyu', 'ふゅ')
    text = text.replace('fya', 'ふゃ').replace('fyu', 'ふゅ').replace('fyo', 'ふょ')
    text = text.replace('pha', 'ふぁ').replace('phi', 'ふぃ').replace('phu', 'ふぅ')
    text = text.replace('phe', 'ふぇ').replace('pho', 'ふぉ')
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
    text = text.replace('wye', 'ゑ')
    text = text.replace('kwa', 'くぁ').replace('kwi', 'くぃ').replace('kwu', 'くぅ')
    text = text.replace('kwe', 'くぇ').replace('kwo', 'くぉ')
    text = text.replace('gwa', 'ぐぁ').replace('gwi', 'ぐぃ').replace('gwu', 'ぐぅ')
    text = text.replace('gwe', 'ぐぇ').replace('gwo', 'ぐぉ')
    text = text.replace('swa', 'すぁ').replace('swi', 'すぃ').replace('swu', 'すぅ')
    text = text.replace('swe', 'すぇ').replace('swo', 'すぉ')
    text = text.replace('zwa', 'ずぁ').replace('zwi', 'ずぃ').replace('zwu', 'ずぅ')
    text = text.replace('zwe', 'ずぇ').replace('zwo', 'ずぉ')
    text = text.replace('vya', 'ゔゃ')
    text = text.replace('xtu', 'っ').replace('xtsu', 'っ')
    text = text.replace('ltu', 'っ').replace('ltsu', 'っ')
    text = text.replace('xya', 'ゃ').replace('lya', 'ゃ')
    text = text.replace('xyu', 'ゅ').replace('lyu', 'ゅ')
    text = text.replace('xyo', 'ょ').replace('lyo', 'ょ')
    text = text.replace('wha', 'うぁ').replace('whi', 'うぃ').replace('whu', 'う')
    text = text.replace('whe', 'うぇ').replace('who', 'うぉ')
    text = text.replace('xwa', 'ゎ').replace('lwa', 'ゎ')
    text = text.replace('lyi', 'ぃ').replace('xyi', 'ぃ')
    text = text.replace('lye', 'ぇ').replace('xye', 'ぇ')
    text = text.replace('xka', 'ヵ').replace('lka', 'ヵ')
    text = text.replace('xke', 'ヶ').replace('lke', 'ヶ')
    text = text.replace('tsu', 'つ')
    text = text.replace('nn', 'ん')
    text = text.replace('ja', 'じゃ').replace('ji', 'じ').replace('ju', 'じゅ')
    text = text.replace('je', 'じぇ').replace('jo', 'じょ')
    text = text.replace('ga', 'が').replace('gi', 'ぎ').replace('gu', 'ぐ')
    text = text.replace('ge', 'げ').replace('go', 'ご')
    text = text.replace('za', 'ざ').replace('zi', 'じ').replace('zu', 'ず')
    text = text.replace('ze', 'ぜ').replace('zo', 'ぞ')
    text = text.replace('da', 'だ').replace('di', 'ぢ').replace('du', 'づ')
    text = text.replace('de', 'で').replace('do', 'ど')
    text = text.replace('va', 'ゔぁ').replace('vi', 'ゔぃ').replace('vu', 'ゔ')
    text = text.replace('ve', 'ゔぇ').replace('vo', 'ゔぉ')
    text = text.replace('ba', 'ば').replace('bi', 'び').replace('bu', 'ぶ')
    text = text.replace('be', 'べ').replace('bo', 'ぼ')
    text = text.replace('pa', 'ぱ').replace('pi', 'ぴ').replace('pu', 'ぷ')
    text = text.replace('pe', 'ぺ').replace('po', 'ぽ')
    text = text.replace('ka', 'か').replace('ki', 'き').replace('ku', 'く')
    text = text.replace('ke', 'け').replace('ko', 'こ')
    text = text.replace('qa', 'くぁ').replace('qi', 'くぃ').replace('qu', 'く')
    text = text.replace('qe', 'くぇ').replace('qo', 'くぉ')
    text = text.replace('ca', 'か').replace('cu', 'く').replace('co', 'こ')
    text = text.replace('ci', 'し').replace('ce', 'せ')
    text = text.replace('sa', 'さ').replace('si', 'し').replace('su', 'す')
    text = text.replace('se', 'せ').replace('so', 'そ')
    text = text.replace('ta', 'た').replace('chi', 'ち').replace('ti', 'ち')
    text = text.replace('tu', 'つ').replace('te', 'て').replace('to', 'と')
    text = text.replace('na', 'な').replace('ni', 'に').replace('nu', 'ぬ')
    text = text.replace('ne', 'ね').replace('no', 'の')
    text = text.replace('ha', 'は').replace('hi', 'ひ').replace('fu', 'ふ')
    text = text.replace('hu', 'ふ').replace('he', 'へ').replace('ho', 'ほ')
    text = text.replace('fa', 'ふぁ').replace('fi', 'ふぃ').replace('fe', 'ふぇ')
    text = text.replace('fo', 'ふぉ')
    text = text.replace('ma', 'ま').replace('mi', 'み').replace('mu', 'む')
    text = text.replace('me', 'め').replace('mo', 'も')
    text = text.replace('ra', 'ら').replace('ri', 'り').replace('ru', 'る')
    text = text.replace('re', 'れ').replace('ro', 'ろ')
    text = text.replace('la', 'ら').replace('li', 'り').replace('lu', 'る')
    text = text.replace('le', 'れ').replace('lo', 'ろ')
    text = text.replace('ya', 'や').replace('yu', 'ゆ').replace('yo', 'よ')
    text = text.replace('ye', 'いぇ')
    text = text.replace('wa', 'わ').replace('wi', 'うぃ').replace('wyi', 'ゐ')
    text = text.replace('wu', 'う').replace('wo', 'を')
    text = text.replace('oh', 'おお')
    text = text.replace('xa', 'ぁ').replace('xi', 'ぃ').replace('xu', 'ぅ')
    text = text.replace('xe', 'ぇ').replace('xo', 'ぉ')
    text = text.replace("n'", 'ん').replace('xn', 'ん').replace('m', 'ん')
    text = _convert(text, HEP2KANA)
    ret = []
    for i, char in enumerate(text):
        if char in consonants:
            char = 'っ'
        ret.append(char)
    return ''.join(ret)


def alphabet2kata(text):
    """Convert alphabets to Katakana

    Parameters
    ----------
    text : str
        Roman-input-style alphabets string.

    Return
    ------
    str
        Katakana string.

    Examples
    --------
    >>> print(jaconv.alphabet2kata('mamisan'))
    マミサン
    """
    return hira2kata(alphabet2kana(text))
