from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
import json
from .models import Cert
from fpdf import FPDF


# Create your views here.
def index(request):
    certificates = Cert.objects.all()
    data = {
        'certificates': certificates,
    }        
    return render(request, 'index.html', context=data)


def download_file(request, pk):
    instance = get_object_or_404(Cert, pk=pk)
    response = HttpResponse(instance.cert, content_type='create_pdf_cert/certificates')
    response['Content-Disposition'] = f'attachment; filename="{instance.name}_{instance.course}_{instance.date}"'

    return response



class PDF(FPDF):
    # def set_template(self, template_path):
    #     self.template_path = template_path

    # def header(self):
    #     self.image(self.template_path, 0, 0, self.w, self.h)

    def header(self):
        # Завантаження зображення шаблону у форматі PNG
        self.image('static/img/template.png', 0, 0, self.w, self.h)  # Налаштуйте розміри зображення під свої потреби

    def add_name(self, text):
        # Додавання тексту на сторінку
        self.set_font('Arial', '', 12)  # Налаштуйте шрифт та розмір під свої потреби
        self.set_xy(30, 50)  # Налаштуйте положення тексту на сторінці під свої потреби
        self.multi_cell(150, 10, text)

    def add_course(self, text):
        # Додавання тексту на сторінку
        self.set_font('Arial', '', 12)  # Налаштуйте шрифт та розмір під свої потреби
        self.set_xy(100, 200)  # Налаштуйте положення тексту на сторінці під свої потреби
        self.multi_cell(150, 10, text)    


def generating_file(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        print(json_data)                        #for check data
        pdf = PDF('L')
        pdf.add_page()
        pdf.add_name(json_data['name'])
        pdf.add_course(json_data['course'])
        pdf.output('NewFile.pdf', 'F')

        return JsonResponse({'success': True})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)
