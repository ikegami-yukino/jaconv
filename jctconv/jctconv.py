# -*- coding: utf-8 -*-
import unicodedata

HIRAGANA = list(u'ぁあぃいぅうぇえぉおかがきぎくぐけげこごさざしじすず'
                u'せぜそぞただちぢっつづてでとどなにぬねのはばぱひびぴ'
                u'ふぶぷへべぺほぼぽまみむめもゃやゅゆょよらりるれろわ'
                u'をんーゎゐゑゕゖゔ')
HALF_ASCII = list(u'!"#$%&\'()*+,-./:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ'
                  u'[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~ ')
HALF_DIGIT = list(u'0123456789'),
HALF_KANA_SEION = list(u'ｧｱｨｲｩｳｪｴｫｵｶｷｸｹｺｻｼｽｾｿﾀﾁｯﾂﾃﾄﾅﾆﾇﾈﾉﾊﾋﾌﾍﾎﾏﾐﾑﾒﾓｬﾔｭﾕｮﾖ'
                       u'ﾗﾘﾙﾚﾛﾜｦﾝｰヮヰヱヵヶ')
HALF_KANA = [u'ｧ', u'ｱ', u'ｨ', u'ｲ', u'ｩ', u'ｳ', u'ｪ', u'ｴ', u'ｫ', u'ｵ',
             u'ｶ', u'ｶﾞ', u'ｷ', u'ｷﾞ', u'ｸ', u'ｸﾞ', u'ｹ', u'ｹﾞ', u'ｺ',
             u'ｺﾞ', u'ｻ', u'ｻﾞ', u'ｼ', u'ｼﾞ', u'ｽ', u'ｽﾞ', u'ｾ', u'ｾﾞ',
             u'ｿ', u'ｿﾞ', u'ﾀ', u'ﾀﾞ', u'ﾁ', u'ﾁﾞ', u'ｯ', u'ﾂ', u'ﾂﾞ',
             u'ﾃ', u'ﾃﾞ', u'ﾄ', u'ﾄﾞ', u'ﾅ', u'ﾆ', u'ﾇ', u'ﾈ', u'ﾉ', u'ﾊ',
             u'ﾊﾞ', u'ﾊﾟ', u'ﾋ', u'ﾋﾞ', u'ﾋﾟ', u'ﾌ', u'ﾌﾞ', u'ﾌﾟ', u'ﾍ',
             u'ﾍﾞ', u'ﾍﾟ', u'ﾎ', u'ﾎﾞ', u'ﾎﾟ', u'ﾏ', u'ﾐ', u'ﾑ', u'ﾒ',
             u'ﾓ', u'ｬ', u'ﾔ', u'ｭ', u'ﾕ', u'ｮ', u'ﾖ', u'ﾗ', u'ﾘ', u'ﾙ',
             u'ﾚ', u'ﾛ', u'ﾜ', u'ｦ', u'ﾝ', u'ｰ',
             u'ヮ', u'ヰ', u'ヱ', u'ヵ', u'ヶ', u'ｳﾞ']
FULL_ASCII = list(u'！＂＃＄％＆＇（）＊＋，－．／：；＜＝＞？＠'
                  u'ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ'
                  u'［＼］＾＿｀ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔ'
                  u'ｕｖｗｘｙｚ｛｜｝～　')
FULL_DIGIT = list(u'０１２３４５６７８９')
FULL_KANA = list(u'ァアィイゥウェエォオカガキギクグケゲコゴサザシジスズセゼソ'
                 u'ゾタダチヂッツヅテデトドナニヌネノハバパヒビピフブプヘベペ'
                 u'ホボポマミムメモャヤュユョヨラリルレロワヲンーヮヰヱヵヶヴ'),
FULL_KANA_SEION = list(u'ァアィイゥウェエォオカキクケコサシスセソタチッツテト'
                       u'ナニヌネノハヒフヘホマミムメモャヤュユョヨラリルレロ'
                       u'ワヲンーヮヰヱヵヶ')


def _to_ord_dict(_from, _to):
    _from = map(ord, _from)
    return dict(zip(map(ord, _from), _to))

H2K_TABLE = _to_ord_dict(HIRAGANA, FULL_KANA)
H2HK_TABLE = _to_ord_dict(HIRAGANA, HALF_KANA)
K2H_TABLE = _to_ord_dict(FULL_KANA, HIRAGANA)

H2Z_A = _to_ord_dict(HALF_ASCII, FULL_ASCII)
H2Z_AD = _to_ord_dict(HALF_ASCII+HALF_DIGIT, FULL_ASCII+FULL_DIGIT)
H2Z_AK = _to_ord_dict(HALF_ASCII+HALF_KANA_SEION, FULL_ASCII+FULL_KANA_SEION)
H2Z_D = _to_ord_dict(HALF_DIGIT, FULL_DIGIT)
H2Z_K = _to_ord_dict(HALF_KANA_SEION, FULL_KANA_SEION)
H2Z_DK = _to_ord_dict(HALF_DIGIT+HALF_KANA_SEION, FULL_DIGIT+FULL_KANA_SEION)
H2Z_ALL = _to_ord_dict(HALF_ASCII+HALF_DIGIT+HALF_KANA_SEION,
                       FULL_ASCII+FULL_DIGIT+FULL_KANA_SEION)

Z2H_A = _to_ord_dict(FULL_ASCII, HALF_ASCII)
Z2H_AD = _to_ord_dict(FULL_ASCII+FULL_DIGIT, HALF_ASCII+HALF_DIGIT)
Z2H_AK = _to_ord_dict(FULL_ASCII+FULL_KANA, HALF_ASCII+HALF_KANA)
Z2H_D = _to_ord_dict(FULL_DIGIT, HALF_DIGIT)
Z2H_K = _to_ord_dict(FULL_KANA, HALF_KANA)
Z2H_DK = _to_ord_dict(FULL_DIGIT+FULL_KANA, HALF_DIGIT+HALF_KANA)
Z2H_ALL = _to_ord_dict(FULL_ASCII+FULL_DIGIT+FULL_KANA,
                       HALF_ASCII+HALF_DIGIT+HALF_KANA)


def hira2kata(text, ignore=''):
    """Convert Hiragana to Full-width (Zenkaku) Katakana

    Params:
        <unicode> text
        <unicode> ignore
    Return:
        <unicode> converted_text
    """
    h2k_hash = _exclude_ignorechar(ignore, H2K_TABLE)
    return _convert(text, h2k_hash)


def hira2hkata(text, ignore=''):
    """Convert Hiragana to Half-width (Hankaku) Katakana

    Params:
        <unicode> text
        <unicode> ignore
    Return:
        <unicode> converted_text
    """
    h2hk_hash = _exclude_ignorechar(ignore, H2HK_TABLE)
    return _convert(text, h2hk_hash)


def kata2hira(text, ignore=''):
    """Convert Full-width Katakana to Hiragana

    Params:
        <unicode> text
        <unicode> ignore
    Return:
        <unicode> converted_text
    """
    k2h_hash = _exclude_ignorechar(ignore, K2H_TABLE)
    return _convert(text, k2h_hash)


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
                h2z_hash = H2Z_ALL
            else:
                h2z_hash = H2Z_AD
        elif kana:
            h2z_hash = H2Z_AK
        else:
            h2z_hash = H2Z_A
    elif digit:
        if kana:
            h2z_hash = H2Z_DK
        else:
            h2z_hash = H2Z_D
    else:
        h2z_hash = H2Z_K
    if kana:
        text = _conv_dakuten(text)
    h2z_hash = _exclude_ignorechar(ignore, h2z_hash)
    return _convert(text, h2z_hash)


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
                z2h_hash = Z2H_ALL
            else:
                z2h_hash = Z2H_AD
        elif kana:
            z2h_hash = Z2H_AK
        else:
            z2h_hash = Z2H_A
    elif digit:
        if kana:
            z2h_hash = Z2H_DK
        else:
            z2h_hash = Z2H_D
    else:
        z2h_hash = Z2H_K
    z2h_hash = _exclude_ignorechar(ignore, z2h_hash)
    return _convert(text, z2h_hash)


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


def _exclude_ignorechar(ignore, conv_hash):
    for character in map(ord, ignore):
        conv_hash[character] = character
    return conv_hash


def _convert(text, conv_hash):
    return text.translate(conv_hash)
