from main import models
from rest_framework.serializers import ModelSerializer

class HeadSerializer(ModelSerializer):
    class Meta:
        model = models.Head
        fields = '__all__'


class PortfolioSerializer(ModelSerializer):
    class Meta:
        model = models.Portfolio
        fields = '__all__'


class TeamSerializer(ModelSerializer):
    class Meta:
        model = models.Team
        fields = '__all__'


class MessageSerializer(ModelSerializer):
    class Meta:
        model = models.Message
        fields = '__all__'


class ResumeSerializer(ModelSerializer):
    class Meta:
        model = models.Resume
        fields = '__all__'


class VacancySerializer(ModelSerializer):
    class Meta:
        model = models.Vacancy
        fields = '__all__'
        