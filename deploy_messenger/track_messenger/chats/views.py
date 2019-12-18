# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http  import require_GET, require_POST
from chats.forms import ChatForm, MemberForm, MessageForm, AttachmentForm
from django.apps import apps

# Create your views here.
@csrf_exempt
@require_GET
def index(request):
    return render(request, 'index.html')


@csrf_exempt
@require_GET
def chat_detail(request, pk):
    return JsonResponse({'Chat' : pk})


@csrf_exempt
@require_GET
def chat_page(request, chat_id):
    Chat = apps.get_model('chats', 'Chat')
    
    chat = Chat.objects.filter(id=chat_id).values('id', 'is_group_chat', 'topic', 'last_message').first()
    return JsonResponse({'chat': chat})

@csrf_exempt
@require_GET
def chat_list(request):
    Chat = apps.get_model('chats', 'Chat')
    
    chats = Chat.objects.all().values('id', 'is_group_chat', 'topic', 'last_message')
    return JsonResponse({'chat_list': list(chats)})
    
    
@csrf_exempt
@require_POST
def create_personal_chat(request):
    Member = apps.get_model('chats', 'Member')
    Chat = apps.get_model('chats', 'Chat')
        
    uid  = int(request.POST['user_id'])
    target_user_id = int(request.POST['target_user_id'])
    
    first_user = set(Member.objects.filter(user_id=uid).values_list('chat_id'))
    seond_user = set(Member.objects.filter(user_id=target_user_id).values_list('chat_id'))
    
    union_chats = list(first_user & second_user)
    
    if union_chats:
        for i in union_chats:
            chat = Chat.objects.filter(id=i[0]).first()
            
            if not chat.is_group_chat:
                chat_json = {'id': chat.id, 'is_group_chat': chat.is_group_chat, 'topic': chat.topic, 'last_message': chat.last_message}
                return JsonResponse({'chat': chat_json})
        
    chat = Chat.objects.create(is_group_chat=False, topic='', last_message='')
    
    chat_json = {'id': chat.id, 'is_group_chat': chat.is_group_chat, 'topic': chat.topic, 'last_message': chat.last_message }    
    
    member1 = Member.objects.create(user_id=uid, chat_id=chat.id, new_messages=0)            
    member2 = Member.objects.create(user_id=target_user_id, chat_id=chat.id, new_messages=0)
    
    return JsonResponse({'chat': chat_json})
    
    
@csrf_exempt
@require_GET
def user_chat_list(request):
    Member = apps.get_model('chats', 'Member')
    Chat = apps.get_model('chats', 'Chat')
    
    chat_lst = []
    members = Member.objects.filter(user_id=request.GET['uid'])
    
    for member in members:
        chat = Chat.objects.filter(id=member.chat_id).first()
        chat_json = {'id': chat.id, 'is_group_chat': chat.is_group_chat, 'topic': chat.topic, 'last_message': chat.last_message}
        chat_lst.append(chat_json)
    
    return JsonResponse({'chats': chat_lst})


@csrf_exempt
@require_POST
def read_message(request):

    # внести в форму + валидация 
    Member = apps.get_model('chats', 'Member')
    Message = apps.get_model('chats', 'Message')
    
    message = Message.objects.filter(id=int(request.POST['message_id'])).first()
    
    if message:
        member = Member.objects.filter(user_id=int(request.POST['user_id']), chat_id=message.chat_id).first()
        
        if member:
            
            if member.last_read_message == None or member.last_read_message_id < int(request.POST['message_id']):
                member.last_read_message_id = int(request.POST['message_id'])
                member.new_messages -= 1
                member.save()            
            
            return JsonResponse({'chat': member.new_messages})
        return JsonResponse({'member': 'Member not found'}, status=400)
    
    return JsonResponse({'message': 'Message not found'}, status=400)
           
    

@csrf_exempt
@require_POST
def send_message(request):

    # вынести в форму 
    Member = apps.get_model('chats', 'Member')
    Chat = apps.get_model('chats', 'Chat')
    
    form = MessageForm(request.POST)
    
    if form.is_valid():
        print('ok')
        message = form.save()
        msg = {'id': message.id, 'chat_id': message.chat.id, 'user_id': message.user.id, 'content': message.content, 'added_at': message.added_at}
        
        chat = Chat.objects.filter(id=message.chat.id).first()
        
        if chat:
            chat.last_message = message.content
            chat.save()
        
        members = list(Member.objects.filter(chat_id=message.chat.id).exclude(user_id=message.user.id))
        for member in members:
            member.new_messages += 1
            member.save()
        
        
        return JsonResponse({'message': msg})
    
    return JsonResponse({'errors': form.errors}, status=400)


@csrf_exempt
@require_GET
def chat_messages_list(request):
    Message = apps.get_model('chats', 'Message')
    # проверка на сущ чат + добавить проверку на юзера
    if Message.objects.filter(chat_id=request.GET['chat_id']).exists():
        messages = Message.objects.filter(chat_id=request.GET['chat_id']).values('id', 'chat_id', 'user_id', 'content', 'added_at')
        # print(Message.objects.filter(chat_id=request.GET['chat_id']))
        return JsonResponse({'messages': list(messages)})
    else:
        return JsonResponse({'You dont have' : 'such chats'})

@csrf_exempt
@require_POST
def upload_file(request):
    Attachment = apps.get_model('chats', 'Attachment')

    form = AttachmentForm(request.POST, request.FILES)

    if form.is_valid():
        attachment = form.save()

        attachment_json = {'id': attachment.id, 
                           'chat_id': attachment.chat.id, 
                           'user_id': attachment.user.id, 
                           'message_id': attachment.message.id, 
                           'att_type': attachment.att_type,
                           'url': attachment.url.url.replace('http://hb.bizmrg.com/abdrakhimov_track/', '/chats/files/')}

        return JsonResponse({'attachment': attachment_json})


    return JsonResponse({'errors': form.errors}, status=400)

@csrf_exempt
@require_GET
def protected_file(request):
    if request.user.is_authenticated:
        url = request.path.replace('/chats/files', '/protected')
        response = HttpResponse(status=200)
        response['X-Accel-Redirect'] = url

        if 'Expires' in request.GET.keys():
            response['X-Accel-Expires'] = request.GET['Expires']
        response['Content-type'] = ''
        return response
    else:
        return HttpResponse('<h1>File not found</h1>', status=404)