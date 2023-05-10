# Generated by Django 4.2.1 on 2023-05-10 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('course', models.CharField(max_length=50)),
                ('date', models.DateField(auto_now=True)),
                ('cert', models.FileField(upload_to='create_pdf_cert/certificates/')),
            ],
            options={
                'verbose_name_plural': 'Certificates',
                'ordering': ('date',),
            },
        ),
    ]