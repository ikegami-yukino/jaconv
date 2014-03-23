jctconv
==========
.. image:: https://badge.fury.io/py/jctconv.png
    :target: http://badge.fury.io/py/jctconv

.. image:: https://travis-ci.org/ikegami-yukino/jctconv.png?branch=master
    :target: https://travis-ci.org/ikegami-yukino/jctconv

jctconv (Japanese Character Type Converter) はひらがな・カタカナ・全角・半角の文字種変換を高速に行います。
Pythonのみで実装されているので、Cコンパイラが使えない環境でも使えます。

normalizeメソッドは、unicodedata.normalizeを日本語処理向けに特化した拡張を行っています。
具体的には以下のように変換します。

::

  u'〜' -> u'ー',
  u'～' -> u'ー',
  u"’" -> "'",
  u'”' -> '"',
  u'―' -> '-',
  u'‐' -> '-'

INSTALLATION
==============

::

 $ pip install jctconv


USAGE
============

>>> import jctconv
>>> jctconv.hira2kata(u'ともえまみ')
トモエマミ
>>> jctconv.hira2hkata(u'ともえまみ')
ﾄﾓｴﾏﾐ
>>> jctconv.kata2hira(u'巴マミ')
巴まみ
>>> jctconv.h2z(u'ﾃｨﾛ･ﾌｨﾅｰﾚ')
ティロ･フィナーレ
>>> jctconv.h2z(u'abc', ascii=True)
ａｂｃ
>>> jctconv.h2z(u'123', digit=True)
１２３
>>> jctconv.h2z(u'ｱabc123', kana=False, digit=True, ascii=True)
ｱａｂｃ１２３
>>> jctconv.z2h(u'ティロ・フィナーレ')
ﾃｨﾛ・ﾌｨﾅｰﾚ
>>> jctconv.z2h(u'ａｂｃ', ascii=True)
abc
>>> jctconv.z2h(u'１２３', digit=True)
123
>>> jctconv.z2h(u'アａｂｃ１２３', kana=False, digit=True, ascii=True)
アabc123
>>> jctconv.normalize(u'ティロ･フィナ〜レ','NFKC')
ティロ・フィナーレ
