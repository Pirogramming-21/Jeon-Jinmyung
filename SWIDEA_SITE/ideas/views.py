from django.shortcuts import render, get_object_or_404, redirect
from .models import Idea, DevTool, IdeaStar
from .forms import IdeaForm, DevToolForm
from django.db.models import Count

def idea_list(request):
    sort_option = request.GET.get('sort', '-created_at')  # 기본 정렬 옵션을 최신순으로 설정
    if sort_option == 'stars':
        ideas = Idea.objects.annotate(star_count=Count('ideastar')).order_by('-star_count')
    else:
        ideas = Idea.objects.all().order_by(sort_option)
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

def idea_edit(request, pk):
    idea = get_object_or_404(Idea, pk=pk)
    if request.method == "POST":
        form = IdeaForm(request.POST, request.FILES, instance=idea)
        if form.is_valid():
            form.save()
            return redirect('idea_detail', pk=idea.pk)
    else:
        form = IdeaForm(instance=idea)
    return render(request, 'ideas/idea_edit.html', {'form': form, 'idea': idea})

def idea_delete(request, pk):
    idea = get_object_or_404(Idea, pk=pk)
    idea.delete()
    return redirect('idea_list')