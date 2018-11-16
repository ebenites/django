from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "home.html")
    
def about(request):
    return render(request, "about.html")
    
# def services(request):
#     return render(request, "services.html")
    
def store(request):
    return render(request, "store.html")
    
# def contact(request):
#     return render(request, "contact.html")
    
# def blog(request):
#     return render(request, "blog.html")
    
# def sample(request):
#     return render(request, "sample.html")