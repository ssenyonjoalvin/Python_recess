from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("HELLO,World. you are at the polls index.")

# Create your views here.
def detail(request, question_id):
    return HttpResponse("you are looking at question %s." % question_id)

def results(request, question_id):
    response = "you are looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("you are voting on question %s." % question_id )