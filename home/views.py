from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse


def start_page(request):
    t = get_template('home/base.html')
    html = t.render(Context())
    return HttpResponse(html)