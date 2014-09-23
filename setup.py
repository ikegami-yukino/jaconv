# -*- coding: utf-8 -*-
from distutils.core import setup


setup(
    name='jctconv',
    py_modules=['jctconv'],
    version='0.0.7.3',
    license='MIT License',
    platforms=['POSIX', 'Windows', 'Unix', 'MacOS'],
    description='Pure-Python Japanese character interconverter for '
                'Hiragana, Katakana, Hankaku and Zenkaku',
    author='Yukino Ikegami',
    author_email='yukino0131@me.com',
    url='https://github.com/ikegami-yukino/jctconv',
    keywords=['japanese converter', 'half-width kana', 'Hiragana', 'Katakana',
              'Hankaku', 'Zenkaku'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: Japanese',
        'Operating System :: MacOS',
        'Operating System :: Microsoft',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Text Processing'
        ],
    data_files=[('', ['README.rst', 'CHANGES.rst'])],
    long_description='%s\n\n%s' % (open('README.rst').read(),
                                   open('CHANGES.rst').read())
)
