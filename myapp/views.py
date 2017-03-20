from django.shortcuts import render
from channels import Channel


def index(request):
    return render(request, "index.html")
