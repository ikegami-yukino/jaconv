# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unicodedata


def normalize(text, mode='NFKC'):
    """Convert Half-width (Hankaku) Katakana to Full-width (Zenkaku) Katakana,
    Full-width (Zenkaku) ASCII and DIGIT to Half-width (Hankaku) ASCII
    and DIGIT.
    Additionally, Full-width wave dash (〜) etc. are normalized

    Parameters
    ----------
    text : str
        Source string.
    mode : Literal['NFC', 'NFD', 'NFKC', 'NFKD'], optional
        Unicode normalization mode.

    Return
    ------
    str
        Normalized string.

    Examples
    --------
    >>> print(jaconv.normalize('ﾃｨﾛ･フィナ〜レ', 'NFKC'))
    ティロ・フィナーレ
    """
    text = text.replace('〜', 'ー').replace('～', 'ー')
    text = text.replace('\u2019', "'").replace('\u201d', '"').replace('\u201c', '"')
    text = text.replace('―', '-').replace('‐', '-').replace('˗', '-').replace('֊', '-')
    text = text.replace('‐', '-').replace('‑', '-').replace('‒', '-').replace('–', '-')
    text = text.replace('⁃', '-').replace('⁻', '-').replace('₋', '-').replace('−', '-')
    text = (
        text.replace('﹣', 'ー')
        .replace('－', 'ー')
        .replace('—', 'ー')
        .replace('―', 'ー')
    )
    text = text.replace('━', 'ー').replace('─', 'ー')
    return unicodedata.normalize(mode, text)  # pyright: ignore[reportArgumentType]
