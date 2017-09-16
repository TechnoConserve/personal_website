import hashlib

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from .models import CustomUser
from blog.models import BlogPage
from .forms import ProfileForm


@login_required
def edit_profile(request):
    user = CustomUser.objects.get(username=request.user.username)
    form = ProfileForm(request.POST or None, instance=user)
    if form.is_valid():
        form.save()
        return redirect('user_profile', request.user.username)
    return render(request, "accounts/edit_profile.html", {'form': form})


def user_profile(request, username):
    user = get_object_or_404(CustomUser, username=username)
    posts = BlogPage.objects.filter(owner=user)

    return render(request, "accounts/user_profile.html", {
        'user_obj': user,
        'email_hash': hashlib.md5(user.email.encode('ascii', 'ignore')).hexdigest(),
        'posts': posts,
    })
