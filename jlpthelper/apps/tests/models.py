# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User


LEVELS = (
    ('N1', 'N1'),
    ('N2', 'N2'),
    ('N3', 'N3'),
    ('N4', 'N4'),
    ('N5', 'N5')
)

TEST_TYPES = (
    ('kanjies', 'kanjies'),
    ('vocabulary', 'vocabulary'),
    ('grammar', 'grammar'),
    ('reading', 'reading'),
    ('listening', 'listening'),
)


class Question(models.Model):
    level = models.CharField(max_length=10, choices=LEVELS)
    type = models.CharField(max_length=10, choices=TEST_TYPES)
    question = models.CharField(max_length=1000)
    description = models.CharField(max_length=255)
    image = models.FileField(blank=True)
    audio = models.FileField(blank=True)

    def __str__(self):
        return "Question({0}, {1})".format(self.level, self.question)


class Answer(models.Model):
    question = models.ForeignKey(Question)
    answer = models.CharField(max_length=255)
    is_right = models.BooleanField(default=False)

    def __str__(self):
        return "Answer({0}, '{1}')".format(self.is_right, self.answer)


class Test(models.Model):
    user = User()
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Test('{0}')".format(self.date_created)


class Response(models.Model):
    test = models.ForeignKey(Test)
    question = models.ForeignKey(Question)
    answer = models.ForeignKey(Answer)

    def __str__(self):
        return "Response('{0}', '{1}', '{2}')".format(self.test, self.question, self.answer)
