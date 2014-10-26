from django.shortcuts import render_to_response
from kanji_analyzer.logic_part.kanji_analyzer import KanjiesText


def start_kanji(request):
    return render_to_response('kanji_analyzer/main.html')


def show_entries():
    global analyzed_text
    global list_of_percents
    global list_of_find_kanjies
    return render_to_response('show_entries.html', {'analyzed_text': analyzed_text, 'list_of_percents': list_of_percents,
                                                 'list_of_find_kanjies': list_of_find_kanjies,})


def send_text(request):
    if 'q' in request.POST:
        q = request.POST['q']
        a = KanjiesText(request.POST['q'])
        a.remove_spaces_from_text()
        list_of_percents = a.take_percent_count()
        list_of_find_kanjies = a.list_find_kanjies()
        for i in range(0,5):
            if len(list_of_find_kanjies[i]) == 0:
                list_of_find_kanjies[i] = ''
        return render_to_response('kanji_analyzer/main.html', {'q': q, 'list_of_percents': list_of_percents,
                                                 'list_of_find_kanjies': list_of_find_kanjies,})
    else:
        q = "your form is empty"
        return render_to_response('kanji_analyzer/main.html', {'q': q},)