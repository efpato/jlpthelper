# -*- coding: utf-8 -*-

from django.contrib import admin

from jlpthelper.apps.tests.models import Question, Answer, Response, Test


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('level', 'question')
    list_filter = ('level',)


admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
admin.site.register(Response)
admin.site.register(Test)
