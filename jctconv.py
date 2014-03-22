# -*- coding: utf-8 -*-
import unicodedata

"""
jctconv 0.0.6 - 全角・半角・ひらがな・カタカナ等相互変換モジュール

Author:
    Yukino Ikegami

Lisence:
    MIT License

Usage:
    import jctconv
    text = jctconv.hira2kata(text, [ignore]) # ひらがなを全角カタカナに変換
    text = jctconv.hira2hkata(text, [ignore]) # ひらがなを半角カタカナに変換
    text = jctconv.kata2hira(text, [ignore]) # 全角カタカナをひらがなに変換
    text = jctconv.h2z(text, [mode, ignore]) # 半角文字を全角文字に変換
    text = jctconv.z2h(text, [mode, ignore]) # 全角文字を半角文字に変換
    text = jctconv.normalize(text, [nomalizemode]) # 半角カナを全角カナへ、全角英数字を半角英数字に変換

    modeで変換対象文字種(ALL, ASCII, DIGIT, KANA)を組み合わせて指定可能
    nomalizemodeはNFC, NFKC, NKD, NFKDから指定可能
    ignoreで変換除外文字を指定可能
"""

HIRAGANA = list(u'ぁあぃいぅうぇえぉおかがきぎくぐけげこごさざしじすずせぜそぞただちぢっつづてでとどなにぬねのはばぱひびぴふぶぷへべぺほぼぽまみむめもゃやゅゆょよらりるれろわをんーゎゐゑゕゖゔ')

HALF_ASCII = list(u'!"#$%&\'()*+,-./:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~ ')
HALF_DIGIT = list(u'0123456789')
HALF_KANA_SEION = list(u'ｧｱｨｲｩｳｪｴｫｵｶｷｸｹｺｻｼｽｾｿﾀﾁｯﾂﾃﾄﾅﾆﾇﾈﾉﾊﾋﾌﾍﾎﾏﾐﾑﾒﾓｬﾔｭﾕｮﾖﾗﾘﾙﾚﾛﾜｦﾝｰヮヰヱヵヶ')
HALF_KANA = [u'ｧ',u'ｱ',u'ｨ',u'ｲ',u'ｩ',u'ｳ',u'ｪ',u'ｴ',u'ｫ',u'ｵ',u'ｶ',u'ｶﾞ',u'ｷ',u'ｷﾞ',u'ｸ',u'ｸﾞ',u'ｹ',u'ｹﾞ',u'ｺ',u'ｺﾞ',u'ｻ',u'ｻﾞ',u'ｼ',u'ｼﾞ',u'ｽ',u'ｽﾞ',u'ｾ',u'ｾﾞ',u'ｿ',u'ｿﾞ',u'ﾀ',u'ﾀﾞ',u'ﾁ',u'ﾁﾞ',u'ｯ',u'ﾂ',u'ﾂﾞ',u'ﾃ',u'ﾃﾞ',u'ﾄ',u'ﾄﾞ',u'ﾅ',u'ﾆ',u'ﾇ',u'ﾈ',u'ﾉ',u'ﾊ',u'ﾊﾞ',u'ﾊﾟ',u'ﾋ',u'ﾋﾞ',u'ﾋﾟ',u'ﾌ',u'ﾌﾞ',u'ﾌﾟ',u'ﾍ',u'ﾍﾞ',u'ﾍﾟ',u'ﾎ',u'ﾎﾞ',u'ﾎﾟ',u'ﾏ',u'ﾐ',u'ﾑ',u'ﾒ',u'ﾓ',u'ｬ',u'ﾔ',u'ｭ',u'ﾕ',u'ｮ',u'ﾖ',u'ﾗ',u'ﾘ',u'ﾙ',u'ﾚ',u'ﾛ',u'ﾜ',u'ｦ',u'ﾝ',u'ｰ',u'ヮ',u'ヰ',u'ヱ',u'ヵ',u'ヶ',u'ｳﾞ']
FULL_ASCII = list(u'！＂＃＄％＆＇（）＊＋，－．／：；＜＝＞？＠ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ［＼］＾＿｀ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ｛｜｝～　')
FULL_DIGIT = list(u'０１２３４５６７８９')
FULL_KANA = list(u'ァアィイゥウェエォオカガキギクグケゲコゴサザシジスズセゼソゾタダチヂッツヅテデトドナニヌネノハバパヒビピフブプヘベペホボポマミムメモャヤュユョヨラリルレロワヲンーヮヰヱヵヶヴ')
FULL_KANA_SEION = list(u'ァアィイゥウェエォオカキクケコサシスセソタチッツテトナニヌネノハヒフヘホマミムメモャヤュユョヨラリルレロワヲンーヮヰヱヵヶ')

def to_ord_dict(list_from, list_to):
    list_from = [ord(char) for char in list_from]
    return dict(zip(list_from, list_to))

H2K_TABLE = to_ord_dict(HIRAGANA, FULL_KANA)
H2HK_TABLE = to_ord_dict(HIRAGANA, HALF_KANA)
K2H_TABLE = to_ord_dict(FULL_KANA, HIRAGANA)

H2Z_A = to_ord_dict(HALF_ASCII, FULL_ASCII)
H2Z_AD = to_ord_dict(HALF_ASCII+HALF_DIGIT, FULL_ASCII+FULL_DIGIT)
H2Z_AK = to_ord_dict(HALF_ASCII+HALF_KANA_SEION, FULL_ASCII+FULL_KANA_SEION)
H2Z_D = to_ord_dict(HALF_DIGIT, FULL_DIGIT)
H2Z_K = to_ord_dict(HALF_KANA_SEION, FULL_KANA_SEION)
H2Z_DK = to_ord_dict(HALF_DIGIT+HALF_KANA_SEION, FULL_DIGIT+FULL_KANA_SEION)
H2Z_ALL = to_ord_dict(HALF_ASCII+HALF_DIGIT+HALF_KANA_SEION, FULL_ASCII+FULL_DIGIT+FULL_KANA_SEION)

Z2H_A = to_ord_dict(FULL_ASCII, HALF_ASCII)
Z2H_AD = to_ord_dict(FULL_ASCII+FULL_DIGIT, HALF_ASCII+HALF_DIGIT)
Z2H_AK = to_ord_dict(FULL_ASCII+FULL_KANA, HALF_ASCII+HALF_KANA)
Z2H_D = to_ord_dict(FULL_DIGIT, HALF_DIGIT)
Z2H_K = to_ord_dict(FULL_KANA, HALF_KANA)
Z2H_DK = to_ord_dict(FULL_DIGIT+FULL_KANA, HALF_DIGIT+HALF_KANA)
Z2H_ALL = to_ord_dict(FULL_ASCII+FULL_DIGIT+FULL_KANA, HALF_ASCII+HALF_DIGIT+HALF_KANA)


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
H2K = hira2kata # hira2kataの別名

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
H2hK = hira2hkata # hira2hkataの別名

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
K2H = kata2hira # kata2hiraの別名

def hankaku2zenkaku(text, mode='KANA', ignore='', kana=True, ascii=False, digit=False):
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
        return text.replace(u"ｶﾞ",u"ガ").replace(u"ｷﾞ",u"ギ").replace(u"ｸﾞ",u"グ").replace(u"ｹﾞ",u"ゲ").replace(u"ｺﾞ",u"ゴ").replace(u"ｻﾞ",u"ザ").replace(u"ｼﾞ",u"ジ").replace(u"ｽﾞ",u"ズ").replace(u"ｾﾞ",u"ゼ").replace(u"ｿﾞ",u"ゾ").replace(u"ﾀﾞ",u"ダ").replace(u"ﾁﾞ",u"ヂ").replace(u"ﾂﾞ",u"ヅ").replace(u"ﾃﾞ",u"デ").replace(u"ﾄﾞ",u"ド").replace(u"ﾊﾞ",u"バ").replace(u"ﾋﾞ",u"ビ").replace(u"ﾌﾞ",u"ブ").replace(u"ﾍﾞ",u"ベ").replace(u"ﾎﾞ",u"ボ").replace(u"ﾊﾟ",u"パ").replace(u"ﾋﾟ",u"ピ").replace(u"ﾌﾟ",u"プ").replace(u"ﾍﾟ",u"ペ").replace(u"ﾎﾟ",u"ポ").replace(u"ｳﾞ",u"ヴ")

    mode = mode.upper()
    if 'KANA' in mode:
        kana = True
    if 'ASCII' in mode:
        ascii = True
    if 'DIGIT' in mode:
        digit = True
    if (kana and ascii and digit) or mode == 'ALL':
        h2z_hash = H2Z_ALL
        text = _conv_dakuten(text)
    else:
        if ascii:
            if digit:
                if kana:
                    h2z_hash = H2Z_ALL
                    text = _conv_dakuten(text)
                else:
                    h2z_hash = H2Z_AD
            elif kana:
                h2z_hash = H2Z_AK
                text = _conv_dakuten(text)
            else:
                h2z_hash = H2Z_A
        elif digit:
            if kana:
                h2z_hash = H2Z_DK
                text = _conv_dakuten(text)
            else:
                h2z_hash = H2Z_D
        else:
            h2z_hash = H2Z_K
            text = _conv_dakuten(text)
    h2z_hash = _exclude_ignorechar(ignore, h2z_hash)
    return _convert(text, h2z_hash)
h2z = hankaku2zenkaku # hankaku2zenkakuの別名

def zenkaku2hankaku(text, mode='', ignore='', kana=True, ascii=False, digit=False):
    """Convert Full-width (Zenkaku) Katakana to Half-width (Hankaku) Katakana

    Params:
        <unicode> text
        <unicode> ignore
    Return:
        <unicode> converted_text
    """
    mode = mode.upper()
    if 'KANA' in mode:
        kana = True
    if 'ASCII' in mode:
        ascii = True
    if 'DIGIT' in mode:
        digit = True
    if (kana and ascii and digit) or mode == 'ALL':
        z2h_hash = Z2H_ALL
    else:
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
z2h = zenkaku2hankaku # zenkaku2hankakuの別名

def normalize(text, mode='NFKC', ignore=''):
    """Convert Half-width (Hankaku) Katakana to Full-width (Zenkaku) Katakana,
    Full-width (Zenkaku) ASCII and DIGIT to Half-width (Hankaku) ASCII and DIGIT
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
    for character in ignore:
        conv_hash[ord(character)] = character
    return conv_hash

def _convert(text, conv_hash):
    return text.translate(conv_hash)
