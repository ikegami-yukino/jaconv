# -*- coding: utf-8 -*-
from .compat import map, zip

HIRAGANA = list(u'ぁあぃいぅうぇえぉおかがきぎくぐけげこごさざしじすず'
                u'せぜそぞただちぢっつづてでとどなにぬねのはばぱひびぴ'
                u'ふぶぷへべぺほぼぽまみむめもゃやゅゆょよらりるれろわ'
                u'をんーゎゐゑゕゖゔゝゞ・「」。、')
HALF_ASCII = list(u'!"#$%&\'()*+,-./:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ'
                  u'[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~ ')
HALF_DIGIT = list(u'0123456789')
HALF_KANA_SEION = list(u'ｧｱｨｲｩｳｪｴｫｵｶｷｸｹｺｻｼｽｾｿﾀﾁｯﾂﾃﾄﾅﾆﾇﾈﾉﾊﾋﾌﾍﾎﾏﾐﾑﾒﾓｬﾔｭﾕｮﾖ'
                       u'ﾗﾘﾙﾚﾛﾜｦﾝｰヮヰヱヵヶヽヾ･｢｣｡､')
HALF_KANA = [u'ｧ', u'ｱ', u'ｨ', u'ｲ', u'ｩ', u'ｳ', u'ｪ', u'ｴ', u'ｫ', u'ｵ',
             u'ｶ', u'ｶﾞ', u'ｷ', u'ｷﾞ', u'ｸ', u'ｸﾞ', u'ｹ', u'ｹﾞ', u'ｺ',
             u'ｺﾞ', u'ｻ', u'ｻﾞ', u'ｼ', u'ｼﾞ', u'ｽ', u'ｽﾞ', u'ｾ', u'ｾﾞ',
             u'ｿ', u'ｿﾞ', u'ﾀ', u'ﾀﾞ', u'ﾁ', u'ﾁﾞ', u'ｯ', u'ﾂ', u'ﾂﾞ',
             u'ﾃ', u'ﾃﾞ', u'ﾄ', u'ﾄﾞ', u'ﾅ', u'ﾆ', u'ﾇ', u'ﾈ', u'ﾉ', u'ﾊ',
             u'ﾊﾞ', u'ﾊﾟ', u'ﾋ', u'ﾋﾞ', u'ﾋﾟ', u'ﾌ', u'ﾌﾞ', u'ﾌﾟ', u'ﾍ',
             u'ﾍﾞ', u'ﾍﾟ', u'ﾎ', u'ﾎﾞ', u'ﾎﾟ', u'ﾏ', u'ﾐ', u'ﾑ', u'ﾒ',
             u'ﾓ', u'ｬ', u'ﾔ', u'ｭ', u'ﾕ', u'ｮ', u'ﾖ', u'ﾗ', u'ﾘ', u'ﾙ',
             u'ﾚ', u'ﾛ', u'ﾜ', u'ｦ', u'ﾝ', u'ｰ',
             u'ヮ', u'ヰ', u'ヱ', u'ヵ', u'ヶ', u'ｳﾞ', u'ヽ', u'ヾ', u'･',
             u'｢', u'｣', u'｡', u'､']
FULL_ASCII = list(u'！＂＃＄％＆＇（）＊＋，－．／：；＜＝＞？＠'
                  u'ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ'
                  u'［＼］＾＿｀ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔ'
                  u'ｕｖｗｘｙｚ｛｜｝～　')
FULL_DIGIT = list(u'０１２３４５６７８９')
FULL_KANA = list(u'ァアィイゥウェエォオカガキギクグケゲコゴサザシジスズセゼソ'
                 u'ゾタダチヂッツヅテデトドナニヌネノハバパヒビピフブプヘベペ'
                 u'ホボポマミムメモャヤュユョヨラリルレロワヲンーヮヰヱヵヶヴ'
                 u'ヽヾ・「」。、')
FULL_KANA_SEION = list(u'ァアィイゥウェエォオカキクケコサシスセソタチッツテト'
                       u'ナニヌネノハヒフヘホマミムメモャヤュユョヨラリルレロ'
                       u'ワヲンーヮヰヱヵヶヽヾ・「」。、')


def _to_ord_list(chars):
    return list(map(ord, chars))

HIRAGANA_ORD = _to_ord_list(HIRAGANA)
FULL_KANA_ORD = _to_ord_list(FULL_KANA)
HALF_ASCII_ORD = _to_ord_list(HALF_ASCII)
FULL_ASCII_ORD = _to_ord_list(FULL_ASCII)
HALF_DIGIT_ORD = _to_ord_list(HALF_DIGIT)
FULL_DIGIT_ORD = _to_ord_list(FULL_DIGIT)
HALF_KANA_SEION_ORD = _to_ord_list(HALF_KANA_SEION)
FULL_KANA_SEION_ORD = _to_ord_list(FULL_KANA_SEION)


def _to_dict(_from, _to):
    return dict(zip(_from, _to))


H2K_TABLE = _to_dict(HIRAGANA_ORD, FULL_KANA)
H2HK_TABLE = _to_dict(HIRAGANA_ORD, HALF_KANA)
K2H_TABLE = _to_dict(FULL_KANA_ORD, HIRAGANA)

H2Z_A = _to_dict(HALF_ASCII_ORD, FULL_ASCII)
H2Z_AD = _to_dict(HALF_ASCII_ORD+HALF_DIGIT_ORD, FULL_ASCII+FULL_DIGIT)
H2Z_AK = _to_dict(HALF_ASCII_ORD+HALF_KANA_SEION_ORD,
                  FULL_ASCII+FULL_KANA_SEION)
H2Z_D = _to_dict(HALF_DIGIT_ORD, FULL_DIGIT)
H2Z_K = _to_dict(HALF_KANA_SEION_ORD, FULL_KANA_SEION)
H2Z_DK = _to_dict(HALF_DIGIT_ORD+HALF_KANA_SEION_ORD,
                  FULL_DIGIT+FULL_KANA_SEION)
H2Z_ALL = _to_dict(HALF_ASCII_ORD+HALF_DIGIT_ORD+HALF_KANA_SEION_ORD,
                   FULL_ASCII+FULL_DIGIT+FULL_KANA_SEION)

Z2H_A = _to_dict(FULL_ASCII_ORD, HALF_ASCII)
Z2H_AD = _to_dict(FULL_ASCII_ORD+FULL_DIGIT_ORD, HALF_ASCII+HALF_DIGIT)
Z2H_AK = _to_dict(FULL_ASCII_ORD+FULL_KANA_ORD, HALF_ASCII+HALF_KANA)
Z2H_D = _to_dict(FULL_DIGIT_ORD, HALF_DIGIT)
Z2H_K = _to_dict(FULL_KANA_ORD, HALF_KANA)
Z2H_DK = _to_dict(FULL_DIGIT_ORD+FULL_KANA_ORD, HALF_DIGIT+HALF_KANA)
Z2H_ALL = _to_dict(FULL_ASCII_ORD+FULL_DIGIT_ORD+FULL_KANA_ORD,
                   HALF_ASCII+HALF_DIGIT+HALF_KANA)

del _to_ord_list
del _to_dict
del HIRAGANA_ORD
del HIRAGANA
del HALF_KANA
del FULL_KANA_ORD
del FULL_KANA
del HALF_ASCII_ORD
del HALF_ASCII
del FULL_ASCII_ORD
del FULL_ASCII
del HALF_DIGIT_ORD
del HALF_DIGIT
del FULL_DIGIT_ORD
del FULL_DIGIT
del HALF_KANA_SEION_ORD
del HALF_KANA_SEION
del FULL_KANA_SEION_ORD
del FULL_KANA_SEION
