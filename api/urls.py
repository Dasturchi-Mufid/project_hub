from django.urls import path
from . import views

urlpatterns = [
    path('headers/',views.head),
    path('portfolios/',views.get_portfolio),
    path('teams/',views.get_team),
    path('vacancies/',views.get_vacancy),
    path('post-message/',views.post_message),
    path('post-resume/',views.post_resume),
]