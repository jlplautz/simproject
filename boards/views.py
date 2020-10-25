from django.shortcuts import render
from .models import Board


def home(request):
    boards = Board.objects.all()
    return render(request, 'home.html', {'boards': boards})

# ***********************************************
# Second attempt ->  show boards.name
# from django.http import HttpResponse
# def home(request):
#     boards = Board.objects.all()
#     boards_names = list()
#
#     for board in boards:
#         boards_names.append(board.name)
#
#     response_html = '<br>'.join(boards_names)
#
#     return HttpResponse(response_html)


# def home(request):
#     return HttpResponse('Hello.World!!!')
