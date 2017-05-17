from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.conf.urls import url
from django.utils import timezone
from .models import Place
from .forms import NewPlaceForm, CommentForm

# Create your views here.


def place_list(request):
    if request.method == 'POST':
        form = NewPlaceForm(request.POST)
        place = form.save()
        if form.is_valid():
            place.save()
            return redirect('place_list')
    places = Place.objects.all()
    form = NewPlaceForm()
    return render(request, 'travel_wishlist/wishlist.html', {'places':places, 'form':form})


def place_comment(request):
    if request.method == 'POST':
        pk = request.POST.get('pk')
        instance = get_object_or_404(Place, id=pk)
        form = CommentForm(request.POST, instance=instance)
        if form.is_valid():
            post = form.save(commit=False)
            post.date = timezone.now()
            post.visited = True
            post.save()
            return redirect('place_list')
    else:
        form = CommentForm()
    places = Place.objects.all()
    return render(request, 'travel_wishlist/comment.html', {'places_comments': places, 'comment': form})


def places_visited(request):

    visited = Place.objects.filter(visited=True)
    return render(request, 'travel_wishlist/visited.html', {'visited': visited})


def place_is_visited(request):

    if request.method == 'POST':
        pk = request.POST.get('pk')
        place = get_object_or_404(Place, pk=pk)
        place.visited = True
        place.save()
        
    return redirect('place_list')
