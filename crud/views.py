from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, JsonResponse
from . models import question, choice
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from crud.serializers import questionSerializer, choiceSerializer
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import generics

""" list all questions or create a new question """
class Question_list(generics.ListCreateAPIView):
    queryset = question.objects.all()
    serializer_class = questionSerializer

""" list a perticular question or edit or delete question """
class Question_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = question.objects.all()
    serializer_class = questionSerializer




""" list all questions or create a new question """

# class Question_list(APIView):
#     def get(self, request):
#         q = question.objects.all()
#         serializer = questionSerializer(q, many=True)
#         return JsonResponse(serializer.data, safe=False)
#
#     def post(self, request):
#         data = JSONParser().parse(request)
#         serializer = questionSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)
#
#
# """ list a perticular question or edit or delete question """
#
# class Question_detail(APIView):
#     def get_object(self, pk):
#         try:
#             return question.objects.get(pk=pk)
#         except question.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk):
#         q = self.get_object(pk)
#         serializer = questionSerializer(q)
#         return Response(serializer.data)
#
#     def put(self, request, pk):
#         q = self.get_object(pk)
#         serializer = questionSerializer(q, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=400)
#
#     def delete(self, request, pk):
#         q = self.get_object(pk)
#         q.delete()
#         return Response(status=204)


@csrf_exempt
@api_view(['GET'])
def choice_list(request):
    c = choice.objects.all()
    serializer = choiceSerializer(c, many=True)
    return JsonResponse(serializer.data, safe=False)

@csrf_exempt
@api_view(['POST'])
def choice_create(request):
    data = JSONParser().parse(request)
    serializer = choiceSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)


@csrf_exempt
@api_view(['PUT'])
def vote(request, pk):
    if request.method == 'PUT':
        c = get_object_or_404(choice, pk=pk)
        c.votes += 1
        c.save()
        return JsonResponse({'votes': c.votes})







