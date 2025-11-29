# -*- coding: utf-8 -*-
from setuptools import setup

from jaconv.compat import open

setup(
      description='Pure-Python Japanese character interconverter for '
      'Hiragana, Katakana, Hankaku, Zenkaku and more',
      long_description='%s\n\n%s' %
      (open('README.rst', encoding='utf8').read(),
       open('CHANGES.rst', encoding='utf8').read()),
)
