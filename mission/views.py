from django.shortcuts import render,get_object_or_404
from .models import Mission
from .forms import MissionForm
from post.models import Post, PostVote
import datetime
from django.core.paginator import Paginator
from django.db.models import Count
from django.db.models.aggregates import Max
from django.db.models import Avg, Max, Sum, Count



def index(request): 
    mission = Mission.objects.filter(start_at__lt = datetime.datetime.now()).filter(end_at__gt = datetime.datetime.now()).all()
    posts_all = Post.objects.filter(mission_number_id=mission[0].id).order_by('-id')
    paginator = Paginator(posts_all, 6)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    date = 'Jan 5, 2021 15:37:25'
    date2 = 'Jan. 31, 2020, 11:54 p.m.'
    return render(request, 'mission/index.html',{'posts':posts,'posts_all':posts_all,'mission':mission})

############# 명예의 전당 ##############

def honors(request):
        postvotes = PostVote.objects.all().order_by('post')

        ## 현이 ##
        honors = []
        max = 0
        missions = Mission.objects.values('id')
        now = Mission.objects.filter(start_at__lt = datetime.datetime.now()).filter(end_at__gt = datetime.datetime.now()).all()
        for one in missions:
                if one['id'] == now[0].id:
                        continue
                post_id = -1
                max = -1
                posts = Post.objects.filter(mission_number_id=one["id"])
                if posts:
                        for post in posts:
                                count = post.votelike.count()
                                if max < count:
                                        max = count
                                        post_id = post.id
                        # honors.append([one["id"], post_id])
                        honors.append([get_object_or_404(Mission, pk=one["id"]), get_object_or_404(Post, pk=post_id)])

        return render(request, 'mission/honors.html', {'postvotes': postvotes,'honor':honors})

# 최신 미션 넘버 ->
# PV객체가 많은 순서대로 정렬

########### 명예의 전당 자세히 ############

################# 어바웃 #################

def about(request):
    return render(request, 'mission/about.html')

############# 미션 관련 ################

def new(request):
    return render(request, 'mission/new.html')

def missioncreate(request):
    if request.method == 'POST':
        form = MissionForm(request.POST)
        if form.is_valid():
            mission = form.save(commit=False)
            mission.save()
            return redirect('index')
    else:
        form = MissionForm()
        return render(request, 'mission/new.html', {'form': form})

def missionupdate():
        return any

def missiondelete(request, post_id):
    mission = get_object_or_404(Post, pk = post_id)
    mission.delete()
    return redirect('index')
