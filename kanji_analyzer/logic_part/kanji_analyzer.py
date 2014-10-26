#!/usr/bin/python
# coding=utf-8

from kanji_analyzer.logic_part.static_data_for_application import AnalyzerData


class KanjiesText:
    def __init__(self, value):
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    def __str__(self):
        return self.value

    def __repr__(self):
        return "KanjiesText({0})".format(self.value)

    def __len__(self):
        return len(self.value)

    def remove_spaces_from_text(self):
        self.value = self.value.replace("　", "").replace(" ", "")

    def remove_kana_symbols(self):
        for items in AnalyzerData.KANA:
            self.value = self.value.replace(items, "")
            for symb in AnalyzerData.SYMBOLS:
                self.value = self.value.replace(symb, "")

    def take_percent_count(self):
        N5 = self.list_of_kanjies(AnalyzerData.KANJI_JLPT_5)
        N4 = self.list_of_kanjies(AnalyzerData.KANJI_JLPT_4)
        N3 = self.list_of_kanjies(AnalyzerData.KANJI_JLPT_3)
        N2 = self.list_of_kanjies(AnalyzerData.KANJI_JLPT_2)
        N1 = self.list_of_kanjies(AnalyzerData.KANJI_JLPT_1)
        total = len(N1) + len(N2) + len(N3) + len(N4) + len(N5)
        list_result =  [take_percent(total, len(N1)), take_percent(total, len(N2)), take_percent(total, len(N3)), take_percent(total, len(N4)),
                take_percent(total, len(N5))]

        return list_result

    def each_level_kanji(self, kanji_level_list):
        kanjis_this_level = 0
        for items in kanji_level_list:
            counter = 0
            for i in range(len(self)):
                if items == self.value[i]:
                    counter = counter + 1
            if counter != 0:
                kanjis_this_level = counter + kanjis_this_level
        return kanjis_this_level

    def list_of_kanjies(self, kanji_level_list):
        list_kanjis_this_level = []
        for items in kanji_level_list:
            for i in range(len(self)):
                if items == self.value[i]:
                    list_kanjis_this_level.append(items)
        return list(set(list_kanjis_this_level))

    def list_find_kanjies(self):
        N1 = self.list_of_kanjies(AnalyzerData.KANJI_JLPT_1)
        N2 = self.list_of_kanjies(AnalyzerData.KANJI_JLPT_2)
        N3 = self.list_of_kanjies(AnalyzerData.KANJI_JLPT_3)
        N4 = self.list_of_kanjies(AnalyzerData.KANJI_JLPT_4)
        N5 = self.list_of_kanjies(AnalyzerData.KANJI_JLPT_5)
        return [N1, N2, N3, N4, N5]


def take_percent(a, b):
    if b == 0:
        return "0"
    else:
        return "{0}".format(round((b/a)*100))