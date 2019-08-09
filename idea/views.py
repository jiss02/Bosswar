from django.shortcuts import render,get_object_or_404, redirect
from .forms import IdeaForm
from .models import Idea
# Create your views here.

def ideaboard(request):
    ideas = Idea.objects.all().order_by('-id')
    return render(request,'idea/ideaboard.html',{'ideas':ideas})

def ideashow(request,idea_id):
    idea= get_object_or_404(Idea,pk = idea_id)
    return render(request, 'idea/ideashow.html', {'idea':idea})

def ideanew(request):
    return render(request,'idea/ideanew.html')

def ideacreate(request):
    if request.method == 'POST':
        form = IdeaForm(request.POST)
        if form.is_valid():
            idea = form.save(commit = False)
            idea.whoseidea = request.user
            idea.save()
            return redirect('ideaboard')
    else:
        form = IdeaForm()
        return render(request,'idea/ideanew.html',{'form':form})

def ideaedit(request):
    return render(request,'idea/ideaedit.html')

def ideaupdate(request, idea_id):
    idea = get_object_or_404(Idea, pk = idea_id)
    if request.method == 'POST':
        form = IdeaForm(request.POST,instance = idea)
        if form.is_valid():
            idea = form.save(commit=False)
            idea.save()
            return redirect('ideashow',idea_id = idea.pk)
    else:
        form = IdeaForm(instance = idea)
        return render(request,'idea/ideaedit.html', {'form':form})

def ideadelete(request, idea_id):
    idea = get_object_or_404(Idea, pk = idea_id)
    idea.delete()
    return redirect('ideaboard')
