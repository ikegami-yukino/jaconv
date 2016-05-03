jaconv
==========
|travis| |coveralls| |downloads| |pyversion| |version| |license|

jaconv (Japanese Converter) はひらがな・カタカナ・全角・半角の文字種変換を高速に行います。
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

 $ pip install jaconv


USAGE
============

.. code:: python

  import jaconv
  jaconv.hira2kata(u'ともえまみ')
  # => u'トモエマミ'
  jaconv.hira2hkata(u'ともえまみ')
  # => u'ﾄﾓｴﾏﾐ'
  jaconv.kata2hira(u'巴マミ')
  # => u'巴まみ'
  jaconv.h2z(u'ﾃｨﾛ･ﾌｨﾅｰﾚ')
  # => u'ティロ･フィナーレ'
  jaconv.h2z(u'abc', ascii=True)
  # => u'ａｂｃ'
  jaconv.h2z(u'123', digit=True)
  # => u'１２３'
  jaconv.h2z(u'ｱabc123', kana=False, digit=True, ascii=True)
  # => u'ｱａｂｃ１２３'
  jaconv.z2h(u'ティロ・フィナーレ')
  # => u'ﾃｨﾛ・ﾌｨﾅｰﾚ'
  jaconv.z2h(u'ａｂｃ', ascii=True)
  # => u'abc'
  jaconv.z2h(u'１２３', digit=True)
  # => u'123'
  jaconv.z2h(u'アａｂｃ１２３', kana=False, digit=True, ascii=True)
  # => u'アabc123'
  jaconv.normalize(u'ティロ･フィナ〜レ', 'NFKC')
  # => u'ティロ・フィナーレ'


.. |travis| image:: https://travis-ci.org/ikegami-yukino/jaconv.svg?branch=master
    :target: https://travis-ci.org/ikegami-yukino/jaconv
    :alt: travis-ci.org

.. |coveralls| image:: https://coveralls.io/repos/ikegami-yukino/jaconv/badge.svg?branch=master&service=github
    :target: https://coveralls.io/github/ikegami-yukino/jaconv?branch=master
    :alt: coveralls.io

.. |downloads| image:: https://img.shields.io/pypi/dm/jaconv.svg
    :target: http://pypi.python.org/pypi/jaconv/
    :alt: downloads

.. |pyversion| image:: https://img.shields.io/pypi/pyversions/jaconv.svg

.. |version| image:: https://img.shields.io/pypi/v/jaconv.svg
    :target: http://pypi.python.org/pypi/jaconv/
    :alt: latest version

.. |license| image:: https://img.shields.io/pypi/l/jaconv.svg
    :target: http://pypi.python.org/pypi/jaconv/
    :alt: license
