from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def translate(request):
    originalTextValue = request.GET["originalText"]
    translationText = ''

    for word in originalTextValue.split():
        if word[0] in ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]:
            translationText += word
            translationText += 'yay '
        else:
            translationText += word[1:]
            translationText += word[0]
            translationText += "ay "
    return render(request, 'translate.html', {
                    "originalText":originalTextValue, 
                    "translationText":translationText
                    })
        