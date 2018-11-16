from django.shortcuts import render, HttpResponse

# html_base = """
# <h1>Mi Web Personal</h1>
# <ul>
#     <li><a href="/">Portada</a></li>
#     <li><a href="/about/">Acerca de</a></li>
#     <li><a href="/portfolio/">Portafolio</a></li>
#     <li><a href="/contact/">Contcacto</a></li>
# </ul>
# """

# Create your views here.
def home(request):
    # html_response = "<h2>Portada</h2>"
    # for i in range(10):
    #     html_response += "Hola Erick <br/>"
    # return HttpResponse(html_base + html_response)
    return render(request, "home.html")

def about(request):
    # return HttpResponse(html_base + """
    # <h2>Acerca de</h2>
    # <p>Consultoría PM</p>
    # <p>Ing. Erick Benites</p>
    # """)
    return render(request, "about.html")
    
# def portfolio(request):
    # return HttpResponse(html_base + """
    # <h2>Portafolio</h2>
    # <ul>
    #     <li>Tecsup App</li>
    #     <li>Simulacro</li>
    #     <li>Ulegacy</li>
    # </ul>
    # """)
    # return render(request, "portfolio.html")
    
def contact(request):
    # return HttpResponse(html_base + """
    # <h2>Contcacto</h2>
    # <p>Erick Benites Cuenca</p>
    # <p>erick.benites@gmail.com</p>
    # """)
    return render(request, "contact.html")