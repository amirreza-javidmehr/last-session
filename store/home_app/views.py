from django.shortcuts import render
from .models import Product, Comment

def home(request):
    comments_list = Comment.objects.all()
    subject = request.GET.get('subject')
    comment = request.GET.get('comment')
    if subject and comment:
        Comment.objects.create(subject=subject, comment=comment)
    return render(request, 'home_app/index.html', {"comment" : comments_list})
