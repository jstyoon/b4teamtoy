from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ProfileForm
from .models import Profile, Follower

@login_required
def edit_profile(request):
    profile = get_object_or_404(Profile, user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, '프로필이 업데이트 되었습니다.')
            return redirect('profile', username=request.user.username)
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'profiles/edit_profile.html', {'form': form})

def profile(request, username):
    profile = get_object_or_404(Profile, user__username=username)
    following = Follower.objects.filter(user=profile.user).count()
    
    #