jaconv
==========
|travis| |coveralls| |pyversion| |version| |license|

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
  jaconv.hira2kata(u'ともえまみ')
  # => u'トモエマミ'

  # Hiragana to half-width Katakana
  jaconv.hira2hkata(u'ともえまみ')
  # => u'ﾄﾓｴﾏﾐ'

  # Katakana to Hiragana
  jaconv.kata2hira(u'巴マミ')
  # => u'巴まみ'

  # half-width character to full-width character
  jaconv.h2z(u'ﾃｨﾛ･ﾌｨﾅｰﾚ')
  # => u'ティロ･フィナーレ'

  # half-width character to full-width character
  # but only ascii characters
  jaconv.h2z(u'abc', ascii=True)
  # => u'ａｂｃ'

  # half-width character to full-width character
  # but only digit characters
  jaconv.h2z(u'123', digit=True)
  # => u'１２３'

  # half-width character to full-width character
  # except half-width Katakana
  jaconv.h2z(u'ｱabc123', kana=False, digit=True, ascii=True)
  # => u'ｱａｂｃ１２３'

  # full-width character to half-width character
  jaconv.z2h(u'ティロ・フィナーレ')
  # => u'ﾃｨﾛ・ﾌｨﾅｰﾚ'

  # full-width character to half-width character
  # but only ascii characters
  jaconv.z2h(u'ａｂｃ', ascii=True)
  # => u'abc'

  # full-width character to half-width character
  # but only digit characters
  jaconv.z2h(u'１２３', digit=True)
  # => u'123'

  # full-width character to half-width character
  # except full-width Katakana
  jaconv.z2h(u'アａｂｃ１２３', kana=False, digit=True, ascii=True)
  # => u'アabc123'

  # normalize
  jaconv.normalize(u'ティロ･フィナ〜レ', 'NFKC')
  # => u'ティロ・フィナーレ'

  # Hiragana to alphabet
  jaconv.kana2alphabet(u'じゃぱん')
  # => japan

  # Alphabet to Hiragana
  jaconv.alphabet2kana(u'japan')
  # => じゃぱん


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
