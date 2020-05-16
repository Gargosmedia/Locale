from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class Message(models.Model):
    author = models.ForeignKey(User, related_name='author_messages', on_delete=models.CASCADE)
    chat = models.TextField(default='trashbin')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author.username

    def last_10_messages(chat_id='trashbin'):
        return Message.objects.order_by('-timestamp').all().filter(chat__exact=chat_id)[:10:-1]

class Chat(models.Model):
    chatname = models.CharField(max_length=50)
    min_longitude = models.DecimalField(max_digits=6, decimal_places=4)
    max_longitude = models.DecimalField(max_digits=6, decimal_places=4)

    min_latitude =  models.DecimalField(max_digits=6, decimal_places=4)
    max_latitude =  models.DecimalField(max_digits=6, decimal_places=4)


    def __str__(self):
        return self.chatname

    def ChatsInRange(user_long, user_lat):
        return Message.objects.order_by('chatname').filter(user_long__range=(min_longitude, max_longitude)).filter(user_lat__range=(min_latitude, max_latitude))


