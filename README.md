# cert_gen
Service for certificates generation
Function generating_file accepts a POST request and user data in JSON format, and generates a PDF certificate based on the provided data. The date is automatically set at the time of creation.
All certificates are saved as PDF files locally. Additionally, certificate models are created in the database.
For clarity and testing purposes, a simple template for entering information has been created (not styled).