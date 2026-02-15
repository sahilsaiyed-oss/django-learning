from django.shortcuts import render

def index(request):
    return render(request, 'home/index.html')

def analyze(request):
    djtext = request.POST.get('text', 'default')
    uppercase = request.POST.get('uppercase', 'off')
    extraspace = request.POST.get('extraspace', 'off')
    charcount = request.POST.get('charcount', 'off')

    purpose = ""
    params = {'original_text': djtext}

    if uppercase == "on":
        djtext = djtext.upper()
        purpose += "| Uppercase "

    if extraspace == "on":
        djtext = " ".join(djtext.split())
        purpose += "| Extra Spaces Removed "

    if charcount == "on":
        params['count'] = len(djtext)
        purpose += "| Character Counted "

    params['analyzed_text'] = djtext
    params['purpose'] = purpose
    return render(request, 'home/index.html', params)

def custom_404(request, exception):
    return render(request, 'home/404.html', status=404)
