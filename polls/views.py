# from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import Question, Choice, Beast, Book
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .forms import SignUpForm, BeastForm, BookForm
from django.core import serializers

def index(request):
  latest_question_list = Question.objects.order_by('-pub_date')[:5]
  template = loader.get_template('polls/index.html')
  context = { 'latest_question_list': latest_question_list }
  return HttpResponse(template.render(context, request))

def detail(request, question_id):
  question = get_object_or_404(Question, pk=question_id)
  return render(request, 'polls/detail.html', { 'question': question })

def results(request, question_id):
  response = "You're looking at the results of question %s."
  return HttpResponse(response % question_id)

def vote(request, question_id):
  question = get_object_or_404(Question, pk=question_id)
  try:
    selected_choice = question.choice_set.get(pk=request.POST['choice'])
  except (KeyError, Choice.DoesNotExist):
    return render(request, 'polls/detail.html', { 'question': question, 'error_message': 'you did not select a choice' })
  else:
    selected_choice.votes+=1
    selected_choice.save()
    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def signin(request):
  return HttpResponse('signin')

def signup(request):
  return render(request, 'polls/signup.html')

def signupCreate(request):
  return render(request, 'polls/signup.html')

def book(request):
  return render(request, "polls/book.html", { "form": BookForm() })

def bookDetail(request, book_id):
  return JsonResponse({ 'data': list(Book.objects.filter(pk=book_id).values()) }, safe=False)
  
def bookList(request):
  return render(request, "polls/book-list.html", { "list": list(Book.objects.values()) })
  
def bookCreate(request):
  if request.method == 'POST':
    form = BookForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect('/polls/book/list/')  # CAN RE-EDIT BY YOUR IDEA
  return HttpResponse('something went wrong')

def bookUpdate(request):
  print('=====', request.POST['id'], request.POST['title'])
  id = request.POST['id']
  title = request.POST['title']
  b = Book.objects.get(pk=id)
  b.title = title
  b.save()
  return HttpResponse('bookUpdate')

def bookDelete(request):
  id = request.POST['id']
  b = Book.objects.get(pk=id)
  b.delete()
  # NEED TO REMOVE FILE FROL MEDIA FOLDER 
  return HttpResponse('bookDelete')
    
def addbeast(request):
  return HttpResponse('add beast')
  # if request.method == 'POST':
  #   form = BeastForm(request.POST, request.FILES)
  #   if form.is_valid():
  #     form.save()
  #     return JsonResponse(list(Beast.objects.values()), safe=False)
  # else:
  #     form = BeastForm()
  # return render(request, "polls/addbeast.html", { "form": form })