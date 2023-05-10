from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
import json
from .models import Cert

# Create your views here.
def index(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        response_data = {'message':'Success'}
        print(json_data)
        certificates = Cert.objects.all()
        data = {
            'certificates': certificates,
        }        
        return JsonResponse({'success': True})
    else:
        certificates = Cert.objects.all()
        data = {
            'certificates': certificates,
        }        
        return render(request, 'index.html', context=data)



def download_file(request, pk):
    # Отримати екземпляр моделі за допомогою ідентифікатора
    instance = get_object_or_404(Cert, pk=pk)

    # Встановити правильні заголовки відповіді
    response = HttpResponse(instance.cert, content_type='create_pdf_cert/certificates')
    response['Content-Disposition'] = f'attachment; filename="{instance.name}_{instance.course}_{instance.date}"'

    return response

# def generating_file(request)