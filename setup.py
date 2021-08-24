# -*- coding: utf-8 -*-
from codecs import open
import os
import re
from setuptools import setup

with open(os.path.join('jaconvV2', '__init__.py'), 'r', encoding='utf8') as f:
    version = re.compile(
        r".*__version__ = '(.*?)'", re.S).match(f.read()).group(1)

setup(
    name='jaconvV2',
    packages=['jaconvV2'],
    version=version,
    license='MIT License',
    platforms=['POSIX', 'Windows', 'Unix', 'MacOS'],
    description='Pure-Python Japanese character interconverter for '
                'Hiragana, Katakana, Hankaku, Zenkaku, as well as Zenkaku or Hankaku Tester',
    author='Miki Liu',
    author_email='MikimotoH@gmail.com',
    url='https://github.com/MikimotoH/jaconv',
    keywords=['Japanese converter', 'Japanese', 'text preprocessing',
              'half-width kana', 'Hiragana', 'Katakana',
              'Hankaku', 'Zenkaku', 'transliteration', 'Julius'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: Japanese',
        'Operating System :: MacOS',
        'Operating System :: Microsoft',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Text Processing'
        ],
    data_files=[('', ['README.rst', 'CHANGES.rst'])],
    long_description='%s\n\n%s' % (open('README.rst', encoding='utf8').read(),
                                   open('CHANGES.rst', encoding='utf8').read()),
    test_suite = 'nose.collector'
)
