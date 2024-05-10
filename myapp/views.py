from django.shortcuts import render
from django.http import JsonResponse


def hello(request):
	data = {'message':'Hello ,World!'}
	return JsonResponse(data)

# Create your views here.
