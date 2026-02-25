from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.conf import settings
from .forms import ContactForm


@csrf_protect
def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # Datos del formulario
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]

            # Construir el mensaje
            full_message = f"Nombre: {name}\nEmail: {email}\n\nMensaje:\n{message}"

            try:
                # Enviar correo
                send_mail(
                    subject=f"Mensaje de contacto de {name}",
                    message=full_message,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[settings.EMAIL_HOST_USER],
                    fail_silently=False,
                )
                return redirect("contact:contact_success")  # ✅ Corregido
            except BadHeaderError:
                return HttpResponse("Cabecera inválida encontrada.")
            except Exception as e:
                return HttpResponse(f"Error al enviar: {e}")
    else:
        form = ContactForm()

    return render(request, "contact/contact.html", {"form": form})


def contact_success(request):
    return render(request, "contact/success.html")
