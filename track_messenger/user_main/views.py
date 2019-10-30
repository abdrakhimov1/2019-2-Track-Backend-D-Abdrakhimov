from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from django.http import Http404
from django.views.generic import View

def start_page(request):
    return render(request, 'main_page.html')

def profile(request):

    return JsonResponse({'my' : 'profile'})