jaconv
==========
|travis| |coveralls| |pyversion| |version| |license| |download|

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
  jaconv.hira2kata('ともえまみ')
  # => 'トモエマミ'

  # ひらがな to 半角カタカナ
  jaconv.hira2hkata('ともえまみ')
  # => 'ﾄﾓｴﾏﾐ'

  # カタカナ to ひらがな
  jaconv.kata2hira('巴マミ')
  # => '巴まみ'

  # 半角かな文字 to 全角かな文字
  jaconv.h2z('ﾃｨﾛ･ﾌｨﾅｰﾚ')
  # => 'ティロ・フィナーレ'

  # 半角ASCII to 全角ASCII
  jaconv.h2z('abc', kana=False, ascii=True, digit=False)
  # => 'ａｂｃ'

  # 数字以外の半角文字 to 全角文字
  jaconv.h2z('123', kana=False, ascii=False, digit=True)
  # => '１２３'

  # カタカナ以外の半角文字 to 全角文字
  jaconv.h2z('ｱabc123', kana=False, digit=True, ascii=True)
  # => 'ｱａｂｃ１２３'

  # h2zのエイリアス
  jaconv.hankaku2zenkaku('ﾃｨﾛ･ﾌｨﾅｰﾚabc123')
  # => 'ティロ・フィナーレabc123'

  # 全角かな文字 to 半角かな文字
  jaconv.z2h('ティロ・フィナーレ')
  # => 'ﾃｨﾛ・ﾌｨﾅｰﾚ'

  # 全角ASCII to 半角ASCII
  jaconv.z2h('ａｂｃ', kana=False, ascii=True, digit=False)
  # => 'abc'

  # 全角アラビア数字 to 半角アラビア数字
  jaconv.z2h('１２３', kana=False, ascii=False, digit=True)
  # => '123'

  # カタカナ以外の全角文字 to 半角文字
  jaconv.z2h('アａｂｃ１２３', kana=False, digit=True, ascii=True)
  # => 'アabc123'

  # z2hのエイリアス
  jaconv.zenkaku2hankaku('ティロ・フィナーレａｂｃ１２３')
  # => 'ﾃｨﾛ･ﾌｨﾅｰﾚａｂｃ１２３'

  # normalize
  jaconv.normalize('ティロ･フィナ〜レ', 'NFKC')
  # => 'ティロ・フィナーレ'

  # ひらがな to アルファベット
  jaconv.kana2alphabet('じゃぱん')
  # => japan

  # アルファベット to ひらがな
  jaconv.alphabet2kana('japan')
  # => じゃぱん

  # カタカナ to アルファベット
  jaconv.kata2alphabet('ケツイ')
  # => 'ketsui'

  # アルファベット to カタカナ
  jaconv.alphabet2kata('namba')
  # => 'ナンバ'

  # ひらがな to Juliusの音素表現
  jaconv.hiragana2julius('てんきすごくいいいいいい')
  # => 't e N k i s u g o k u i:'


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

.. |download| image:: https://static.pepy.tech/personalized-badge/neologdn?period=total&units=international_system&left_color=black&right_color=blue&left_text=Downloads
    :target: https://pepy.tech/project/neologdn
    :alt: download
