
from django.shortcuts import render,HttpResponse
from .forms import petForm
from .models import Pets

def index(request):
    if request.method == 'POST':
        form = petForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return HttpResponse('success')
        else:
            return form.errors.as_data()
    return render(request, 'index.html',{'form': petForm})

def viewPets(request):
    if request.method == 'GET':
        pets_information = Pets.objects.all()
        form = []
        for item in pets_information:
            if item.species == str(1):
                form.append(f"{item.name}: 'dog'")
            elif item.species == str(2):
                form.append(f"{item.name}: 'cat'")
            else:
                form.append(f"{item.name}: 'hamster'")
        return render(request, 'viewPets.html',{'form': form })
