# from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Page
from .forms import PageForm

from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.
# def pages(request):
#     pages = get_list_or_404(Page)
#     return render(request, 'pages/pages.html', {'pages':pages})

class PageListView(ListView):
    model = Page

# def page(request, page_id, page_slug):
#     page = get_object_or_404(Page, id=page_id)
#     return render(request, 'pages/page.html', {'page':page})

class PageDetailView(DetailView):
    model = Page

@method_decorator(staff_member_required, name="dispatch")
class PageCreateView(SuccessMessageMixin, CreateView):
    model = Page
    # fields = ['title', 'content', 'order']
    form_class = PageForm
    success_message = 'Registro guardado satisfactoriamente.'
    success_url = reverse_lazy('pages:index')

@method_decorator(staff_member_required, name="dispatch")
class PageUpdateView(SuccessMessageMixin, UpdateView):
    model = Page
    # fields = ['title', 'content', 'order']
    form_class = PageForm
    template_name_suffix = '_update_form'
    success_message = 'Registro actualizado satisfactoriamente.'
    success_url = reverse_lazy('pages:index')
    # def get_success_url(self): # reverse_lazy with param
    #     return reverse_lazy('pages:update', args=[self.object.id])

@method_decorator(staff_member_required, name="dispatch")    
class PageDeleteView(SuccessMessageMixin, DeleteView):
    model = Page
    success_message = 'Registro eliminado satisfactoriamente.'
    success_url = reverse_lazy('pages:index')
    def delete(self, request, *args, **kwargs): # https://stackoverflow.com/a/25325228/2823916
        messages.success(self.request, self.success_message)
        return super(PageDeleteView, self).delete(request, *args, **kwargs)