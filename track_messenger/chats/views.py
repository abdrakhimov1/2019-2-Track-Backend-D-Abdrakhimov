from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from django.http import Http404
from django.http import HttpResponseBadRequest
from django.views.generic import View

def chat_list(request):
    #return render(request, 'chat_list.html')
    return JsonResponse({'chat' : 'list'})

#сделать проверку на наличие чата в списке
def chat_details(request):
    if request.method == 'POST':
        chat_id = request.GET.get("id", "no_chat")
        if chat_id == "no_chat":
            raise Http404
        else:
            return JsonResponse({'chat' : chat_id})    
    else:
        return HttpResponseBadRequest()

def contacts_list(request):

    return JsonResponse({'contacts' : 'list'})  

def chat_page(request):
    id = request.GET.get("id", 1)
    return JsonResponse({'chat' : id})