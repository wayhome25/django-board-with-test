from django.http import HttpResponse
from django.shortcuts import render

from boards.models import Board


def home(request):
    boards = Board.objects.all()
    return render(request, 'home.html', {'boards': boards})
