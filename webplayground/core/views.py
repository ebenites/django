from django.views.generic.base import TemplateView
from django.shortcuts import render

# def home(request):
#     return render(request, "core/home.html")

class HomePageView(TemplateView):
    # template_name =  "core/home.html"
    def get(self, request):
        return render(request, "core/home.html", {'title':'Mi Web Page personal'})
        
# def sample(request):
#     return render(request, "core/sample.html")
    
class SamplePageView(TemplateView):
    template_name =  "core/sample.html"