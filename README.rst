jaconvV2
==========
|travis| |coveralls| |pyversion| |version| |license|

jaconvV2 (Japanese Converter) can detect whether a character is Zenkaku or Hankaku, and also support interconvertion for Hiragana, Katakana, Hankaku (half-width character) and Zenkaku (full-width character)

`Japanese README <https://github.com/MikimotoH/jaconv/blob/master/README_JP.rst>`_ is available.

INSTALLATION
==============

::

 $ pip install jaconvV2


USAGE
============

See also `document <http://ikegami-yukino.github.io/jaconv/jaconv.html>`_

.. code:: python

  import jaconvV2


  # Test if Zenkaku
  jaconvV2.is_zen('Ｄ')
  # => True

  # Test if Hankaku
  jaconvV2.is_han('D')
  # => True


  # Hiragana to Katakana
  jaconvV2.hira2kata('ともえまみ')
  # => 'トモエマミ'

  # Hiragana to half-width Katakana
  jaconvV2.hira2hkata('ともえまみ')
  # => 'ﾄﾓｴﾏﾐ'

  # Katakana to Hiragana
  jaconvV2.kata2hira('巴マミ')
  # => '巴まみ'

  # half-width character to full-width character
  # default parameters are followings: kana=True, ascii=False, digit=False
  jaconvV2.h2z('ﾃｨﾛ･ﾌｨﾅｰﾚ')
  # => 'ティロ・フィナーレ'

  # half-width character to full-width character
  # but only ascii characters
  jaconvV2.h2z('abc', kana=False, ascii=True, digit=False)
  # => 'ａｂｃ'

  # half-width character to full-width character
  # but only digit characters
  jaconvV2.h2z('123', kana=False, ascii=False, digit=True)
  # => '１２３'

  # half-width character to full-width character
  # except half-width Katakana
  jaconvV2.h2z('ｱabc123', kana=False, digit=True, ascii=True)
  # => 'ｱａｂｃ１２３'

  # an alias of h2z
  jaconvV2.hankaku2zenkaku('ﾃｨﾛ･ﾌｨﾅｰﾚabc123')
  # => 'ティロ・フィナーレabc123'

  # full-width character to half-width character
  # default parameters are followings: kana=True, ascii=False, digit=False
  jaconvV2.z2h('ティロ・フィナーレ')
  # => 'ﾃｨﾛ・ﾌｨﾅｰﾚ'

  # full-width character to half-width character
  # but only ascii characters
  jaconvV2.z2h('ａｂｃ', kana=False, ascii=True, digit=False)
  # => 'abc'

  # full-width character to half-width character
  # but only digit characters
  jaconvV2.z2h('１２３', kana=False, ascii=False, digit=True)
  # => '123'

  # full-width character to half-width character
  # except full-width Katakana
  jaconvV2.z2h('アａｂｃ１２３', kana=False, digit=True, ascii=True)
  # => 'アabc123'

  # an alias of z2h
  jaconvV2.zenkaku2hankaku('ティロ・フィナーレａｂｃ１２３')
  # => 'ﾃｨﾛ･ﾌｨﾅｰﾚａｂｃ１２３'

  # normalize
  jaconvV2.normalize('ティロ･フィナ〜レ', 'NFKC')
  # => 'ティロ・フィナーレ'

  # Hiragana to alphabet
  jaconvV2.kana2alphabet('じゃぱん')
  # => 'japan'

  # Alphabet to Hiragana
  jaconvV2.alphabet2kana('japan')
  # => 'じゃぱん'

  # Katakana to Alphabet
  jaconvV2.kata2alphabet('ケツイ')
  # => 'ketsui'

  # Alphabet to Katakana
  jaconvV2.alphabet2kata('namba')
  # => 'ナンバ'

  # Hiragana to Julius's phoneme format
  jaconvV2.hiragana2julius('てんきすごくいいいいいい')
  # => 't e N k i s u g o k u i:'

NOTE
============

jaconvV2.normalize method expand unicodedata.normalize for Japanese language processing.

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

.. |coveralls| image:: https://coveralls.io/repos/MikimotoH/jaconv/badge.svg?branch=master&service=github
    :target: https://coveralls.io/github/ikegami-yukino/jaconv?branch=master
    :alt: coveralls.io

.. |pyversion| image:: https://img.shields.io/pypi/pyversions/jaconv.svg

.. |version| image:: https://img.shields.io/pypi/v/jaconv.svg
    :target: http://pypi.python.org/pypi/jaconv/
    :alt: latest version

.. |license| image:: https://img.shields.io/pypi/l/jaconv.svg
    :target: http://pypi.python.org/pypi/jaconv/
    :alt: license
