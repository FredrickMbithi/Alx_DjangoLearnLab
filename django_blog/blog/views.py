from django.shortcuts import render
from .models import Post


def post_list(request):
    # Fetch all posts from the database
    posts = Post.objects.all().order_by('-published_date')

    # Send data to template
    return render(request, 'blog/index.html', {'posts': posts})

