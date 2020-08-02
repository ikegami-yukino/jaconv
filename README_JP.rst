jaconv
==========
|travis| |coveralls| |pyversion| |version| |license|

jaconv (Japanese Converter) はひらがな・カタカナ・全角・半角の文字種変換を高速に行います。
Pythonのみで実装されているので、Cコンパイラが使えない環境でも利用できます。


INSTALLATION
==============

::

 $ pip install jaconv


USAGE
============

.. code:: python

  import jaconv

  # ひらがな to カタカナ
  jaconv.hira2kata(u'ともえまみ')
  # => u'トモエマミ'

  # ひらがな to 半角カタカナ
  jaconv.hira2hkata(u'ともえまみ')
  # => u'ﾄﾓｴﾏﾐ'

  # カタカナ to ひらがな
  jaconv.kata2hira(u'巴マミ')
  # => u'巴まみ'

  # 半角かな文字 to 全角かな文字
  jaconv.h2z(u'ﾃｨﾛ･ﾌｨﾅｰﾚ')
  # => u'ティロ･フィナーレ'

  # 半角ASCII to 全角ASCII
  jaconv.h2z(u'abc', kana=False, ascii=True, digit=False)
  # => u'ａｂｃ'

  # 数字以外の半角文字 to 全角文字
  jaconv.h2z(u'123', kana=False, ascii=False, digit=True)
  # => u'１２３'

  # カタカナ以外の半角文字 to 全角文字
  jaconv.h2z(u'ｱabc123', kana=False, digit=True, ascii=True)
  # => u'ｱａｂｃ１２３'

  # 全角かな文字 to 半角かな文字
  jaconv.z2h(u'ティロ・フィナーレ')
  # => u'ﾃｨﾛ・ﾌｨﾅｰﾚ'

  # 全角ASCII to 半角ASCII
  jaconv.z2h(u'ａｂｃ', kana=False, ascii=True, digit=False)
  # => u'abc'

  # 全角アラビア数字 to 半角アラビア数字
  jaconv.z2h(u'１２３', kana=False, ascii=False, digit=True)
  # => u'123'

  # カタカナ以外の全角文字 to 半角文字
  jaconv.z2h(u'アａｂｃ１２３', kana=False, digit=True, ascii=True)
  # => u'アabc123'

  # normalize
  jaconv.normalize(u'ティロ･フィナ〜レ', 'NFKC')
  # => u'ティロ・フィナーレ'

  # ひらがな to アルファベット
  jaconv.kana2alphabet(u'じゃぱん')
  # => japan

  # アルファベット to ひらがな
  jaconv.alphabet2kana(u'japan')
  # => じゃぱん


NOTE
============

normalizeメソッドは、unicodedata.normalize を日本語処理向けに特化した拡張を行っています。
具体的には以下のように変換します。

.. code::

    '〜' => 'ー'
    '～' => 'ー'
    "’" => "'"
    '”'=> '"'
    '“' => '``'
    '―' => '-'
    '‐' => '-'
    '˗' => '-'
    '֊' => '-'
    '‐' => '-'
    '‑' => '-'
    '‒' => '-'
    '–' => '-'
    '⁃' => '-'
    '⁻' => '-'
    '₋' => '-'
    '−' => '-'
    '﹣' => 'ー'
    '－' => 'ー'
    '—' => 'ー'
    '―' => 'ー'
    '━' => 'ー'
    '─' => 'ー'


.. |travis| image:: https://travis-ci.org/ikegami-yukino/jaconv.svg?branch=master
    :target: https://travis-ci.org/ikegami-yukino/jaconv
    :alt: travis-ci.org

.. |coveralls| image:: https://coveralls.io/repos/ikegami-yukino/jaconv/badge.svg?branch=master&service=github
    :target: https://coveralls.io/github/ikegami-yukino/jaconv?branch=master
    :alt: coveralls.io

.. |pyversion| image:: https://img.shields.io/pypi/pyversions/jaconv.svg

.. |version| image:: https://img.shields.io/pypi/v/jaconv.svg
    :target: http://pypi.python.org/pypi/jaconv/
    :alt: latest version

.. |license| image:: https://img.shields.io/pypi/l/jaconv.svg
    :target: http://pypi.python.org/pypi/jaconv/
    :alt: license
