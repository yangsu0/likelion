from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Comment
from django.utils import timezone
from django.shortcuts import redirect


# Create your views here.
def home(request):
    return render(request,'firstpractice/home.html')

def count(request):
    full_text = request.GET['fulltext']
    word_list = full_text.split()
    word_dictionary = {}

    for word in word_list:
        if word in word_dictionary:
            word_dictionary[word] += 1
        else:
            word_dictionary[word] = 1

    return render(request, 'firstpractice/count.html', {'fulltext' : full_text, 'total' : len(word_list), 'dictionary' : word_dictionary.items()})

def about(request):
    return render(request,'firstpractice/about.html')

def com_list(request):
    com_text=Comment.objects
    return render(request, 'firstpractice/com_list.html',{'com_text':com_text})


def text(request):
    comment = Comment()
    comment.content = request.POST['body']
    comment.pub_date = timezone.datetime.now()
    comment.save()
    return redirect('/')
