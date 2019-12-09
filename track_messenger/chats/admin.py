from chats.models import Chat, Member, Message, Attachment
from django.contrib import admin
# Register your models here.


class ChatAdmin(admin.ModelAdmin):
    pass

class MessageAdmin(admin.ModelAdmin):
    pass

class AttachmentAdmin(admin.ModelAdmin):
    pass

class MemberAdmin(admin.ModelAdmin):
    pass
    
admin.site.register(Chat, ChatAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(Attachment, AttachmentAdmin)
admin.site.register(Member, MemberAdmin)