from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def translate(request):
    originalTextValue = request.GET["originalText"]

    translation = ''

    for word in originalTextValue.split():
        if word[0] in ["a", "A", "e", "E", "i", "I", "o", "O", "u"]:
            translation += word
            translation += 'ay '
        else:
            translation += word[1:]
            translation += word[0]
            translation += "ay "

    return HttpResponse(translation)