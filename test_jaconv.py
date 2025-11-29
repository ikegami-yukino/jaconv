# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from functools import partial

import jaconv

HIRAGANA = ('ぁあぃいぅうぇえぉおかがきぎくぐけげこごさざしじすずせぜそぞた',
            'だちぢっつづてでとどなにぬねのはばぱひびぴふぶぷへべぺほぼぽま',
            'みむめもゃやゅゆょよらりるれろわをんーゎゐゑゕゖゔゝゞ・「」。、')
FULL_KANA = ('ァアィイゥウェエォオカガキギクグケゲコゴサザシジスズセゼソゾタ',
             'ダチヂッツヅテデトドナニヌネノハバパヒビピフブプヘベペホボポマ',
             'ミムメモャヤュユョヨラリルレロワヲンーヮヰヱヵヶヴヽヾ・「」。、')
HALF_KANA = ('ｧｱｨｲｩｳｪｴｫｵｶｶﾞｷｷﾞｸｸﾞｹｹﾞｺｺﾞｻｻﾞｼｼﾞｽｽﾞｾｾﾞｿｿﾞﾀ',
             'ﾀﾞﾁﾁﾞｯﾂﾂﾞﾃﾃﾞﾄﾄﾞﾅﾆﾇﾈﾉﾊﾊﾞﾊﾟﾋﾋﾞﾋﾟﾌﾌﾞﾌﾟﾍﾍﾞﾍﾟﾎﾎﾞﾎﾟﾏ',
             'ﾐﾑﾒﾓｬﾔｭﾕｮﾖﾗﾘﾙﾚﾛﾜｦﾝｰヮヰヱヵヶｳﾞヽヾ･｢｣｡､')
HALF_ASCII = ('!"#$%&\'()*+,-./:;<=>?@[\\]^_`~',
              'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
              'abcdefghijklmnopqrstuvwxyz{|} ')
HALF_DIGIT = '0123456789'
FULL_ASCII = ('！＂＃＄％＆＇（）＊＋，－．／：；＜＝＞？＠［＼］＾＿｀～',
              'ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ',
              'ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ｛｜｝　')
FULL_DIGIT = '０１２３４５６７８９'


def _compare(mathod, lhs, rhs):
    for i in range(len(lhs)):
        assert mathod(lhs[i]) == rhs[i]


def _concat(*iterables):
    result = ''
    for iterable in iterables:
        result += ''.join(iterable)
    return result


def test_hira2kata():
    assert jaconv.hira2kata('ともえまみ') == 'トモエマミ'
    assert jaconv.hira2kata('まどまぎ', ignore='ど') == 'マどマギ'
    _compare(jaconv.hira2kata, HIRAGANA, FULL_KANA)


def test_hira2hkata():
    assert jaconv.hira2hkata('ともえまみ') == 'ﾄﾓｴﾏﾐ'
    assert jaconv.hira2hkata('ともえまみ', ignore='み') == 'ﾄﾓｴﾏみ'
    _compare(jaconv.hira2hkata, HIRAGANA, HALF_KANA)


def test_kata2hira():
    assert jaconv.kata2hira('巴マミ') == '巴まみ'
    assert jaconv.kata2hira('マミサン', ignore='ン') == 'まみさン'
    _compare(jaconv.kata2hira, FULL_KANA, HIRAGANA)


def test_h2z():
    assert jaconv.h2z('ﾃｨﾛﾌｨﾅｰﾚ') == 'ティロフィナーレ'
    assert jaconv.h2z('ﾃｨﾛﾌｨﾅｰﾚ', ignore='ｨ') == 'テｨロフｨナーレ'
    _compare(jaconv.h2z, HALF_KANA, FULL_KANA)
    _compare(partial(jaconv.h2z, ascii=True), HALF_ASCII, FULL_ASCII)
    _compare(partial(jaconv.h2z, digit=True), HALF_DIGIT, FULL_DIGIT)

    for ascii in (True, False):
        for digit in (True, False):
            for kana in (True, False):
                before = _concat(FULL_KANA,  HALF_KANA,
                                 FULL_ASCII, HALF_ASCII,
                                 FULL_DIGIT, HALF_DIGIT)
                after = _concat(FULL_KANA,  FULL_KANA  if kana  else HALF_KANA,
                                FULL_ASCII, FULL_ASCII if ascii else HALF_ASCII,
                                FULL_DIGIT, FULL_DIGIT if digit else HALF_DIGIT)
                converted = jaconv.h2z(before,
                                       ascii=ascii, digit=digit, kana=kana)
                assert converted == after


def test_z2h():
    assert jaconv.z2h('ティロフィナーレ') == 'ﾃｨﾛﾌｨﾅｰﾚ'
    assert jaconv.z2h('ティロフィナーレ', ignore='ィ') == 'ﾃィﾛﾌィﾅｰﾚ'
    _compare(partial(jaconv.z2h, kana=True), FULL_KANA, HALF_KANA)
    _compare(partial(jaconv.z2h, ascii=True), FULL_ASCII, HALF_ASCII)
    _compare(partial(jaconv.z2h, digit=True), FULL_DIGIT, HALF_DIGIT)

    for ascii in (True, False):
        for digit in (True, False):
            for kana in (True, False):
                before = _concat(FULL_KANA,  HALF_KANA,
                                 FULL_ASCII, HALF_ASCII,
                                 FULL_DIGIT, HALF_DIGIT)
                after = _concat(HALF_KANA  if kana  else FULL_KANA,  HALF_KANA,
                                HALF_ASCII if ascii else FULL_ASCII, HALF_ASCII,
                                HALF_DIGIT if digit else FULL_DIGIT, HALF_DIGIT)
                converted = jaconv.z2h(before,
                                       ascii=ascii, digit=digit, kana=kana)
                assert converted == after


def test_normalize():
    assert jaconv.normalize('ﾃｨﾛ･フィナ〜レ', 'NFKC') == 'ティロ・フィナーレ'
    assert jaconv.normalize(_concat(HALF_KANA, FULL_DIGIT), 'NFKC') == ''.join(FULL_KANA)+''.join(HALF_DIGIT)


def test_kana2alphabet():
    assert jaconv.kana2alphabet('まみさん') == 'mamisan'
    assert jaconv.kana2alphabet('はっとり') == 'hattori'
    assert jaconv.kana2alphabet('はっ') == 'haxtsu'
    assert jaconv.kana2alphabet('ぽっ') == 'poxtsu'
    assert jaconv.kana2alphabet('ふぁふぃふぇふぉ') == 'fafifefo'
    assert jaconv.kana2alphabet('っって') == 'xtsutte'


def test_alphabet2kana():
    assert jaconv.alphabet2kana('mamisan') == 'まみさん'
    assert jaconv.alphabet2kana('doggu doguu') == 'どっぐ どぐう'
    assert jaconv.alphabet2kana('botchi') == 'ぼっち'
    assert jaconv.alphabet2kana('fainarufantaji-') == 'ふぁいなるふぁんたじー'
    assert jaconv.alphabet2kana('atsui') == 'あつい'
    assert jaconv.alphabet2kana('itoh') == 'いとう'
    assert jaconv.alphabet2kana('ohtaku') == 'おおたく'
    assert jaconv.alphabet2kana('namba') == 'なんば'


def test_alphabet2julius():
    assert jaconv.hiragana2julius('てんき') == 't e N k i'
    assert jaconv.hiragana2julius('やったー') == 'y a q t a:'
    assert jaconv.hiragana2julius('かわいいいいい') == 'k a w a i:'
    assert jaconv.hiragana2julius('やろうぜ') == 'y a r o: z e'
    assert jaconv.hiragana2julius('てんきすごくいいいいいい') == 't e N k i s u g o k u i:'

def test_enlargesmallkana():
    assert jaconv.enlargesmallkana('キュゥべえ') == 'キユウべえ'
    assert jaconv.enlargesmallkana('しゃえい') == 'しやえい'
    assert jaconv.enlargesmallkana('しゅみ') == 'しゆみ'
    assert jaconv.enlargesmallkana('きょういっぱい') == 'きよういつぱい'
    assert jaconv.enlargesmallkana('霞ヶ関') == '霞ケ関'
    assert jaconv.enlargesmallkana('一ヵ月') == '一カ月'
    assert jaconv.enlargesmallkana('シャトー') == 'シヤトー'
    assert jaconv.enlargesmallkana('チューリップ') == 'チユーリツプ'
    assert jaconv.enlargesmallkana('ショート') == 'シヨート'
    assert jaconv.enlargesmallkana('きょういっぱい', 'っ') == 'きよういっぱい'
    assert jaconv.enlargesmallkana('きょういっぱい', 'ょっ') == 'きょういっぱい'
