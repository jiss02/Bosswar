from django.shortcuts import render,get_object_or_404,redirect, HttpResponseRedirect
from profiles.models import Profile
from post.models import Post,PostVote
# Create your views here.

def mypage(request):
    votes = PostVote.objects.filter(user_id = request.user.id)
    profile = Profile.objects.get(user_id = request.user.id)

    vote_post = []

    for i in votes:
        vote_post.append(Post.objects.get(id=i.post_id))

    mypost = Post.objects.filter(writer = request.user.id)
    return render(request,'profiles/mypage.html',{'profile':profile,'votes': vote_post,'mypost':mypost})