from django.shortcuts import render, get_object_or_404, redirect
from .models import Review
# Create your views here.
def review_list(request):
    reviews = Review.objects.all()
    return render(request, 'posts/review_list.html', {'reviews': reviews})

def review_detail(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    return render(request, 'posts/review_detail.html', {'review': review})

def review_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        director = request.POST.get('director')
        actors = request.POST.get('actors')
        release_year = request.POST.get('release_year')
        genre = request.POST.get('genre')
        rating = request.POST.get('rating')
        runtime = request.POST.get('runtime')
        content = request.POST.get('content')

        Review.objects.create(
            title=title,
            director=director,
            actors=actors,
            release_year=release_year,
            genre=genre,
            rating=rating,
            runtime=runtime,
            content=content
        )
        return redirect('posts:review_list')
    return render(request, 'posts/review_form.html')

def review_update(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    if request.method == 'POST':
        review.title = request.POST.get('title')
        review.director = request.POST.get('director')
        review.actors = request.POST.get('actors')
        review.release_year = request.POST.get('release_year')
        review.genre = request.POST.get('genre')
        review.rating = request.POST.get('rating')
        review.runtime = request.POST.get('runtime')
        review.content = request.POST.get('content')
        review.save()
        return redirect('posts:review_detail', review_id=review.id)
    return render(request, 'posts/review_form.html', {'review': review})

def review_delete(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    review.delete()
    return redirect('posts:review_list')