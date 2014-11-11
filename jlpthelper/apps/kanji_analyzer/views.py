# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from .core import N1, N2, N3, N4, N5
from .core.analyzer import KanjiesText, KanjiesTextError


def analyze(request):
    if request.method == 'POST':
        text = request.POST.get('source')
        try:
            kanji = KanjiesText(text)
            results = [
                {'id': 1, 'value': kanji.n1, 'percent': round(100 * len(kanji.n1) / len(N1))},
                {'id': 2, 'value': kanji.n2, 'percent': round(100 * len(kanji.n2) / len(N2))},
                {'id': 3, 'value': kanji.n3, 'percent': round(100 * len(kanji.n3) / len(N3))},
                {'id': 4, 'value': kanji.n4, 'percent': round(100 * len(kanji.n4) / len(N4))},
                {'id': 5, 'value': kanji.n5, 'percent': round(100 * len(kanji.n5) / len(N5))}
            ]
            return render_to_response('kanji_analyzer/main.html', {'text': text, 'results': results})
        except KanjiesTextError as e:
            return render_to_response('kanji_analyzer/main.html', {'text': text, 'error': e})
    else:
        return render_to_response('kanji_analyzer/main.html')
