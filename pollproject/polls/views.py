from django.template import loader
from django.shortcuts import render,get_object_or_404
from django.http import Http404, HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.db.models import F

from .models import Question,Choice


def index(request):
    
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("polls/index.html")
    context = {"latest_question_list": latest_question_list,}
    return HttpResponse(template.render(context,request))


# Create your views here.
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "polls/detail.html", {'question': question})

def results(request, question_id):
    question =get_object_or_404(Question,pk=question_id)
    return render(request, "polls/results.html",{"question":question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except(KeyError,Choice.DoesNotExist):
        #redisplay the question vting form
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes +=1
        selected_choice.save()
        #redirect to the results page
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))