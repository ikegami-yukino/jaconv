jaconv
==========
|version| |pyversion| |license| |download| |usedby| |githubstars| |nowar| |nonuke|

jaconv (Japanese Converter) is interconverter for Hiragana, Katakana, Hankaku (half-width character) and Zenkaku (full-width character)

`Japanese README <https://github.com/ikegami-yukino/jaconv/blob/master/README_JP.rst>`_ is available.

INSTALLATION
==============

::

 $ pip install jaconv


USAGE
============

See also `document <http://ikegami-yukino.github.io/jaconv/jaconv.html>`_

.. code:: python

  import jaconv

  # Hiragana to Katakana
  jaconv.hira2kata('ともえまみ')
  # => 'トモエマミ'

  # Hiragana to half-width Katakana
  jaconv.hira2hkata('ともえまみ')
  # => 'ﾄﾓｴﾏﾐ'

  # Katakana to Hiragana
  jaconv.kata2hira('巴マミ')
  # => '巴まみ'

  # half-width character to full-width character
  # default parameters are followings: kana=True, ascii=False, digit=False
  jaconv.h2z('ﾃｨﾛ･ﾌｨﾅｰﾚ')
  # => 'ティロ・フィナーレ'

  # half-width character to full-width character
  # but only ascii characters
  jaconv.h2z('abc', kana=False, ascii=True, digit=False)
  # => 'ａｂｃ'

  # half-width character to full-width character
  # but only digit characters
  jaconv.h2z('123', kana=False, ascii=False, digit=True)
  # => '１２３'

  # half-width character to full-width character
  # except half-width Katakana
  jaconv.h2z('ｱabc123', kana=False, digit=True, ascii=True)
  # => 'ｱａｂｃ１２３'

  # an alias of h2z
  jaconv.hankaku2zenkaku('ﾃｨﾛ･ﾌｨﾅｰﾚabc123')
  # => 'ティロ・フィナーレabc123'

  # full-width character to half-width character
  # default parameters are followings: kana=True, ascii=False, digit=False
  jaconv.z2h('ティロ・フィナーレ')
  # => 'ﾃｨﾛ・ﾌｨﾅｰﾚ'

  # full-width character to half-width character
  # but only ascii characters
  jaconv.z2h('ａｂｃ', kana=False, ascii=True, digit=False)
  # => 'abc'

  # full-width character to half-width character
  # but only digit characters
  jaconv.z2h('１２３', kana=False, ascii=False, digit=True)
  # => '123'

  # full-width character to half-width character
  # except full-width Katakana
  jaconv.z2h('アａｂｃ１２３', kana=False, digit=True, ascii=True)
  # => 'アabc123'

  # an alias of z2h
  jaconv.zenkaku2hankaku('ティロ・フィナーレａｂｃ１２３')
  # => 'ﾃｨﾛ･ﾌｨﾅｰﾚａｂｃ１２３'

  # normalize
  jaconv.normalize('ティロ･フィナ〜レ', 'NFKC')
  # => 'ティロ・フィナーレ'

  # Hiragana to alphabet
  jaconv.kana2alphabet('じゃぱん')
  # => 'japan'

  # Alphabet to Hiragana
  jaconv.alphabet2kana('japan')
  # => 'じゃぱん'

  # Katakana to Alphabet
  jaconv.kata2alphabet('ケツイ')
  # => 'ketsui'

  # Alphabet to Katakana
  jaconv.alphabet2kata('namba')
  # => 'ナンバ'

  # Hiragana to Julius's phoneme format
  jaconv.hiragana2julius('てんきすごくいいいいいい')
  # => 't e N k i s u g o k u i:'


NOTE
============

jaconv.normalize method expand unicodedata.normalize for Japanese language processing.

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


.. |pyversion| image:: https://img.shields.io/pypi/pyversions/jaconv.svg

.. |version| image:: https://img.shields.io/pypi/v/jaconv.svg
    :target: http://pypi.python.org/pypi/jaconv/
    :alt: latest version

.. |license| image:: https://img.shields.io/pypi/l/jaconv.svg
    :target: http://pypi.python.org/pypi/jaconv/
    :alt: license

.. |download| image:: https://static.pepy.tech/personalized-badge/jaconv?period=total&units=international_system&left_color=black&right_color=blue&left_text=Downloads
    :target: https://pepy.tech/project/jaconv
    :alt: download

.. |usedby| image:: https://img.shields.io/github/search?query=import%20jaconv%20language%3Apython&label=Used%20in%20GitHub
    :target: https://github.com/search?q=import+jaconv+language%3Apython&type=code
    :alt: GitHub code search count

.. |githubstars| image:: https://img.shields.io/github/stars/ikegami-yukino/jaconv
    :target: https://github.com/ikegami-yukino/jaconv
    :alt: GitHub Repo stars

.. |nowar| image:: https://img.shields.io/badge/%F0%9F%A4%9D%20NO%20WAR-FF0000?style=plastic
    :alt: NO WAR budge

.. |nonuke| image:: https://img.shields.io/badge/%E2%98%A2%20NO%20NUKE-FFFF00?style=plastic
    :alt: NO NUKE budge
