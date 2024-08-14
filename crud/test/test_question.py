from django.utils import timezone
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
import pytest
from crud.test.factories import questionfactory



@pytest.mark.django_db
def test_create_post():
    client = APIClient()
    url = reverse('crud:question_list')
    data = {'question_text': 'test question', 'pub_date': timezone.now()}
    response = client.post(url, data, format='json')
    print(response.data)
    assert response.status_code == 201
    assert response.data['question_text'] == 'test question'

@pytest.mark.django_db
def test_create_put():
    client = APIClient()
    question = questionfactory(question_text='Original question', pub_date=timezone.now())
    url = reverse('crud:question_detail', kwargs={'pk': question.pk})
    data = {'question_text': 'updated test question', 'pub_date': timezone.now().isoformat()}
    response = client.put(url, data, format='json')
    assert response.status_code == status.HTTP_200_OK
    assert response.data['question_text'] == 'updated test question'

@pytest.mark.django_db
def test_create_del():
    client = APIClient()
    question = questionfactory(question_text='Original question', pub_date=timezone.now())
    url = reverse('crud:question_detail', kwargs={'pk': question.pk})
    response = client.delete(url)
    assert response.status_code == 204
    response = client.get(url)
    response_data = response.json()
    print(response_data)
    assert response.status_code == status.HTTP_404_NOT_FOUND


