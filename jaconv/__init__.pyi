from _typeshed import Incomplete

from . import jaconv

__all__ = [
    'hira2kata',
    'hira2hkata',
    'kata2hira',
    'h2z',
    'z2h',
    'hankaku2zenkaku',
    'zenkaku2hankaku',
    'han2zen',
    'zen2han',
    'normalize',
    'kana2alphabet',
    'alphabet2kana',
    'kata2alphabet',
    'alphabet2kata',
    'hiragana2julius',
    'enlargesmallkana',
    'enlarge_smallkana',
]

hira2kata = jaconv.hira2kata
hira2hkata = jaconv.hira2hkata
kata2hira = jaconv.kata2hira
h2z = jaconv.h2z
z2h = jaconv.z2h
han2zen = jaconv.han2zen
zen2han = jaconv.zen2han
hankaku2zenkaku = jaconv.hankaku2zenkaku
zenkaku2hankaku = jaconv.zenkaku2hankaku
normalize = jaconv.normalize
kana2alphabet = jaconv.kana2alphabet
alphabet2kana = jaconv.alphabet2kana
kata2alphabet = jaconv.kata2alphabet
alphabet2kata = jaconv.alphabet2kata
hiragana2julius = jaconv.hiragana2julius
enlargesmallkana = jaconv.enlargesmallkana
enlarge_smallkana = jaconv.enlarge_smallkana
