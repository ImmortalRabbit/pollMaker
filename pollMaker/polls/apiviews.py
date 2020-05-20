from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Question, Poll, Choice
from .serializers import PollSerializer, QuestionSerializer, ChoiceSerializer

from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response


@csrf_exempt
@api_view(["POST"])
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=HTTP_200_OK)


@api_view(['POST'])
@permission_classes((IsAuthenticated, IsAdminUser,))
def poll_create(request):
    serializer = PollSerializer(data=request.data)
    if serializer.is_valid():
        poll = serializer.save()
        return Response(PollSerializer(poll).data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PATCH', 'DELETE'])
@permission_classes((IsAuthenticated, IsAdminUser,))
def poll_update(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    if request.method == 'PATCH':
        serializer = PollSerializer(poll, data=request.data, partial=True)
        if serializer.is_valid():
            poll = serializer.save()
            return Response(PollSerializer(poll).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        poll.delete()
        return Response("Poll deleted", status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def polls_view(request):
    polls = Poll.objects.all()
    serializer = PollSerializer(polls, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def poll_view(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    serializer = PollSerializer(poll)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes((IsAuthenticated, IsAdminUser,))
def question_create(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    serializer = QuestionSerializer(data=request.data)
    if serializer.is_valid():
        question = serializer.save()
        return Response(QuestionSerializer(question).data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PATCH', 'DELETE'])
@permission_classes((IsAuthenticated, IsAdminUser,))
def question_update(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'PATCH':
        serializer = QuestionSerializer(question, data=request.data, partial=True)
        if serializer.is_valid():
            question = serializer.save()
            return Response(QuestionSerializer(question).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        question.delete()
        return Response("Question deleted", status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def questions_view(request, poll_id):
    questions = Question.objects.filter(poll=poll_id)
    serializer = QuestionSerializer(questions, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def question_view(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    serializer = QuestionSerializer(question)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes((IsAuthenticated, IsAdminUser,))
def choices_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    serializer = ChoiceSerializer(data=request.data)
    if serializer.is_valid():
        choice = serializer.save(question=question)
        return Response(ChoiceSerializer(choice).data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PATCH', 'DELETE'])
@permission_classes((IsAuthenticated, IsAdminUser,))
def choices_update(request, choice_id):
    choice = get_object_or_404(Choice, pk=choice_id)
    if request.method == 'PATCH':
        serializer = ChoiceSerializer(choice, data=request.data, partial=True)
        if serializer.is_valid():
            choice = serializer.save()
            return Response(ChoiceSerializer(choice).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        choice.delete()
        return Response("Choice deleted", status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def choices_view(request, question_id):
    choices = Choice.objects.filter(question=question_id)
    serializer = QuestionSerializer(choices, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def choice_view(request, choice_id):
    choice = get_object_or_404(Choice, pk=choice_id)
    serializer = QuestionSerializer(choice)
    return Response(serializer.data)
