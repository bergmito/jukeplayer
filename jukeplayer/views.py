from django.shortcuts import render

# Create your views here.
def player(request):
    return render(request, 'jukeplayer/player.html', {})
