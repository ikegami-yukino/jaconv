# -*- coding: utf-8 -*-
from nose.tools import assert_equal
import jctconv

assert_equal.__self__.maxDiff = None

HIRAGANA = u'ぁあぃいぅうぇえぉおかがきぎくぐけげこごさざしじすずせぜそぞただちぢっつづてでとどなにぬねのはばぱひびぴふぶぷへべぺほぼぽまみむめもゃやゅゆょよらりるれろわをんーゎゐゑゕゖゔ'
HALF_ASCII = u'!"#$%&\'()*+,-./:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~ '
HALF_DIGIT = u'0123456789'
HALF_KANA_SEION = u'ｧｱｨｲｩｳｪｴｫｵｶｷｸｹｺｻｼｽｾｿﾀﾁｯﾂﾃﾄﾅﾆﾇﾈﾉﾊﾋﾌﾍﾎﾏﾐﾑﾒﾓｬﾔｭﾕｮﾖﾗﾘﾙﾚﾛﾜｦﾝｰヮヰヱヵヶ'
HALF_KANA = u'ｧｱｨｲｩｳｪｴｫｵｶｶﾞｷｷﾞｸｸﾞｹｹﾞｺｺﾞｻｻﾞｼｼﾞｽｽﾞｾｾﾞｿｿﾞﾀﾀﾞﾁﾁﾞｯﾂﾂﾞﾃﾃﾞﾄﾄﾞﾅﾆﾇﾈﾉﾊﾊﾞﾊﾟﾋﾋﾞﾋﾟﾌﾌﾞﾌﾟﾍﾍﾞﾍﾟﾎﾎﾞﾎﾟﾏﾐﾑﾒﾓｬﾔｭﾕｮﾖﾗﾘﾙﾚﾛﾜｦﾝｰヮヰヱヵヶｳﾞ'
FULL_ASCII = u'！＂＃＄％＆＇（）＊＋，－．／：；＜＝＞？＠ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ［＼］＾＿｀ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ｛｜｝～　'
FULL_DIGIT = u'０１２３４５６７８９'
FULL_KANA = u'ァアィイゥウェエォオカガキギクグケゲコゴサザシジスズセゼソゾタダチヂッツヅテデトドナニヌネノハバパヒビピフブプヘベペホボポマミムメモャヤュユョヨラリルレロワヲンーヮヰヱヵヶヴ'
FULL_KANA_SEION = u'ァアィイゥウェエォオカキクケコサシスセソタチッツテトナニヌネノハヒフヘホマミムメモャヤュユョヨラリルレロワヲンーヮヰヱヵヶ'


def test_hira2kata():
    assert_equal(jctconv.hira2kata(u'ともえまみ'), u'トモエマミ')
    assert_equal(jctconv.hira2kata(HIRAGANA), FULL_KANA)


def test_hira2hkata():
    assert_equal(jctconv.hira2hkata(u'ともえまみ'), u'ﾄﾓｴﾏﾐ')
    assert_equal(jctconv.hira2hkata(HIRAGANA), HALF_KANA)


def test_kata2hira():
    assert_equal(jctconv.kata2hira(u'巴マミ'), u'巴まみ')
    assert_equal(jctconv.kata2hira(FULL_KANA), HIRAGANA)


def test_h2z():
    assert_equal(jctconv.h2z(u'ﾃｨﾛﾌｨﾅｰﾚ'), u'ティロフィナーレ')
    assert_equal(jctconv.h2z(HALF_KANA), FULL_KANA)
    assert_equal(jctconv.h2z(HALF_ASCII, ascii=True), FULL_ASCII)
    assert_equal(jctconv.h2z(HALF_DIGIT, digit=True), FULL_DIGIT)


def test_z2h():
    assert_equal(jctconv.z2h(u'ティロフィナーレ'), u'ﾃｨﾛﾌｨﾅｰﾚ')
    assert_equal(jctconv.z2h(FULL_KANA), HALF_KANA)
    assert_equal(jctconv.z2h(FULL_ASCII, ascii=True), HALF_ASCII)
    assert_equal(jctconv.z2h(FULL_DIGIT, digit=True), HALF_DIGIT)


def test_normalize():
    assert_equal(jctconv.normalize(u'ﾃｨﾛ･フィナ〜レ', 'NFKC'), u'ティロ・フィナーレ')
    assert_equal(jctconv.normalize(HALF_KANA+FULL_DIGIT, 'NFKC'), FULL_KANA+HALF_DIGIT)
