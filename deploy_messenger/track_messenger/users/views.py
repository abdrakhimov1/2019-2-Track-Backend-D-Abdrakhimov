from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET, require_POST
from django.apps import apps
# Create your views here.


@csrf_exempt
@require_GET
def index(request):
    return render(request, 'users_index.html')


@csrf_exempt
@require_GET
def profile_details(request, pk):
    User = apps.get_model('users', 'User')
    user = User.objects.filter(id=pk).values('id', 'username', 'first_name', 'avatar').first()
    return JsonResponse({'profile': user})


@csrf_exempt
@require_GET
def contacts_list(request):
    User = apps.get_model('users', 'User')
    
    users= User.objects.all().values('id', 'username', 'first_name', 'avatar')
    return JsonResponse({'contacts': list(users)})
    

@csrf_exempt
@require_GET
def search_users(request):
    User = apps.get_model('users', 'User')
    if User.object.filter(username__contains=request.GET['name']).exists():
        users = User.objects.filter(username__contains=request.GET['name']).values('id', 'username', 'first_name', 'avatar')[:int(request.GET['limit'])]
        return JsonResponse({'users': list(users)})
    else:
        return JsonResponse({'User' : 'NotFound'})