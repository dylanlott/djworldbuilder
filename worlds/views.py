from django.shortcuts import render
from .models import World
from .forms import WorldForm

# Create your views here.

def view_worlds(request):
    ctx = {}

    current_user = request.user
    all_worlds = World.objects.all().filter(created_by = current_user)

    return render(request, 'worlds/worlds.html', {all_worlds: all_worlds})


def create_world(request):
    template = "worlds/templates/worlds/create_world.html"

    if request.method == 'POST':
        form = WorldForm(request.POST)

        if form.is_valid():
            return HttpResponseRedirect('/worlds')

    else: 
        form = WorldForm()

    return render(request, template, {"form": form})
