from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Cert
from .forms import InputInfoForm

# Create your views here.
def index(request):
    certificates = Cert.objects.all()
    input_form = InputInfoForm()

    data = {
        'certificates': certificates,
        'input_form': input_form,
    }
    return render(request, 'index.html', context=data)

def download_file(request, pk):
    # Отримати екземпляр моделі за допомогою ідентифікатора
    instance = get_object_or_404(Cert, pk=pk)

    # Встановити правильні заголовки відповіді
    response = HttpResponse(instance.cert, content_type='create_pdf_cert/certificates')
    response['Content-Disposition'] = f'attachment; filename="{instance.name}_{instance.course}_{instance.date}"'

    return response