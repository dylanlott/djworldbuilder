from django.shortcuts import render

# Create your views here.

def worlds(request):
    return render(request, 'worlds/worlds.html')

def addWorld(request):
	if request.method == 'POST': 
		form = WorldForm(request.POST)
		if form.is_valid():
			return HttpResponseRedirect('/')
	else: 
		form = WorldForm()

	return render_to_response('addWorld.html', {
		'form': form,
		})