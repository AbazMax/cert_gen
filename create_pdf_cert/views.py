from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
import json
from .models import Cert
from fpdf import FPDF
from datetime import datetime

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
    def header(self):
        self.image('static/img/template.png', 0, 0, self.w, self.h)

    def add_name(self, text):
        self.set_font('Arial', 'B', 34)
        self.set_xy(90, 87)
        self.multi_cell(150, 10, text)

    def add_course(self, text):
        self.set_font('Arial', 'B', 26)
        self.set_xy(93, 125)
        self.multi_cell(150, 10, text, align='L')

    def add_date(self, text):
        self.set_font('Arial', '', 20)
        self.set_xy(97, 160)
        self.multi_cell(150, 10, text)         


def generating_file(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        new_cert = Cert()
        new_cert.name = json_data['name']
        new_cert.course = json_data['course']
        file_path = f'create_pdf_cert/certificates/{new_cert.name}_{new_cert.course}.pdf'
        new_cert.cert = file_path
        new_cert.save()
        pdf = PDF('L')
        pdf.add_page()
        pdf.add_name(json_data['name'])
        pdf.add_course(json_data['course'])
        pdf.add_date(f'{new_cert.date.strftime("%d.%m.%Y")}')
        pdf.output(file_path, 'F')

        return JsonResponse({'success': True})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)
