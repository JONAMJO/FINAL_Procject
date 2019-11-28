from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import Http404, HttpResponse, JsonResponse, HttpResponseBadRequest
from .models import Genre, Movie, Review
from .forms import ReviewForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model


def index(request):
    request.session.modified = True
    movies = Movie.objects.all()
    context = {'movies': movies,}
    return render(request, 'movies/index.html', context)


def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    reviews = movie.review_set.all()
    review_form = ReviewForm()
    context = {'movie': movie, 'review_form': review_form, 'reviews': reviews,}
    return render(request, 'movies/detail.html', context)


@require_POST
def reviews_create(request, movie_pk):
    if request.user.is_authenticated:
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.movie_id = movie_pk
            review.user_id = request.user.pk
            review.save()
            return redirect('movies:detail', movie_pk)
    return redirect('movies:detail', movie_pk)


@require_POST
def reviews_delete(request, movie_pk, review_pk):
    if request.user.is_authenticated:
        review = get_object_or_404(Review, pk=review_pk)
        if request.user == review.user:
            review.delete()
            return redirect('movies:detail', movie_pk)
    return HttpResponse('You are Unauthorized', status=401)


@login_required
def reviews_update(request, movie_pk, review_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    review = get_object_or_404(Review, pk=review_pk)
    if request.user == review.user:
        if request.method == 'POST':
            review_form = ReviewForm(request.POST, instance=review)
            if review_form.is_valid():
                review = review_form.save()
                return redirect('movies:detail', movie_pk)
    return redirect('movies:detail', movie_pk)


@login_required
def like(request, movie_pk):
    if request.is_ajax():
        movie = get_object_or_404(Movie, pk=movie_pk)
        if movie.like_users.filter(pk=request.user.pk).exists():
            movie.like_users.remove(request.user)
            liked = False
        else:
            movie.like_users.add(request.user)
            liked = True
        context = {'liked': liked, 'count': movie.like_users.count(),}
        return JsonResponse(context)
    else:
        return HttpResponseBadRequest()


def search(request):
    movies = Movie.objects.all()
    check = request.GET.get('b','')
    if check:
        movies = movies.filter(title__icontains=check)
    context = { 'movies':movies , 'check':check}
    return render(request, 'movies/search.html', context)