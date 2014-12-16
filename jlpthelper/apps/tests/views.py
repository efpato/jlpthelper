# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response

from .models import LEVELS, Question


def select_level(request):
    return render_to_response('tests/select_level.html', {'levels': map(lambda level: level[1], LEVELS)})


def main(request):
    return render_to_response('tests/main.html', {'tests': Question.objects.all()})
