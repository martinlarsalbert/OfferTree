from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

from .forms import ItemForm,ItemGroupForm

def item(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ItemForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/offer_generator/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ItemForm()

    return render(request, 'offer_generator/item.html', {'form': form})

def item_group(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ItemGroupForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/offer_generator/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ItemGroupForm()

    return render(request, 'offer_generator/item_group.html', {'form': form})