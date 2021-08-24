# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from nose.tools import assert_equal, nottest
import jaconvV2
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
    assert_equal(jaconvV2.hira2kata('ともえまみ'), 'トモエマミ')
    assert_equal(jaconvV2.hira2kata('まどまぎ', ignore='ど'), 'マどマギ')
    _compare(jaconvV2.hira2kata, HIRAGANA, FULL_KANA)


def test_hira2hkata():
    assert_equal(jaconvV2.hira2hkata('ともえまみ'), 'ﾄﾓｴﾏﾐ')
    assert_equal(jaconvV2.hira2hkata('ともえまみ', ignore='み'), 'ﾄﾓｴﾏみ')
    _compare(jaconvV2.hira2hkata, HIRAGANA, HALF_KANA)


def test_kata2hira():
    assert_equal(jaconvV2.kata2hira('巴マミ'), '巴まみ')
    assert_equal(jaconvV2.kata2hira('マミサン', ignore='ン'), 'まみさン')
    _compare(jaconvV2.kata2hira, FULL_KANA, HIRAGANA)


def test_h2z():
    assert_equal(jaconvV2.h2z('ﾃｨﾛﾌｨﾅｰﾚ'), 'ティロフィナーレ')
    assert_equal(jaconvV2.h2z('ﾃｨﾛﾌｨﾅｰﾚ', ignore='ｨ'), 'テｨロフｨナーレ')
    _compare(jaconvV2.h2z, HALF_KANA, FULL_KANA)
    _compare(partial(jaconvV2.h2z, ascii=True), HALF_ASCII, FULL_ASCII)
    _compare(partial(jaconvV2.h2z, digit=True), HALF_DIGIT, FULL_DIGIT)

    for ascii in (True, False):
        for digit in (True, False):
            for kana in (True, False):
                assert_equal(
                    jaconvV2.h2z(_concat(HALF_KANA if kana else FULL_KANA,
                                         HALF_ASCII if ascii else FULL_ASCII,
                                         HALF_DIGIT if digit else FULL_DIGIT),
                                 ascii=ascii, digit=digit, kana=kana),
                    _concat(FULL_KANA, FULL_ASCII, FULL_DIGIT))


def test_z2h():
    assert_equal(jaconvV2.z2h('ティロフィナーレ'), 'ﾃｨﾛﾌｨﾅｰﾚ')
    assert_equal(jaconvV2.z2h('ティロフィナーレ', ignore='ィ'), 'ﾃィﾛﾌィﾅｰﾚ')
    _compare(partial(jaconvV2.z2h, kana=True), FULL_KANA, HALF_KANA)
    _compare(partial(jaconvV2.z2h, ascii=True), FULL_ASCII, HALF_ASCII)
    _compare(partial(jaconvV2.z2h, digit=True), FULL_DIGIT, HALF_DIGIT)

    for ascii in (True, False):
        for digit in (True, False):
            for kana in (True, False):
                assert_equal(
                    jaconvV2.z2h(_concat(FULL_KANA if kana else HALF_KANA,
                                         FULL_ASCII if ascii else HALF_ASCII,
                                         FULL_DIGIT if digit else HALF_DIGIT),
                                 ascii=ascii, digit=digit, kana=kana),
                    _concat(HALF_KANA, HALF_ASCII, HALF_DIGIT))


def test_normalize():
    assert_equal(jaconvV2.normalize('ﾃｨﾛ･フィナ〜レ', 'NFKC'), 'ティロ・フィナーレ')
    assert_equal(jaconvV2.normalize(_concat(HALF_KANA, FULL_DIGIT), 'NFKC'),
                 ''.join(FULL_KANA) + ''.join(HALF_DIGIT))


def test_kana2alphabet():
    assert_equal(jaconvV2.kana2alphabet('まみさん'), 'mamisan')
    assert_equal(jaconvV2.kana2alphabet('はっとり'), 'hattori')
    assert_equal(jaconvV2.kana2alphabet('はっ'), 'haxtsu')
    assert_equal(jaconvV2.kana2alphabet('ぽっ'), 'poxtsu')
    assert_equal(jaconvV2.kana2alphabet('ふぁふぃふぇふぉ'), 'fafifefo')
    assert_equal(jaconvV2.kana2alphabet('っって'), 'xtsutte')


def test_alphabet2kana():
    assert_equal(jaconvV2.alphabet2kana('mamisan'), 'まみさん')
    assert_equal(jaconvV2.alphabet2kana('doggu doguu'), 'どっぐ どぐう')
    assert_equal(jaconvV2.alphabet2kana('botchi'), 'ぼっち')
    assert_equal(jaconvV2.alphabet2kana('fainarufantaji-'), 'ふぁいなるふぁんたじー')
    assert_equal(jaconvV2.alphabet2kana('atsui'), 'あつい')
    assert_equal(jaconvV2.alphabet2kana('itoh'), 'いとう')
    assert_equal(jaconvV2.alphabet2kana('ohtaku'), 'おおたく')
    assert_equal(jaconvV2.alphabet2kana('namba'), 'なんば')


def test_alphabet2julius():
    assert_equal(jaconvV2.hiragana2julius('てんき'), 't e N k i')
    assert_equal(jaconvV2.hiragana2julius('やったー'), 'y a q t a:')
    assert_equal(jaconvV2.hiragana2julius('かわいいいいい'), 'k a w a i:')
    assert_equal(jaconvV2.hiragana2julius('やろうぜ'), 'y a r o: z e')
    assert_equal(jaconvV2.hiragana2julius('てんきすごくいいいいいい'), 't e N k i s u g o k u i:')


def test_is_han():
    assert_equal(jaconvV2.is_han('!'), True)
    assert_equal(jaconvV2.is_han('！'), False)
    assert_equal(jaconvV2.is_han('D'), True)
    assert_equal(jaconvV2.is_han('Ｄ'), False)
    assert_equal(jaconvV2.is_han('デ'), False)
    assert_equal(jaconvV2.is_han('で'), False)
    assert_equal(jaconvV2.is_han('ﾗ'), True)
    assert_equal(jaconvV2.is_han('★'), False)
    assert_equal(jaconvV2.is_han('ｯ'), True)
    assert_equal(jaconvV2.is_han('ッ'), False)
    assert_equal(jaconvV2.is_han('ﾞ'), True)
    assert_equal(jaconvV2.is_han('゛'), False)
    assert_equal(jaconvV2.is_han('ﾟ'), True)
    assert_equal(jaconvV2.is_han('゜'), False)
    assert_equal(all(jaconvV2.is_han(_) for _ in '!DELAdap'), True)
    assert_equal(all(jaconvV2.is_han(_) for _ in 'テイルズオブアライズ'), False)
    assert_equal(all(jaconvV2.is_han(_) for _ in 'ﾃｲﾙｽﾞｵﾌﾞｱﾗｲｽﾞ'), True)


def test_is_zen():
    assert_equal(jaconvV2.is_zen('!'), False)
    assert_equal(jaconvV2.is_zen('！'), True)
    assert_equal(jaconvV2.is_zen('D'), False)
    assert_equal(jaconvV2.is_zen('Ｄ'), True)
    assert_equal(jaconvV2.is_zen('デ'), True)
    assert_equal(jaconvV2.is_zen('で'), True)
    assert_equal(jaconvV2.is_zen('ﾗ'), False)
    assert_equal(jaconvV2.is_zen('★'), True)
    assert_equal(jaconvV2.is_zen('ｯ'), False)
    assert_equal(jaconvV2.is_zen('ッ'), True)
    assert_equal(jaconvV2.is_zen('ﾞ'), False)
    assert_equal(jaconvV2.is_zen('゛'), True)
    assert_equal(jaconvV2.is_zen('ﾟ'), False)
    assert_equal(jaconvV2.is_zen('゜'), True)
    assert_equal(all(jaconvV2.is_zen(_) for _ in '!DELAdap'), False)
    assert_equal(all(jaconvV2.is_zen(_) for _ in 'テイルズオブアライズ'), True)
    assert_equal(all(jaconvV2.is_zen(_) for _ in 'ﾃｲﾙｽﾞｵﾌﾞｱﾗｲｽﾞ'), False)
