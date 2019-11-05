from django.shortcuts import render, redirect, get_object_or_404
from .models import Board, Comment
from .forms import BoardForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

# Create your views here.
def index(request):
    boards = Board.objects.all()
    form = CommentForm()
    context = {
        'boards': boards,
        'form': form,
    }
    return render(request, 'board/index.html', context)


def create(request):
    if request.method == "POST":
        form = BoardForm(request.POST)
        if form.is_valid():
            board = form.save(commit=False)
            board.user = request.user
            board.save()
            return redirect('board:index')
    else:
        form = BoardForm()
    context = {
        'form':form
    }
    return render(request, 'board/form.html', context)

@login_required
def like(request, id):
    board = get_object_or_404(Board, id=id)
    user = request.user
    if user in board.user_likes.all():
        board.user_likes.remove(user)
    else:
        board.user_likes.add(user)
    return redirect('board:index')


def comment_create(request, id):
    board = get_object_or_404(Board, id=id)
    user = request.user
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = user
            comment.board = board
            comment.save()
    return redirect("board:index")


@require_POST
def comment_delete(request, id):
    comment = get_object_or_404(Comment, id=id)
    comment.delete()
    return redirect("board:index")


def update(request, id):
    board = get_object_or_404(Board, id=id)
    if request.method == "POST":
        form = BoardForm(request.POST, instance=board)
        if form.is_valid():
            board = form.save(commit = False)
            board.user = request.user
            board.save()
            return redirect('board:index')
    else:
        form = BoardForm(instance=board)
    context = {
        'form': form
    }
    return render(request, "board:form", context)