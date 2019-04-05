from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Comment


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
    com_text=Comment.object.all().order_by('-pub_date')
    context={'com_text':com_text}
    return render(request, 'firstpractice/com_list.html',context)

"""
def text(request):
    com_text=Comment.objects.all()
    try:
        context=com_text.Comment_set.get(pk=request.POST[''])
    except (KeyError, Comment.DoesNotExist):
        return render(request,'firstpractice/home.html',{'com_text':com_text})
    else:
        context.save()
        return HttpResponseRedirect(reverse('app_name:url'))
        """
"""
def text(request):
    comment = Comment.objects.all()
    try:
        context = comment.get(request.POST[''])
"""
def text(request):
    if request.method=='POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/feedback/list')
    else:
        form = CommentForm()
 
    return render(request, 'submit.html', {'form': form})
