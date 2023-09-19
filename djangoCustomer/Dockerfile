# Gunakan image base Python
FROM python:3.9

# Set working directory
WORKDIR /app

# Salin file requirements.txt ke dalam kontainer
COPY requirements.txt requirements.txt

# Install dependensi Python
RUN pip install -r requirements.txt

# Salin seluruh proyek Anda ke dalam kontainer
COPY . .

# Expose port yang digunakan oleh Django (biasanya 8000)
EXPOSE 8000

# Perintah untuk menjalankan aplikasi Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
