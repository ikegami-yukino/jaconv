# -*- coding: utf-8 -*-
from codecs import open
import os
import re
from setuptools import setup

with open(os.path.join('jaconv', '__init__.py'), 'r', encoding='utf8') as f:
    version = re.compile(r".*__version__ = '(.*?)'",
                         re.S).match(f.read()).group(1)

setup(name='jaconv',
      packages=['jaconv'],
      version=version,
      license='MIT License',
      platforms=['POSIX', 'Windows', 'Unix', 'MacOS'],
      description='Pure-Python Japanese character interconverter for '
      'Hiragana, Katakana, Hankaku, Zenkaku and more',
      author='Yukino Ikegami',
      author_email='yknikgm@gmail.com',
      url='https://github.com/ikegami-yukino/jaconv',
      keywords=[
          'Japanese converter', 'Japanese', 'text preprocessing',
          'half-width kana', 'Hiragana', 'Katakana', 'Hankaku', 'Zenkaku',
          'transliteration', 'Julius'
      ],
      classifiers=[
          'Development Status :: 4 - Beta', 'Intended Audience :: Developers',
          'Intended Audience :: Information Technology',
          'License :: OSI Approved :: MIT License',
          'Natural Language :: Japanese', 'Operating System :: MacOS',
          'Operating System :: Microsoft', 'Operating System :: POSIX',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Programming Language :: Python :: 3.9',
          'Programming Language :: Python :: 3.10',
          'Programming Language :: Python :: 3.11', 'Topic :: Text Processing'
      ],
      data_files=[('', ['README.rst', 'CHANGES.rst'])],
      long_description='%s\n\n%s' %
      (open('README.rst', encoding='utf8').read(),
       open('CHANGES.rst', encoding='utf8').read()),
      test_suite='nose.collector')
