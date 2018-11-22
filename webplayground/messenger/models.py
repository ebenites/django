from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import m2m_changed

# Create your models here.
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['created']
        
class ThreadManager(models.Manager):
    def find(self, user1, user2):
        queryset = self.filter(users=user1).filter(users=user2)
        if len(queryset) > 0:
            return queryset[0]
        return None

    def find_or_create(self, user1, user2):
        thread = self.find(user1, user2)
        if thread is None:
            thread = Thread.objects.create()
            thread.users.add(user1, user2)
        return thread
        
class Thread(models.Model):
    users = models.ManyToManyField(User, related_name='threads')
    messages = models.ManyToManyField(Message)
    updated = models.DateTimeField(auto_now=True)
    
    objects = ThreadManager()
    
    class Meta:
        ordering = ['-updated']
    
# Definiendo la Signal para Thread
def messages_changed(sender, **kwargs):
    instance = kwargs.pop('instance', None) # Thread object
    action = kwargs.pop('action', None)     # pre_add, post_add
    pk_set = kwargs.pop('pk_set', None)     # {thread_messages.id1, thread_messages.id2, ...}
    print(instance, action, pk_set)
    
    if action is 'pre_add':
        false_pk_set = set()
        # Buscar los mensajes de usuarios no suscrutos
        for msg_pk in pk_set:
            msg = Message.objects.get(pk=msg_pk)
            if msg.user not in instance.users.all():
                print("Ups, ({}) no forma parte del hilo".format(msg.user))
                false_pk_set.add(msg_pk)
        # Borramos de pk_set los mensajes que concuerdan con los de false_pk_set
        pk_set.difference_update(false_pk_set)
        
        # Guardar Thread para forzar la actualización del campo updated
        instance.save()
        
# Relacionando la Signal a Thread.messages on m2m_changed
m2m_changed.connect(messages_changed, sender=Thread.messages.through)