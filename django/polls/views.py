from .models import Question
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.template import loader


def index(request: HttpRequest):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    tempalte = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list
    }
    return HttpResponse(tempalte.render(context, request))


def detail(request: HttpRequest, question_id: int):
    return HttpResponse('You\'re looking at question %s.' % question_id)


def result(request: HttpRequest, question_id: int):
    response = "You're looking at the results of question %s"
    return HttpResponse(response % question_id)


def vote(request: HttpRequest, question_id: int):
    return HttpResponse("You're voting on question %s." % question_id)
