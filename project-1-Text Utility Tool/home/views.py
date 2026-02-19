from django.shortcuts import render
import string
def index(request):
    return render(request, 'home/index.html')

def analyze(request):
    djtext = request.POST.get('text', 'default')
    # NEW: Get Remove Punc checkbox status
    removepunc = request.POST.get('removepunc', 'off')
    
    uppercase = request.POST.get('uppercase', 'off')
    titlecase = request.POST.get('titlecase', 'off')
    reverse = request.POST.get('reverse', 'off')
    extraspace = request.POST.get('extraspace', 'off')
    charcount = request.POST.get('charcount', 'off')
    wordcount = request.POST.get('wordcount', 'off')

    purpose = ""
    params = {'original_text': djtext}

    # NEW: Remove Punctuation Logic
    if removepunc == "on":
        punctuations = string.punctuation
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        djtext = analyzed
        purpose += "| Removed Punctuations "

    if uppercase == "on":
        djtext = djtext.upper()
        purpose += "| Uppercase "

    if titlecase == "on":
        djtext = djtext.title()
        purpose += "| Title Case "

    if reverse == "on":
        djtext = djtext[::-1]
        purpose += "| Reversed Text "

    if extraspace == "on":
        djtext = " ".join(djtext.split())
        purpose += "| Extra Spaces Removed "

    if charcount == "on":
        params['count'] = len(djtext)
        purpose += "| Character Counted "

    if wordcount == "on":
        words = len(djtext.split())
        params['words'] = words
        params['read_time'] = round(words / 200, 2)
        purpose += "| Text Statistics Analyzed "

    params['analyzed_text'] = djtext
    params['purpose'] = purpose
    return render(request, 'home/index.html', params)


def custom_404(request, exception):
    return render(request, 'home/404.html', status=404)
