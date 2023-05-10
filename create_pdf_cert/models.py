from django.db import models

class Cert(models.Model):
    name = models.CharField(max_length=50)
    course = models.CharField(max_length=50)
    date = models.DateField(auto_now=True)
    cert = models.FileField(upload_to=('create_pdf_cert/certificates/'))

    class Meta:
        ordering = ('date',)
        verbose_name_plural = 'Certificates'
        
    def __str__(self):
        return f'{self.id}. {self.name}, {self.date}'
    
