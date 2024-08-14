from django.utils import timezone
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
import pytest
from crud.test.factories import choicefactory, questionfactory

@pytest.mark.django_db
def test_get():
    client = APIClient()
    url = reverse('crud:choice_list') #name from the url pattren
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK

@pytest.mark.django_db
def test_post():
    client = APIClient()
    url = reverse('crud:choice_list')
    question = questionfactory(question_text='Original question', pub_date=timezone.now())
    choice = choicefactory(question=question, choice_text='test', votes=1,)
    data = {'choice_text': choice.choice_text, 'votes': choice.votes, 'question': question.id}
    response = client.post(url, data, format='json')
    assert response.status_code == 201
    response_data = response.json()
    assert response_data['choice_text'] == 'test'
    assert response_data['votes'] == 1
    assert response_data['question'] == question.id


@pytest.mark.django_db
def test_votes():
    client = APIClient()
    question = questionfactory(question_text='Original question', pub_date=timezone.now())
    choice = choicefactory(question=question, choice_text='test', votes=1)
    url = reverse('crud:vote', kwargs={'pk': choice.id})
    data = {'choice_text': choice.choice_text, 'votes': choice.votes, 'question': question.id}
    response = client.put(url, data, format='json')
    assert response.status_code == 200
    response_data = response.json()
    print("response data here:", response_data)
    assert response_data['votes'] == choice.votes+1





