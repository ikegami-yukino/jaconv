jaconvV2
==========
|travis| |coveralls| |pyversion| |version| |license|

jaconvV2 (Japanese Converter) は 全角キャラクタと半角キャラクタの検査を行い、及び平仮名・カタカナ・全角・半角の文字種変換を高速に行います。
Pythonのみで実装されているので、Cコンパイラが使えない環境でも利用できます。


INSTALLATION
==============

::

 $ pip install jaconvV2


USAGE
============

.. code:: python

  import jaconvV2

  # 全角キャラクタの検査
  jaconvV2.is_zen('Ｄ')
  # => True

  # 半角キャラクタの検査
  jaconvV2.is_han('D')
  # => True

  # ひらがな to カタカナ
  jaconvV2.hira2kata('ともえまみ')
  # => 'トモエマミ'

  # ひらがな to 半角カタカナ
  jaconvV2.hira2hkata('ともえまみ')
  # => 'ﾄﾓｴﾏﾐ'

  # カタカナ to ひらがな
  jaconvV2.kata2hira('巴マミ')
  # => '巴まみ'

  # 半角かな文字 to 全角かな文字
  jaconvV2.h2z('ﾃｨﾛ･ﾌｨﾅｰﾚ')
  # => 'ティロ・フィナーレ'

  # 半角ASCII to 全角ASCII
  jaconvV2.h2z('abc', kana=False, ascii=True, digit=False)
  # => 'ａｂｃ'

  # 数字以外の半角文字 to 全角文字
  jaconvV2.h2z('123', kana=False, ascii=False, digit=True)
  # => '１２３'

  # カタカナ以外の半角文字 to 全角文字
  jaconvV2.h2z('ｱabc123', kana=False, digit=True, ascii=True)
  # => 'ｱａｂｃ１２３'

  # h2zのエイリアス
  jaconvV2.hankaku2zenkaku('ﾃｨﾛ･ﾌｨﾅｰﾚabc123')
  # => 'ティロ・フィナーレabc123'

  # 全角かな文字 to 半角かな文字
  jaconvV2.z2h('ティロ・フィナーレ')
  # => 'ﾃｨﾛ・ﾌｨﾅｰﾚ'

  # 全角ASCII to 半角ASCII
  jaconvV2.z2h('ａｂｃ', kana=False, ascii=True, digit=False)
  # => 'abc'

  # 全角アラビア数字 to 半角アラビア数字
  jaconvV2.z2h('１２３', kana=False, ascii=False, digit=True)
  # => '123'

  # カタカナ以外の全角文字 to 半角文字
  jaconvV2.z2h('アａｂｃ１２３', kana=False, digit=True, ascii=True)
  # => 'アabc123'

  # z2hのエイリアス
  jaconvV2.zenkaku2hankaku('ティロ・フィナーレａｂｃ１２３')
  # => 'ﾃｨﾛ･ﾌｨﾅｰﾚａｂｃ１２３'

  # normalize
  jaconvV2.normalize('ティロ･フィナ〜レ', 'NFKC')
  # => 'ティロ・フィナーレ'

  # ひらがな to アルファベット
  jaconvV2.kana2alphabet('じゃぱん')
  # => japan

  # アルファベット to ひらがな
  jaconvV2.alphabet2kana('japan')
  # => じゃぱん

  # カタカナ to アルファベット
  jaconvV2.kata2alphabet('ケツイ')
  # => 'ketsui'

  # アルファベット to カタカナ
  jaconvV2.alphabet2kata('namba')
  # => 'ナンバ'

  # ひらがな to Juliusの音素表現
  jaconvV2.hiragana2julius('てんきすごくいいいいいい')
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


.. |travis| image:: https://travis-ci.org/MikimotoH/jaconv.svg?branch=master
    :target: https://travis-ci.org/MikimotoH/jaconv
    :alt: travis-ci.org

.. |coveralls| image:: https://coveralls.io/repos/github/MikimotoH/jaconv/badge.svg?branch=master
    :target: https://coveralls.io/github/MikimotoH/jaconv?branch=master
    :alt: coveralls.io

.. |pyversion| image:: https://img.shields.io/pypi/pyversions/jaconv.svg

.. |version| image:: https://img.shields.io/pypi/v/jaconv.svg
    :target: http://pypi.python.org/pypi/jaconvV2/
    :alt: latest version

.. |license| image:: https://img.shields.io/pypi/l/jaconv.svg
    :target: http://pypi.python.org/pypi/jaconvV2/
    :alt: license
