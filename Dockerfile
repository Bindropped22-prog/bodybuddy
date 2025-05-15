# Use official Python image as a base
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy project files
COPY . /app/

# Collect static files (optional if you manage static externally)
RUN python manage.py collectstatic --noinput

# Expose the port for Fly
EXPOSE 8080

#Gunicorn setting
CMD ["gunicorn", "bodybuddy.wsgi:application", "--bind", "0.0.0.0:8080", "--timeout", "60"]
