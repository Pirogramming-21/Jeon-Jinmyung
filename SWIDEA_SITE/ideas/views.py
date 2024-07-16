from django.shortcuts import render, get_object_or_404, redirect
from .models import Idea, DevTool, IdeaStar
from .forms import IdeaForm, DevToolForm

def idea_list(request):
    ideas = Idea.objects.all().order_by('-created_at')
    return render(request, 'ideas/idea_list.html', {'ideas': ideas})

def idea_detail(request, pk):
    idea = get_object_or_404(Idea, pk=pk)
    return render(request, 'ideas/idea_detail.html', {'idea': idea})

def idea_register(request):
    if request.method == "POST":
        form = IdeaForm(request.POST, request.FILES)
        if form.is_valid():
            idea = form.save(commit=False)
            idea.save()
            return redirect('idea_list')
    else:
        form = IdeaForm()
    return render(request, 'ideas/idea_register.html', {'form': form})

def idea_edit(request):
    return 