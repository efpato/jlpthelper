#!/usr/bin/env python
# -*- coding: utf-8 -*-

from . import N1, N2, N3, N4, N5, KANJIES


class KanjiesTextError(Exception):
    pass


class KanjiesText:
    def __init__(self, text):
        if not isinstance(text, str):
            text = str(text)
        if not len(text):
            raise KanjiesTextError('Text is empty string')
        self._kanjies = set(text) & KANJIES

    @property
    def kanjies(self):
        return self._kanjies

    @property
    def n1(self):
        return self._kanjies & N1

    @property
    def n2(self):
        return self._kanjies & N2

    @property
    def n3(self):
        return self._kanjies & N3

    @property
    def n4(self):
        return self._kanjies & N4

    @property
    def n5(self):
        return self._kanjies & N5
