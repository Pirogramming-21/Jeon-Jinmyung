from django.shortcuts import render, get_object_or_404, redirect
from .models import Idea, DevTool, IdeaStar
from .forms import IdeaForm, DevToolForm
from django.db.models import Count
from django.core.paginator import Paginator

def idea_list(request):
    sort_option = request.GET.get('sort', '-created_at')
    if sort_option == 'stars':
        ideas = Idea.objects.annotate(star_count=Count('ideastar')).order_by('-star_count')
    else:
        ideas = Idea.objects.all().order_by(sort_option)
    
    paginator = Paginator(ideas, 4)  # 페이지당 4개의 게시물
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'ideas/idea_list.html', {'page_obj': page_obj, 'sort_option': sort_option})

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

def devtool_register(request):
    if request.method == "POST":
        form = DevToolForm(request.POST, request.FILES)
        if form.is_valid():
            devtool = form.save(commit=False)
            devtool.save()
            return redirect('devtool_list')  
    else:
        form = DevToolForm()
    return render(request, 'ideas/devtool_register.html', {'form': form})

def devtool_list(request):
    devtools = DevTool.objects.all()
    return render(request, 'ideas/devtool_list.html', {'devtools': devtools})

def devtool_detail(request, pk):
    devtool = get_object_or_404(DevTool, pk=pk)
    return render(request, 'ideas/devtool_detail.html', {'devtool': devtool})

def devtool_edit(request, pk):
    devtool = get_object_or_404(DevTool, pk=pk)
    if request.method == "POST":
        form = DevToolForm(request.POST, request.FILES, instance=devtool)
        if form.is_valid():
            form.save()
            return redirect('devtool_detail', pk=devtool.pk)
    else:
        form = DevToolForm(instance=devtool)
    return render(request, 'ideas/devtool_edit.html', {'form': form, 'devtool': devtool})

def devtool_delete(request, pk):
    devtool = get_object_or_404(DevTool, pk=pk)
    devtool.delete()
    return redirect('devtool_list')

def toggle_star(request, pk):
    idea = get_object_or_404(Idea, pk=pk)
    idea_star, created = IdeaStar.objects.get_or_create(idea=idea)
    if not created:
        idea_star.delete()
    return redirect('idea_list')
