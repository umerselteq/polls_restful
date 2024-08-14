from django.urls import path
from . import views
app_name = 'crud'
urlpatterns = [
    path("question/", views.Question_list.as_view(), name="question_list"),
    path("choice/", views.choice_list, name="choice_list"),
    path("post_choice/", views.choice_list, name="choice_list"),
    path("question/<int:pk>", views.Question_detail.as_view(), name="question_detail"),
    path("vote/<int:pk>", views.vote, name="vote"),

]