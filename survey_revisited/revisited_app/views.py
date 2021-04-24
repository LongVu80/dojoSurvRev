from django.shortcuts import render, redirect
LOCS = (
    'Houston',
    'Seatle',
    'Dallas',
    'San Jose'
)
LANGS = (
    'JavaScript',
    'Python',
    'Java',
    'C+'
)
FLUE = (
    'JavaScript',
    'Python',
    'Java',
    'C+'
)
def index(request):
    context = {
        'locations': LOCS,
        'languages': LANGS,
        'fluence': FLUE
    }
    return render(request, 'form.html', context)

def process(request):
    if request.method == 'GET':
        return redirect('/')
    request.session['results'] = {
        'name': request.POST['name'],
        'locations': request.POST['locations'],
        'languages': request.POST['languages'],
        'fluence': request.POST.getlist('fluence'),
        'comment': request.POST['comment']
    }
    return redirect('/results')

def results(request):
    context = {
        'results': request.session['results']
    }
    return render(request, 'results.html', context)