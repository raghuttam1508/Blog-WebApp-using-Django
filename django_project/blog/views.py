from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        "author": "Raghuttam",
        "title": "blog first post",
        "content": "First post content",
        "date_posted": "Augest 27 2022",
    },
    {
        "author": "Jane Doe",
        "title": "blog Second post",
        "content": "Second post content",
        "date_posted": "Augest 28 2023",
    },
]


def home(request):
    context = {"posts": posts}
    return render(request, "blog/home.html", context)


def about(request):
    return render(request, "blog/about.html", {"title": "About"})


# Create your views here.
