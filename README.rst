jctconv
==========
|travis| |coveralls| |downloads| |Python2.7| |Python3.5| |version| |license|


jctconv (Japanese Character Type Converter) はひらがな・カタカナ・全角・半角の文字種変換を高速に行います。
Pythonのみで実装されているので、Cコンパイラが使えない環境でも利用できます。

normalizeメソッドは、unicodedata.normalize を日本語処理向けに特化した拡張を行っています。
具体的には以下のように変換します。

.. code:: python

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

.. code:: python

  import jctconv
  jctconv.hira2kata(u'ともえまみ')
  # => u'トモエマミ'
  jctconv.hira2hkata(u'ともえまみ')
  # => u'ﾄﾓｴﾏﾐ'
  jctconv.kata2hira(u'巴マミ')
  # => u'巴まみ'
  jctconv.h2z(u'ﾃｨﾛ･ﾌｨﾅｰﾚ')
  # => u'ティロ･フィナーレ'
  jctconv.h2z(u'abc', ascii=True)
  # => u'ａｂｃ'
  jctconv.h2z(u'123', digit=True)
  # => u'１２３'
  jctconv.h2z(u'ｱabc123', kana=False, digit=True, ascii=True)
  # => u'ｱａｂｃ１２３'
  jctconv.z2h(u'ティロ・フィナーレ')
  # => u'ﾃｨﾛ・ﾌｨﾅｰﾚ'
  jctconv.z2h(u'ａｂｃ', ascii=True)
  # => u'abc'
  jctconv.z2h(u'１２３', digit=True)
  # => u'123'
  jctconv.z2h(u'アａｂｃ１２３', kana=False, digit=True, ascii=True)
  # => u'アabc123'
  jctconv.normalize(u'ティロ･フィナ〜レ', 'NFKC')
  # => u'ティロ・フィナーレ'


.. |travis| image:: https://travis-ci.org/ikegami-yukino/jctconv.svg?branch=master
    :target: https://travis-ci.org/ikegami-yukino/jctconv
    :alt: travis-ci.org

.. |coveralls| image:: https://coveralls.io/repos/ikegami-yukino/jctconv/badge.svg?branch=master&service=github
    :target: https://coveralls.io/github/ikegami-yukino/jctconv?branch=master
    :alt: coveralls.io

.. |downloads| image:: https://img.shields.io/pypi/dm/jctconv.svg
    :target: http://pypi.python.org/pypi/jctconv/
    :alt: downloads

.. |Python2.7| image:: https://img.shields.io/badge/python-2.7-blue.svg

.. |Python3.5| image:: https://img.shields.io/badge/python-3.5-blue.svg

.. |version| image:: https://img.shields.io/pypi/v/jctconv.svg
    :target: http://pypi.python.org/pypi/jctconv/
    :alt: latest version

.. |license| image:: https://img.shields.io/pypi/l/jctconv.svg
    :target: http://pypi.python.org/pypi/jctconv/
    :alt: license
