from rest_framework.decorators import api_view
from rest_framework.response import Response
from main import models
from . import serializers

@api_view(['GET'])
def head(request):
    head = models.Head.objects.all().last()
    serializer = serializers.HeadSerializer(head)
    return Response(serializer.data)


@api_view(['GET'])
def get_portfolio(request):
    portfolio = models.Portfolio.objects.all()
    serializer = serializers.PortfolioSerializer(portfolio, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_team(request):
    team = models.Team.objects.all()
    serializer = serializers.TeamSerializer(team, many=True)


@api_view(['GET'])
def get_vacancy(request):
    vacancy = models.Vacancy.objects.all()
    serializer = serializers.VacancySerializer(vacancy, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def post_message(request):
    if request.method == 'POST':
        serializer = serializers.MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['POST'])
def post_resume(request):
    if request.method == 'POST':
        serializer = serializers.ResumeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)