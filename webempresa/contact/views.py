from django.shortcuts import render, redirect
from django.contrib import messages
from django .core.mail import EmailMessage
from .forms import ContactForm

# Create your views here.
def contact(request):
    contact_form = ContactForm()
    
    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            
            # Send email
            email = EmailMessage(
                "La Caffettiera: Nuevo mensaje de contacto",
                "De {} <{}>\n\nEscribió:\n\n{}".format(name, email, content),
                "no-contestar@inbox.mailtrap.io",
                ["erick.benites@gmail.com"],
                reply_to=[email]
            )
            
            try:
                email.send()
                # Success
                messages.add_message(request, messages.SUCCESS, 'Su mensaje se ha enviado correctamente, en breve nos pondremos en contacto con usted.')
            except:
                messages.add_message(request, messages.ERROR, 'Ocurrió un error inesperado.')
            
            return redirect('contact')
    
    return render(request, "contact.html", {'form': contact_form})