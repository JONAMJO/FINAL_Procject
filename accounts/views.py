from IPython import embed
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_http_methods
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponseBadRequest
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from . forms import CustomUserChangeForm, CustomUserCreationForm
from movies.models import Movie
from .models import User


@require_http_methods(["GET", "POST"])
def signup(request):
    if request.user.is_authenticated:
        return redirect('movies:index')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('movies:index')
    else:
        form = CustomUserCreationForm()
    context = {'form': form,}
    return render(request, 'accounts/auth_form.html', context)


def login(request):
    if request.user.is_authenticated:
        return redirect('movies:index')

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('movies:index')
    else:
        form = AuthenticationForm()
    context = {'form': form,}
    return render(request, 'accounts/login.html', context)


@login_required
def logout(request):
    auth_logout(request)
    return redirect('movies:index')


@require_POST
def delete(request):
    request.user.delete()
    return redirect('movies:index')


@login_required
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('movies:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {'form': form,}
    return render(request, 'accounts/auth_form.html', context)


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('movies:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {'form': form,}
    return render(request, 'accounts/auth_form.html', context)


@login_required    
def index(request):
    users = User.objects.all()
    context = {'users': users}
    return render(request, 'accounts/index.html', context)

@login_required
def profile(request, user_pk):
    people = get_object_or_404(get_user_model(), pk=user_pk)
    context = {'people': people}
    return render(request, 'accounts/profile.html', context)


@login_required
def follow(request, user_pk):
    if request.is_ajax():
        users = get_object_or_404(get_user_model(), pk=user_pk)
        if request.user in users.followers.all():
            users.followers.remove(request.user)
            followed = False
        else:
            users.followers.add(request.user)
            followed = True
        context = {'followed': followed,}
        return JsonResponse(context)
    else:
        return HttpResponseBadRequest()
    

@login_required
def followings(request, user_pk):
    people = get_object_or_404(get_user_model(), pk=user_pk)
    context = {'people': people}
    return render(request, 'accounts/follow.html', context)
    
@login_required
def followers(request, user_pk):
    people = get_object_or_404(get_user_model(), pk=user_pk)
    context = {'people': people}
    return render(request, 'accounts/follow.html', context)