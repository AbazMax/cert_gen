# cert_gen
Service for certificates generation
Function generating_file accepts a POST request and user data in JSON format, and generates a PDF certificate based on the provided data. The date is automatically set at the time of creation.
All certificates are saved as PDF files locally. Additionally, certificate models are created in the database.
For clarity and testing purposes, a simple template for entering information has been created (not styled).

## Running

1. Clone repository
```
https://github.com/AbazMax/cert_gen.git
```
2. Install requirements
```
pip install -r requirements.txt
```

3. Create superuser to generate DB and Admin panel
```
python manage.py createsuperuser
```

4. To run server
```
python manage.py runserver
```

5. To generate certificate send HTTP request or use homepage (localhost/):
	HTTP method: POST, JSON request example: { “name”: “xxx”, “course”: “yyy” }

6. To get admin panel use entered in p.3 login and password in browser (localhost/admin). There you can manage created certificates.
