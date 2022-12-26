# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re

from .compat import map, zip

HIRAGANA = list('ぁあぃいぅうぇえぉおかがきぎくぐけげこごさざしじすず'
                'せぜそぞただちぢっつづてでとどなにぬねのはばぱひびぴ'
                'ふぶぷへべぺほぼぽまみむめもゃやゅゆょよらりるれろわ'
                'をんーゎゐゑゕゖゔゝゞ・「」。、')
HALF_ASCII = list('!"#$%&\'()*+,-./:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ'
                  '[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~ ')
HALF_DIGIT = list('0123456789')
HALF_KANA_SEION = list('ｧｱｨｲｩｳｪｴｫｵｶｷｸｹｺｻｼｽｾｿﾀﾁｯﾂﾃﾄﾅﾆﾇﾈﾉﾊﾋﾌﾍﾎﾏﾐﾑﾒﾓｬﾔｭﾕｮﾖ'
                       'ﾗﾘﾙﾚﾛﾜｦﾝｰヮヰヱヵヶヽヾ･｢｣｡､')
HALF_KANA = ['ｧ', 'ｱ', 'ｨ', 'ｲ', 'ｩ', 'ｳ', 'ｪ', 'ｴ', 'ｫ', 'ｵ',
             'ｶ', 'ｶﾞ', 'ｷ', 'ｷﾞ', 'ｸ', 'ｸﾞ', 'ｹ', 'ｹﾞ', 'ｺ',
             'ｺﾞ', 'ｻ', 'ｻﾞ', 'ｼ', 'ｼﾞ', 'ｽ', 'ｽﾞ', 'ｾ', 'ｾﾞ',
             'ｿ', 'ｿﾞ', 'ﾀ', 'ﾀﾞ', 'ﾁ', 'ﾁﾞ', 'ｯ', 'ﾂ', 'ﾂﾞ',
             'ﾃ', 'ﾃﾞ', 'ﾄ', 'ﾄﾞ', 'ﾅ', 'ﾆ', 'ﾇ', 'ﾈ', 'ﾉ', 'ﾊ',
             'ﾊﾞ', 'ﾊﾟ', 'ﾋ', 'ﾋﾞ', 'ﾋﾟ', 'ﾌ', 'ﾌﾞ', 'ﾌﾟ', 'ﾍ',
             'ﾍﾞ', 'ﾍﾟ', 'ﾎ', 'ﾎﾞ', 'ﾎﾟ', 'ﾏ', 'ﾐ', 'ﾑ', 'ﾒ',
             'ﾓ', 'ｬ', 'ﾔ', 'ｭ', 'ﾕ', 'ｮ', 'ﾖ', 'ﾗ', 'ﾘ', 'ﾙ',
             'ﾚ', 'ﾛ', 'ﾜ', 'ｦ', 'ﾝ', 'ｰ',
             'ヮ', 'ヰ', 'ヱ', 'ヵ', 'ヶ', 'ｳﾞ', 'ヽ', 'ヾ', '･',
             '｢', '｣', '｡', '､']
FULL_ASCII = list('！＂＃＄％＆＇（）＊＋，－．／：；＜＝＞？＠'
                  'ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ'
                  '［＼］＾＿｀ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔ'
                  'ｕｖｗｘｙｚ｛｜｝～　')
FULL_DIGIT = list('０１２３４５６７８９')
FULL_KANA = list('ァアィイゥウェエォオカガキギクグケゲコゴサザシジスズセゼソ'
                 'ゾタダチヂッツヅテデトドナニヌネノハバパヒビピフブプヘベペ'
                 'ホボポマミムメモャヤュユョヨラリルレロワヲンーヮヰヱヵヶヴ'
                 'ヽヾ・「」。、')
FULL_KANA_SEION = list('ァアィイゥウェエォオカキクケコサシスセソタチッツテト'
                       'ナニヌネノハヒフヘホマミムメモャヤュユョヨラリルレロ'
                       'ワヲンーヮヰヱヵヶヽヾ・「」。、')
HEPBURN = list('aiueoaiueon')
HEPBURN_KANA = list('ぁぃぅぇぉあいうえおん')
SMALL_KANA = list('ぁぃぅぇぉゃゅょっァィゥェォヵヶャュョッ')
SMALL_KANA_NORMALIZED = list('あいうえおやゆよつアイウエオカケヤユヨツ')


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
SMALL_KANA_ORD = _to_ord_list(SMALL_KANA)


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
KANA2HEP = _to_dict(_to_ord_list(HEPBURN_KANA), HEPBURN)
HEP2KANA = _to_dict(_to_ord_list(HEPBURN), HEPBURN_KANA)

JULIUS_LONG_VOWEL = tuple(
    (
        (re.compile('( a){2,}'), ' a:'),
        (re.compile('( i){2,}'), ' i:'),
        (re.compile('( u){2,}'), ' u:'),
        (re.compile('( e){2,}'), ' e:'),
        (re.compile('( o){2,}'), ' o:')
    )
)

SMALL_KANA2BIG_KANA = _to_dict(SMALL_KANA_ORD, SMALL_KANA_NORMALIZED)

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
del HEPBURN
del HEPBURN_KANA
del SMALL_KANA
del SMALL_KANA_ORD
del SMALL_KANA_NORMALIZED
