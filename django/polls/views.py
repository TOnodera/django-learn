from .models import Question
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.http import Http404


def index(request: HttpRequest):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list
    }
    return render(request, 'polls/index.html', context)


def detail(request: HttpRequest, question_id: int):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")

    return render(request, 'polls/detail.html', {'question': question})


def result(request: HttpRequest, question_id: int):
    response = "You're looking at the results of question %s"
    return HttpResponse(response % question_id)


def vote(request: HttpRequest, question_id: int):
    return HttpResponse("You're voting on question %s." % question_id)
