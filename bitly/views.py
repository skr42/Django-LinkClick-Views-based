from django.shortcuts import render , get_object_or_404, redirect
from django.urls import reverse

from .forms import LinkForm
from .models import Link

# Create your views here.
def index(request):
    links=Link.objects.all()
    context={
        "links":links
    }
    return render(request,'index.html',context)


def root_link(request, link_slug):
    link = get_object_or_404(Link, slug=link_slug)
    link.click() #this will increment the clicks


    return redirect(link.url)


def add_link(request):
    if request.method == "POST":
        form = LinkForm(request.POST)
        if form.is_valid():
            # if the form is valid - then process
            form.save()
            return redirect(reverse('home'))

    else:
        form = LinkForm()

    context = {
        "form": form
    }
    return render(request, 'create.html', context)