# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.core.mail import mail_managers


def home(request):
    return render_to_response('index.html')


def feedback(request):
    error = None
    status = None
    if request.method == 'POST':
        message = request.POST.get('message', '')
        if message:
            mail_managers(
                subject='Feedback',
                message=message,
                fail_silently=True)
            status = 'Ваше сообщение отправлено. Спасибо!'
        else:
            error = 'Сообщение не может быть пустым'
    return render_to_response('feedback.html', {'status': status, 'error': error})
