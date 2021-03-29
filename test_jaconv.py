# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from nose.tools import assert_equal, nottest
import jaconv
from functools import partial

assert_equal.__self__.maxDiff = None

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


@nottest
def _compare(mathod, lhs, rhs):
    for i in range(len(lhs)):
        assert_equal(mathod(lhs[i]), rhs[i])


@nottest
def _concat(*iterables):
    result = ''
    for iterable in iterables:
        result += ''.join(iterable)
    return result


def test_hira2kata():
    assert_equal(jaconv.hira2kata('ともえまみ'), 'トモエマミ')
    assert_equal(jaconv.hira2kata('まどまぎ', ignore='ど'), 'マどマギ')
    _compare(jaconv.hira2kata, HIRAGANA, FULL_KANA)


def test_hira2hkata():
    assert_equal(jaconv.hira2hkata('ともえまみ'), 'ﾄﾓｴﾏﾐ')
    assert_equal(jaconv.hira2hkata('ともえまみ', ignore='み'), 'ﾄﾓｴﾏみ')
    _compare(jaconv.hira2hkata, HIRAGANA, HALF_KANA)


def test_kata2hira():
    assert_equal(jaconv.kata2hira('巴マミ'), '巴まみ')
    assert_equal(jaconv.kata2hira('マミサン', ignore='ン'), 'まみさン')
    _compare(jaconv.kata2hira, FULL_KANA, HIRAGANA)


def test_h2z():
    assert_equal(jaconv.h2z('ﾃｨﾛﾌｨﾅｰﾚ'), 'ティロフィナーレ')
    assert_equal(jaconv.h2z('ﾃｨﾛﾌｨﾅｰﾚ', ignore='ｨ'), 'テｨロフｨナーレ')
    _compare(jaconv.h2z, HALF_KANA, FULL_KANA)
    _compare(partial(jaconv.h2z, ascii=True), HALF_ASCII, FULL_ASCII)
    _compare(partial(jaconv.h2z, digit=True), HALF_DIGIT, FULL_DIGIT)

    for ascii in (True, False):
        for digit in (True, False):
            for kana in (True, False):
                assert_equal(
                    jaconv.h2z(_concat(HALF_KANA if kana else FULL_KANA,
                                        HALF_ASCII if ascii else FULL_ASCII,
                                        HALF_DIGIT if digit else FULL_DIGIT),
                                ascii=ascii, digit=digit, kana=kana),
                    _concat(FULL_KANA, FULL_ASCII, FULL_DIGIT))


def test_z2h():
    assert_equal(jaconv.z2h('ティロフィナーレ'), 'ﾃｨﾛﾌｨﾅｰﾚ')
    assert_equal(jaconv.z2h('ティロフィナーレ', ignore='ィ'), 'ﾃィﾛﾌィﾅｰﾚ')
    _compare(partial(jaconv.z2h, kana=True), FULL_KANA, HALF_KANA)
    _compare(partial(jaconv.z2h, ascii=True), FULL_ASCII, HALF_ASCII)
    _compare(partial(jaconv.z2h, digit=True), FULL_DIGIT, HALF_DIGIT)

    for ascii in (True, False):
        for digit in (True, False):
            for kana in (True, False):
                assert_equal(
                    jaconv.z2h(_concat(FULL_KANA if kana else HALF_KANA,
                                        FULL_ASCII if ascii else HALF_ASCII,
                                        FULL_DIGIT if digit else HALF_DIGIT),
                                ascii=ascii, digit=digit, kana=kana),
                    _concat(HALF_KANA, HALF_ASCII, HALF_DIGIT))


def test_normalize():
    assert_equal(jaconv.normalize('ﾃｨﾛ･フィナ〜レ', 'NFKC'), 'ティロ・フィナーレ')
    assert_equal(jaconv.normalize(_concat(HALF_KANA, FULL_DIGIT), 'NFKC'),
                 ''.join(FULL_KANA)+''.join(HALF_DIGIT))


def test_kana2alphabet():
    assert_equal(jaconv.kana2alphabet('まみさん'), 'mamisan')
    assert_equal(jaconv.kana2alphabet('はっとり'), 'hattori')
    assert_equal(jaconv.kana2alphabet('はっ'), 'haxtsu')
    assert_equal(jaconv.kana2alphabet('ぽっ'), 'poxtsu')
    assert_equal(jaconv.kana2alphabet('ふぁふぃふぇふぉ'), 'fafifefo')
    assert_equal(jaconv.kana2alphabet('っって'), 'xtsutte')


def test_alphabet2kana():
    assert_equal(jaconv.alphabet2kana('mamisan'), 'まみさん')
    assert_equal(jaconv.alphabet2kana('doggu doguu'), 'どっぐ どぐう')
    assert_equal(jaconv.alphabet2kana('botchi'), 'ぼっち')
    assert_equal(jaconv.alphabet2kana('fainarufantaji-'), 'ふぁいなるふぁんたじー')
    assert_equal(jaconv.alphabet2kana('atsui'), 'あつい')
    assert_equal(jaconv.alphabet2kana('itoh'), 'いとう')
    assert_equal(jaconv.alphabet2kana('ohtaku'), 'おおたく')
    assert_equal(jaconv.alphabet2kana('namba'), 'なんば')
