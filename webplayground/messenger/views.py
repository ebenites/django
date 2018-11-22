from django.shortcuts import render
#from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView
from django.http import Http404, JsonResponse
from .models import Thread, Message
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.
#class ThreadList(ListView)
#    model = Thread
#    
#    # Listar solo la del usuario identificado
#    def get_queryset(self):
#        queryset = super(ThreadList, self).get_queryset()
#        return queryset.filter(users=self.request.user)
#    # No necesario porque se puede usar de la relación user.threads.all()

@method_decorator(login_required, name="dispatch")
class ThreadList(TemplateView):
    template_name = "messenger/thread_list.html"

@method_decorator(login_required, name="dispatch")
class ThreadDetail(DetailView):
    model = Thread
    
    # Validar que el usuario vea el hilo solo si pertenece
    def get_object(self):
        obj = super(ThreadDetail, self).get_object()
        if self.request.user not in obj.users.all():
            raise Http404()
        return obj

@login_required
def add_message(request, pk):
    print(request.GET)
    json_response = {'created':False}
    
    content = request.GET.get('content', None)  # Get with default
    if content:
        thread = get_object_or_404(Thread, pk=pk)
        message = Message.objects.create(user=request.user, content=content)
        thread.messages.add(message)
        json_response['created'] = True
        
        # Si es el primer mensaje informar que refrezque la página
        if len(thread.messages.all()) is 1:
            json_response['first'] = True
    
    return JsonResponse(json_response)
    
@login_required
def start_thread(request, username): # Se inicia o crea el nuevo hilo si no existe
    user = get_object_or_404(User, username=username)
    thread = Thread.objects.find_or_create(user, request.user)
    return redirect(reverse_lazy('messenger:detail', args=[thread.pk]))