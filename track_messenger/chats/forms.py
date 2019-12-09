from django import forms
from chats.models import Chat, Message, Attachment, Member


class ChatForm(forms.ModelForm):
    class Meta:
        model = Chat
        fields = ['is_group_chat', 'topic', 'last_message']
        

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['chat', 'user', 'content', 'added_at']
        
        
class AttachmentForm(forms.ModelForm):
    class Meta:
        model = Attachment
        fields = ['chat', 'user', 'message', 'att_type', 'url']
        

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['user', 'chat', 'new_messages', 'last_read_message']